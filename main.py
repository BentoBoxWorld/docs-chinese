import csv
import json

def define_env(env):

    languages = [
        {"id": "zh-CN", "name": "中文（中国）"},
        {"id": "zh-HK", "name": "中文（香港）"},
        {"id": "zh-TW", "name": "中文（台湾）"},
        {"id": "hr", "name": "克罗地亚语"},
        {"id": "cs", "name": "捷克语"},
        {"id": "fr", "name": "法语"},
        {"id": "de", "name": "德语"},
        {"id": "hu", "name": "匈牙利语"},
        {"id": "id", "name": "印尼语"},
        {"id": "it", "name": "意大利语"},
        {"id": "ja", "name": "日语"},
        {"id": "ko", "name": "韩语"},
        {"id": "lv", "name": "拉脱维亚语"},
        {"id": "pl", "name": "波兰语"},
        {"id": "pt", "name": "葡萄牙语"},
        {"id": "ro", "name": "罗马尼亚语"},
        {"id": "ru", "name": "俄语"},
        {"id": "es", "name": "西班牙语"},
        {"id": "tr", "name": "土耳其语"},
        {"id": "vi", "name": "越南语"},
        {"id": "uk", "name": "乌克兰语"},
        {"id": "nl", "name": "荷兰语"}
    ]

    @env.macro
    def translations(gitlocalize_id:int, available_translations:list):
        yes = "✅"
        no = "❌"

        # We are adding the intro + header of the language table
        result = f"""!!! note "我们需要你的帮助！"
    BentoBox 及其附加组件中的绝大多数字符串几乎可以翻译成任何语言。
    然而，BentoBox 或上述附加组件提供的大部分翻译都是由社区完成的，我们在很大程度上依赖社区。
    我们无法审查这些翻译的所有内容，也无法保证其质量，因此我们非常感谢任何贡献。

    * 如果这个附加组件没有提供你的语言，或者你想改进现有的翻译，请阅读[翻译指南](../../BentoBox/Translate-BentoBox-and-addons)并[开始翻译](https://gitlocalize.com/repo/{gitlocalize_id})！
    * 如果下面没有列出你的语言，请在 [Discord](https://discord.bentobox.world) 上联系我们，我们会安排一切，以便你可以开始翻译！

| Available | Language | Language code | Progress |
| --- | ---------- | --- | ----------- |
| ✅ | English (United States) | `en-US` | 100% (Default) |
"""

        for language in languages:
            available = no
            if language["id"] in available_translations:
                available = yes
            link = f"https://gitlocalize.com/repo/{gitlocalize_id}/{language['id']}/src/main/resources/locales"
            badge = f"https://gitlocalize.com/repo/{gitlocalize_id}/{language['id']}/badge.svg"
            result += f"| {available} | [{language['name']}]({link}) | `{language['id']}` | ![progress]({badge}) |\n"

        return result

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
