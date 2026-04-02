# 多语言支持

BentoBox 及其插件开箱即用地支持各种语言。所有游戏内消息、GUI 文本和玩家看到的物品名称都可以用他们自己的语言显示 — 无需额外插件。

## 支持的语言

BentoBox 目前提供以下语言的翻译：

| 语言 | 代码 |
|---|---|
| 英语（默认） | `en-US` |
| 简体中文 | `zh-CN` |
| 繁体中文（香港） | `zh-HK` |
| 繁体中文（台湾） | `zh-TW` |
| 克罗地亚语 | `hr` |
| 捷克语 | `cs` |
| 荷兰语 | `nl` |
| 法语 | `fr` |
| 德语 | `de` |
| 匈牙利语 | `hu` |
| 印度尼西亚语 | `id` |
| 意大利语 | `it` |
| 日语 | `ja` |
| 韩语 | `ko` |
| 拉脱维亚语 | `lv` |
| 波兰语 | `pl` |
| 葡萄牙语 | `pt` |
| 罗马尼亚语 | `ro` |
| 俄语 | `ru` |
| 西班牙语 | `es` |
| 土耳其语 | `tr` |
| 乌克兰语 | `uk` |
| 越南语 | `vi` |

单个插件可能支持不同的语言子集。请查看每个插件的页面以获取其特定的翻译状态。

## 设置默认语言

要设置所有玩家默认看到的语言，请编辑 BentoBox 的 `config.yml`：

```yaml
# Default language for new players.
# Refer to the /locale folder in the BentoBox plugin folder for available languages.
default-language: en-US
```

将其设置为上表中的任何语言代码。更改后，重新加载服务器或运行 `/bentobox reload`。

## 玩家语言选择

如果启用，玩家可以使用以下方式切换到他们首选的语言：
```
/bentobox locale
```

这在国际服务器上很有用，玩家基数讲多种语言。

## 翻译是社区贡献的

BentoBox 及其插件的翻译由社区贡献。BentoBox 团队无法深入审查每个翻译，但在接受前会检查所有贡献的质量。

!!! note "翻译质量"
    因为翻译是社区贡献的，质量各不相同。如果你发现翻译中的错误，请帮助改进它！

## 如何贡献翻译

如果你的语言尚不可用，或现有翻译需要改进：

1. 访问 [GitLocalize](https://gitlocalize.com/repo/2855) 上 BentoBox 或特定插件的翻译页面。
2. 选择你的语言（或在我们的 [Discord](https://discord.bentobox.world) 上请求新语言）。
3. 翻译字符串 — **不要**翻译方括号内的文本，例如 `[name]` 应该保持原样。
4. 提交你的工作。翻译者获得特殊社区徽章！

翻译辅助工具可在 [download.bentobox.world/translate.html](https://download.bentobox.world/translate.html) — 完全在浏览器中运行。

请参阅插件翻译页面的完整列表，见[翻译 BentoBox 和插件](../Translate-BentoBox-and-addons.md)。
