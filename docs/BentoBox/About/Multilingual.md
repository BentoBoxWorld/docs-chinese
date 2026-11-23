# 语言和消息 { #languages-messages }

BentoBox 及其附属中的每条消息、菜单和物品名称都来自**区域文件**：每种语言一个 YAML 文件。玩家选择自己的语言，你可以改变任何文本、颜色或消息的显示方式（聊天、动作栏、标题、声音）。

## 语言 { #languages }

BentoBox 附带 25 种语言：

| 语言 | 文件 | 语言 | 文件 |
|---|---|---|---|
| 英语（默认） | `en-US` | 意大利语 | `it` |
| 简体中文 | `zh-CN` | 日语 | `ja` |
| 繁体中文（香港） | `zh-HK` | 韩语 | `ko` |
| 繁体中文（台湾） | `zh-TW` | 拉脱维亚语 | `lv` |
| 克罗地亚语 | `hr` | 波兰语 | `pl` |
| 捷克语 | `cs` | 葡萄牙语 | `pt` |
| 荷兰语 | `nl` | 巴西葡萄牙语 | `pt-BR` |
| 法语 | `fr` | 罗马尼亚语 | `ro` |
| 德语 | `de` | 俄语 | `ru` |
| 匈牙利语 | `hu` | 西班牙语 | `es` |
| 印度尼西亚语 | `id` | 土耳其语 | `tr` |
| | | 乌克兰语 | `uk` |
| | | 越南语 | `vi` |

附属可能有较少的语言。每个[游戏模式](../../gamemodes/Comparison.md)和[附属](Addons.md)页面都有一个表格显示每种语言的完整程度。

### 服务器的默认语言 { #the-servers-default-language }

新玩家看到默认语言，直到他们选择一个。在 BentoBox 的 `config.yml` 中设置它，使用表中的文件名：

```yaml
general:
  default-language: en-US
```

然后重启或运行 `/bentobox reload`。BentoBox 不会自动检测玩家的 Minecraft 语言。

### 玩家选择语言 { #players-choosing-a-language }

玩家使用**`/island language`**（或游戏模式的自己的命令）更改语言，这打开已安装语言的菜单。他们的选择适用于 BentoBox 和所有附属，在每个游戏模式中。

如果玩家语言中缺少消息，BentoBox 使用服务器的默认语言，然后使用英语。

## 改变消息 { #changing-messages }

区域文件位于：

| 文本来自 | 文件夹 |
|---|---|
| BentoBox | `plugins/BentoBox/locales/BentoBox/` |
| 游戏模式或附属 | `plugins/BentoBox/locales/<AddonName>/`，例如 `locales/BSkyBlock/` |

要改变消息：

1. 找到它：在语言文件中搜索（例如 `en-US.yml`）玩家看到的文本。
2. 改变键后的文本，保持键和缩进。留下方括号中的任何东西，如 `[name]`、`[number]` 或 `[prefix_island]`；这些由 BentoBox 填入。（`[prefix_island]` 变成游戏模式的岛屿词，例如"岛屿"、"洞穴"或"方块"。）
3. 运行 `/bentobox reload locales`。

```yaml
commands:
  island:
    create:
      creating-island: "<green>正在构建你的 [prefix_island]，稍等...</green>"
```

改变你的玩家使用的每种语言，否则其他语言仍会显示旧文本。

**你的改变在更新时保留。** 当 BentoBox 或附属更新时，新消息被添加到服务器上的文件，但已有的消息不会被覆盖。这也意味着如果更新改进了消息的措辞，你在删除该行（或整个文件）并重新加载之前不会看到它。

**要隐藏消息**，将其设置为空字符串：`creating-island: ""`。空消息不会被发送。

**要检查缺失的翻译**，运行 `/bentobox locale`。它比较每种语言文件，对于 BentoBox 和每个附属，与英语并报告缺失的内容。

## 颜色和格式 { #colours-and-formatting }

