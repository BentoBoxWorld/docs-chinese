import csv
import json
import logging
import os

import requests
import yaml

log = logging.getLogger("mkdocs.macros.translations")

# Friendly names for the locale codes we expect to encounter. Anything not
# listed here will fall back to its bare locale code as the display name.
LANGUAGE_NAMES = {
    "zh-CN": "中文（中国）",
    "zh-HK": "中文（香港）",
    "zh-TW": "中文（台湾）",
    "hr": "克罗地亚语",
    "cs": "捷克语",
    "nl": "荷兰语",
    "fr": "法语",
    "de": "德语",
    "hu": "匈牙利语",
    "id": "印尼语",
    "it": "意大利语",
    "ja": "日语",
    "ko": "韩语",
    "lv": "拉脱维亚语",
    "pl": "波兰语",
    "pt": "葡萄牙语",
    "pt-BR": "葡萄牙语（巴西）",
    "en-GB": "英语（英国）",
    "es-ES": "西班牙语（西班牙）",
    "fr-FR": "法语（法国）",
    "ro": "罗马尼亚语",
    "ru": "俄语",
    "es": "西班牙语",
    "tr": "土耳其语",
    "uk": "乌克兰语",
    "vi": "越南语",
}

# Module-level cache so each (repo, branch) is fetched at most once per build,
# even though several pages may reference the same repo.
_translations_cache: dict = {}

GITHUB_ORG = "BentoBoxWorld"
LOCALES_PATH = "src/main/resources/locales"
ENGLISH_FILE = "en-US.yml"