消息使用 [MiniMessage](https://docs.advntr.dev/minimessage/format.html) 标签：

```yaml
example: "<green>欢迎来到岛屿！</green>"
example: "<bold><red>警告！</red></bold> 发生了一些事情。"
example: "<gradient:gold:yellow>岛屿名称</gradient>"
```

旧式颜色代码（`&a`、`&l`、`§c`）仍然有效。

## 消息的显示方式 { #how-a-message-is-shown }

默认情况下消息去聊天。用标签在其他地方显示它：

| 标签 | 显示消息 |
|---|---|
| `[actionbar]` | 在快捷栏上方 |
| `[title]` | 作为屏幕中间的大标题。添加 `[subtitle]` 在更小的行下面放置文本 |
| `[sound:name:volume:pitch]` | 播放声音。音量和音调是可选的。使用 Minecraft 声音名称下划线分隔，例如 `entity_experience_orb_pickup` |

```yaml
example: "[actionbar]正在传送..."
example: "[title]正在传送...[subtitle]等一秒。"
example: "[sound:entity_experience_orb_pickup:1:1][title]正在传送...[subtitle]等一秒。"
```

发给控制台的消息总是进入控制台日志。

### 可点击的消息 { #clickable-messages }

在消息中的任何地方添加这些以使整条消息可点击或在悬停时显示文本：

| 标签 | 效果 |
|---|---|
| `[run_command: /command]` | 单击运行命令 |
| `[suggest_command: /command]` | 单击将命令放在聊天框中 |
| `[open_url: https://...]` | 单击打开链接 |
| `[copy_to_clipboard: text]` | 单击复制文本 |
| `[hover: text]` | 玩家悬停消息时显示文本 |

```yaml
example: "你不在你的岛屿上。单击回家！[run_command: /island go][hover: 传送回家]"
```

## 菜单文本 { #menu-text }

菜单标题和按钮文本也在区域文件中，从菜单模板引用。请参阅[自定义菜单](../../Tutorials/generic/Customizable-GUI.md#change-the-title-or-button-text)。

## 修复或添加翻译 { #fixing-or-adding-translations }

翻译由 AI 帮助完成并由社区更正。如果你发现错误，在项目的 GitHub 存储库中的区域文件中修复它并打开拉取请求，或在 [Discord](https://discord.bentobox.world) 上告诉我们。请参阅[翻译 BentoBox](../Translate-BentoBox-and-addons.md)了解指南和每个项目的翻译状态。

## 故障排除 { #troubleshooting }

**我的改变没有显示。**
运行 `/bentobox reload locales`。检查你编辑了玩家的语言（他们可能没有使用英语）和正确的文件夹（BentoBox 的自己的消息在 `locales/BentoBox/` 中，游戏模式消息在 `locales/<GameMode>/` 中）。

**服务器显示 `commands.island...` 代替消息。**
键在玩家的语言、服务器的默认语言和英语中缺失。删除文件，使 BentoBox 写一个新副本，或添加键回去。

**更新后，消息仍有旧措辞。**
你的文件保留旧文本。删除该行或整个文件并运行 `/bentobox reload locales`。

**保护标志工具提示中所有等级都是同一种颜色，或者标志没有“左键点击 / 右键点击”提示。**
这些区域文件最初由旧版 BentoBox 生成，里面仍是旧文本。BentoBox 3.23.7 起，即使使用旧文件也能再次正确显示等级颜色，但只有新生成的文件才包含点击提示以及之后的所有措辞修正。刷新方法：停止服务器，将 `plugins/BentoBox/locales/BentoBox/` 重命名（例如改为 `BentoBox-old`），启动服务器以写出当前版本的文件，然后把你自己的修改再复制回去。附属的文件夹 `plugins/BentoBox/locales/<AddonName>/` 也可以用同样的方法处理。

**编辑后 YAML 文件不会加载。**
通常是缺少引号或错误的缩进。将包含 `:` 或 `#` 的消息放在引号中，并检查控制台以获取行号。