def _gh_session():
    s = requests.Session()
    s.headers.update({"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        s.headers["Authorization"] = f"token {token}"
    return s


def _flatten_yaml(data, prefix=""):
    """Flatten a nested YAML mapping into {dotted.key: leaf_value}."""
    out = {}
    if isinstance(data, dict):
        for k, v in data.items():
            key = f"{prefix}.{k}" if prefix else str(k)
            out.update(_flatten_yaml(v, key))
    elif isinstance(data, list):
        # Treat the whole list as a single leaf — translators usually
        # translate the list as a unit.
        out[prefix] = "\n".join(str(x) for x in data)
    else:
        out[prefix] = data
    return out


def _is_translated(value, english_value) -> bool:
    """A key counts as translated if it has a non-empty string value that
    differs from the English source."""
    if value is None:
        return False
    if isinstance(value, str) and not value.strip():
        return False
    return value != english_value


def _fetch_translation_status(repo: str, branch: str):
    """Return a list of dicts: {code, name, url, percent} for every locale
    file in the repo (excluding en-US.yml). On failure returns None."""
    cache_key = (repo, branch)
    if cache_key in _translations_cache:
        return _translations_cache[cache_key]

    session = _gh_session()
    api_url = (
        f"https://api.github.com/repos/{GITHUB_ORG}/{repo}/contents/"
        f"{LOCALES_PATH}?ref={branch}"
    )
    try:
        r = session.get(api_url, timeout=15)
        if r.status_code == 404:
            # The repo has no locales/ directory at all — distinct from a
            # transient failure so callers can render an accurate message.
            _translations_cache[cache_key] = "missing"
            return "missing"
        if r.status_code != 200:
            log.warning(
                "translations(%s): GitHub listing returned %s", repo, r.status_code
            )
            _translations_cache[cache_key] = None
            return None
        listing = r.json()
    except Exception as e:  # network errors, JSON errors, etc.
        log.warning("translations(%s): listing failed: %s", repo, e)
        _translations_cache[cache_key] = None
        return None

    yml_files = [
        item for item in listing
        if isinstance(item, dict)
        and item.get("type") == "file"
        and item.get("name", "").endswith(".yml")
    ]
    en_entry = next((f for f in yml_files if f["name"] == ENGLISH_FILE), None)
    if en_entry is None:
        log.warning("translations(%s): no %s in repo", repo, ENGLISH_FILE)
        _translations_cache[cache_key] = None
        return None

    def _raw(file_entry):
        url = file_entry.get("download_url")
        if not url:
            return None
        try:
            rr = session.get(url, timeout=15)
            if rr.status_code != 200:
                return None
            return rr.text
        except Exception:
            return None

    en_text = _raw(en_entry)
    if en_text is None:
        log.warning("translations(%s): could not fetch %s", repo, ENGLISH_FILE)
        _translations_cache[cache_key] = None
        return None

    try:
        en_flat = _flatten_yaml(yaml.safe_load(en_text) or {})
    except yaml.YAMLError as e:
        log.warning("translations(%s): could not parse %s: %s", repo, ENGLISH_FILE, e)
        _translations_cache[cache_key] = None
        return None

    total = len([k for k, v in en_flat.items() if v not in (None, "")])
    if total == 0:
        total = len(en_flat) or 1

    results = []
    for entry in yml_files:
        name = entry["name"]
        if name == ENGLISH_FILE:
            continue
        code = name[:-4]  # strip .yml
        text = _raw(entry)
        percent = None
        if text is not None:
            try:
                flat = _flatten_yaml(yaml.safe_load(text) or {})
                translated = sum(
                    1 for k, en_v in en_flat.items()
                    if _is_translated(flat.get(k), en_v)
                )
                percent = round(translated * 100 / total)
            except yaml.YAMLError as e:
                log.warning("translations(%s): could not parse %s: %s", repo, name, e)
        results.append({
            "code": code,
            "name": LANGUAGE_NAMES.get(code, code),
            "url": (
                f"https://github.com/{GITHUB_ORG}/{repo}/blob/{branch}/"
                f"{LOCALES_PATH}/{name}"
            ),
            "percent": percent,
        })

    # Sort by display name for stable, readable output.
    results.sort(key=lambda x: x["name"].lower())
    _translations_cache[cache_key] = results
    return results


def define_env(env):

    @env.macro
    def translations(repo: str, branch: str = "develop"):
        intro = (
            '!!! note "帮助我们保持翻译准确"\n'
            "    现在 BentoBox 及其插件的大多数翻译已借助 AI 完成——大部分工作已经做好，\n"
            "    但 **AI 并不完美**。我们真正需要社区提供的是**错误报告和纠正**。\n"
            "\n"
            "    * 发现错误或措辞不当？请在 [bentobox.world](https://bentobox.world)\n"
            "    的相关仓库（我们 GitHub 组织的短链接）上提交 issue 或 PR，或者在\n"
            "    [Discord](https://discord.bentobox.world) 上告知我们。\n"
            "    * 想要添加全新语言？请在相关仓库的 `src/main/resources/locales/` 目录下\n"
            "    提交包含新语言文件的 PR，或在 Discord 上联系我们，我们会为你提供帮助。\n"
            "\n"
        )

        en_url = (
            f"https://github.com/{GITHUB_ORG}/{repo}/blob/{branch}/"
            f"{LOCALES_PATH}/{ENGLISH_FILE}"
        )
        header = (
            "| 语言 | 语言代码 | 进度 |\n"
            "| ---------- | --- | ----------- |\n"
            f"| [英语（美国）]({en_url}) | `en-US` | 100%（默认）|\n"
        )

        rows = _fetch_translation_status(repo, branch)
        if rows == "missing":
            # No locales/ directory in the repo — this addon currently has
            # no translatable strings.
            note = (
                f"\n_此项目目前尚无可翻译的语言文件。目前仅提供英语版本。_\n"
            )
            return intro + header + note
        if rows is None:
            # Network/parse failure — render a graceful fallback that still
            # links to the locales directory on GitHub.
            locales_url = (
                f"https://github.com/{GITHUB_ORG}/{repo}/tree/{branch}/"
                f"{LOCALES_PATH}"
            )
            fallback = (
                f"\n_翻译状态目前不可用。请直接在 [GitHub]({locales_url}) 上浏览语言文件。_\n"
            )
            return intro + header + fallback

        body = ""
        for row in rows:
            pct = f"{row['percent']}%" if row["percent"] is not None else "?"
            body += (
                f"| [{row['name']}]({row['url']}) | `{row['code']}` | {pct} |\n"
            )
        return intro + header + body

    @env.macro
    def addon_description(addon_name:str, beta:bool=False):
        result = ""

        if beta:
            result += f"""!!! warning
    **{addon_name}** 目前处于 **Beta 测试阶段**。\n
    请记住，**您可能会遇到更多的错误** 且 **某些功能可能不够稳定**。\n\n"""

        result += f"""!!! info "有用的链接"
    - [GitHub 仓库](https://github.com/BentoBoxWorld/{addon_name})
    ([发布版本](https://github.com/BentoBoxWorld/{addon_name}/releases))
    - [问题跟踪器](https://github.com/BentoBoxWorld/{addon_name}/issues)
    - [开发构建版本](https://ci.codemc.org/job/BentoBoxWorld/job/{addon_name})
    ([最新稳定构建](https://ci.codemc.io/job/BentoBoxWorld/job/{addon_name}/lastStableBuild/))"""

        return result

    @env.macro
    def placeholders_bundle(gamemode_name:str):
        result = ""
        source = ""

        # Let's read the csv file
        with open('data/placeholders.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Analyze the source
                if (row['source'] != source):
                    if ("[gamemode]" in row['placeholder'] or gamemode_name in row['placeholder']):
                        # We are in a new "source" so we have to put the header
                        source = row['source']
                        result += f"""\n## {source} placeholders

| Placeholder | Description | {source} version
| ---------- | ---------- | ---------- |
"""

                if ("[gamemode]" in row['placeholder'] or gamemode_name in row['placeholder']):
                    result += f"| `%{row['placeholder'].replace('[gamemode]',gamemode_name)}%` | {row['desc']} | {row['version']} |\n"

        return result

    # Adds placeholder table to the addon pages.
    @env.macro
    def placeholders_source(source:str):
        result = f"""!!! tip "提示"\n
    `[gamemode]` 是一个前缀，根据你运行的游戏模式而有所不同。\n
    前缀是游戏模式名称的小写形式，即如果你正在使用 BSkyBlock，前缀则为 `bskyblock`。\n\n
    每个游戏模式正确翻译的占位符可以在以下位置找到：\n
    - [AcidIsland](/en/latest/gamemodes/AcidIsland/Placeholders)
    - [AOneBlock](/en/latest/gamemodes/AOneBlock/Placeholders)
    - [Boxed](/en/latest/gamemodes/Boxed/Placeholders)
    - [BSkyBlock](/en/latest/gamemodes/BSkyBlock/Placeholders)
    - [CaveBlock](/en/latest/gamemodes/CaveBlock/Placeholders)
    - [SkyGrid](/en/latest/gamemodes/SkyGrid/Placeholders).\n
    请阅读主要的[占位符页面](/en/latest/BentoBox/Placeholders).\n\n"""

        result += f"""\n

| Placeholder | Description | {source} version
| ---------- | ---------- | ---------- |
"""

        # Let's read the csv file
        with open('data/placeholders.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Analyze the source
                if (row['source'] == source):
                    # We are in our plugin, populate rows
                    result += f"| `%{row['placeholder']}%` | {row['desc']} | {row['version']} |\n"

        return result


    # Creates a table of requested flags type.
    @env.macro
    def flags_bundle(type:str):
        result = ""
        source = ""

        # Let's read the csv file
        with open('data/flags.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Analyze the source
                if (row['source'] != source):
                    # We are in a new "source" so we have to put the header
                    source = row['source']

                    if (row['type'] == type) or (type == "WORLD_DEFAULT_PROTECTION" and row['type'] == "PROTECTION"):
                        if (type == "PROTECTION"):
                            result += f"""\n## {source} {type.replace("_", " ").capitalize()} flags

| | Flag ID | Flag | Description | Default | Min Rank | Max Rank |
| - | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
"""
                        else:
                            result += f"""\n## {source} {type.replace("_", " ").capitalize()} flags

| | Flag ID | Flag | Description | Default |
| - | ---------- | ---------- | ---------- | ---------- |
"""

                if (row['type'] == type) or (type == "WORLD_DEFAULT_PROTECTION" and row['type'] == "PROTECTION"):
                    if (type == "PROTECTION"):
                        result += f"| <span class='icon-minecraft {icon_css(row['icon'])}'></span> | {row['flag']} | {row['name']} | {row['description']} | {row['default']} | {row['min']} | {row['max']} |\n"
                    else:
                        result += f"| <span class='icon-minecraft {icon_css(row['icon'])}'></span> | {row['flag']} | {row['name']} | {row['description']} | {row['default']} |\n"

        return result


    # Creates a table of requested flags type.
    @env.macro
    def flags_source(source:str, type:str):
        result = ""

        # Let's read the csv file
        with open('data/flags.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Analyze the source
                if (row['source'] == source):
                    # We are in a new "source" so we have to put the header

                    if (row['type'] == type) or (type == "WORLD_DEFAULT_PROTECTION" and row['type'] == "PROTECTION"):
                        if (type == "PROTECTION"):
                            result += f"""\n## {source} {type.replace("_", " ").capitalize()} flags

| | Flag ID | Flag | Description | Default | Min Rank | Max Rank |
| - | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
"""

                            result += f"| <span class='icon-minecraft {icon_css(row['icon'])}'></span> | {row['flag']} | {row['name']} | {row['description']} | {row['default']} | {row['min']} | {row['max']} |\n"
                        else:
                            result += f"""\n## {source} {type.replace("_", " ").capitalize()} flags

| | Flag ID | Flag | Description | Default |
| - | ---------- | ---------- | ---------- | ---------- |
"""
                            result += f"| <span class='icon-minecraft {icon_css(row['icon'])}'></span> | {row['flag']} | {row['name']} | {row['description']} | {row['default']} |\n"

        return result

    # Creates a table of requested flags type.
    @env.macro
    def icon_css(icon:str):
        with open("data/minecraft-block-and-entity.json", 'r') as j:
            contents = json.loads(j.read())

            for entry in contents:
                if icon.lower() == entry['name']:
                    return entry['css']

        return ""
