## 可用语言

{{ translations("BentoBox") }}

## MiniMessage 格式

BentoBox 对所有语言字符串使用 [MiniMessage](https://docs.advntr.dev/minimessage/format.html) 格式。这意味着你可以在翻译中使用 MiniMessage 标签来应用富文本格式。例如：

```yaml
my-message: "<green>欢迎来到岛屿！</green>"
my-message: "<bold><red>警告！</red></bold> 发生了一些事情。"
my-message: "<gradient:gold:yellow>岛屿名称</gradient>"
```

旧版的 `§` 或 `&` 颜色代码仍向后兼容，加载时会自动转换为 MiniMessage 格式。

## 消息传递标签

语言字符串可以通过特殊的内联标签控制消息的传递方式。当没有传递标签时，消息将以聊天形式发送（默认行为）。

### `[actionbar]`

将消息作为**动作栏**消息发送（显示在快捷栏上方的文字）。

```yaml
island-go: "[actionbar]正在传送..."
```

### `[title]` 和 `[subtitle]`

将消息作为屏幕上的**标题**叠加层发送。`[title]` 显示大标题文字，`[subtitle]` 显示其下方的小字。`[subtitle]` 不是独立的传递类型——它只能作为 `[title]` 消息中的分隔符使用。没有 `[title]` 时，它会回退到聊天传递方式。

```yaml
# 带副标题的标题
island-go: "[title]正在传送...[subtitle]请稍等。"
# 仅副标题（空标题，文字作为副标题）
scooping: "[title][subtitle]你舀走了岩浆！"
```

### `[sound:name:volume:pitch]`

为玩家播放**音效**。音量和音调是可选的（默认 `1.0`）。使用 Bukkit/Minecraft 音效列表中以下划线分隔的音效名称（如 `entity_experience_orb_pickup`）。音效标签可与任何传递类型标签组合使用。

```yaml
island-go: "[sound:entity_experience_orb_pickup:1:1][title]正在传送...[subtitle]请稍等。"
```

!!! note
    非玩家发送者（如控制台）在使用动作栏或标题标签时将回退到聊天输出。

## 翻译指南

* 我们现在提供了一个翻译工具，地址为 [https://download.bentobox.world/translate.html](https://download.bentobox.world/translate.html)。该工具在你的浏览器中本地运行，可能对翻译有所帮助。请将新文件以 PR 形式提交到 GitHub。
* 翻译者将获得特殊徽章！
* 不要翻译方括号内的文字，因为那些是占位符，例如 [name] 应保持英文
* 测试你的翻译——在提交前尽量检查所有内容
* 翻译中不得包含任何广告、脏话或贬义内容。我们在接受 PR 前会进行审核。
* 欢迎在 Discord 上提问有关翻译的问题。

## 游戏模式

- [AcidIsland](../gamemodes/AcidIsland/index.md#翻译)
- [AOneBlock](../gamemodes/AOneBlock/index.md#翻译)
- [Boxed](../gamemodes/Boxed/index.md#翻译)
- [BSkyBlock](../gamemodes/BSkyBlock/index.md#翻译)
- [CaveBlock](../gamemodes/CaveBlock/index.md#翻译)
- [Poseidon](../gamemodes/Poseidon/index.md#翻译)
- [SkyGrid](../gamemodes/SkyGrid/index.md#翻译)
- [Stranger Realms](../gamemodes/StrangerRealms/index.md#翻译)

## 插件

- [Bank](../addons/Bank/index.md#翻译)
- [Biomes](../addons/Biomes/index.md#翻译)
- [Border](../addons/Border/index.md#翻译)
- [CauldronWitchery](../addons/CauldronWitchery/index.md#翻译)
- [Challenges](../addons/Challenges/index.md#翻译)
- [Chat](../addons/Chat/index.md#翻译)
- [CheckMeOut](../addons/CheckMeOut/index.md#翻译)
- [ControlPanel](../addons/ControlPanel/index.md#翻译)
- [DimensionalTrees](../addons/DimensionalTrees/index.md#翻译)
- [ExtraMobs](../addons/ExtraMobs/index.md#翻译)
- [FarmersDance](../addons/FarmersDance/index.md#翻译)
- [Greenhouses](../addons/Greenhouses/index.md#翻译)
- [InvSwitcher](../addons/InvSwitcher/index.md#翻译)
- [IslandFly](../addons/IslandFly/index.md#翻译)
- [Level](../addons/Level/index.md#翻译)
- [Likes](../addons/Likes/index.md#翻译)
- [Limits](../addons/Limits/index.md#翻译)
- [MagicCobblestoneGenerator](../addons/MagicCobblestoneGenerator/index.md#翻译)
- [TopBlock](../addons/TopBlock/index.md#翻译)
- [TwerkingForTrees](../addons/TwerkingForTrees/index.md#翻译)
- [Upgrades](../addons/Upgrades/index.md#翻译)
- [Visit](../addons/Visit/index.md#翻译)
- [VoidPortals](../addons/VoidPortals/index.md#翻译)
- [Warps](../addons/Warps/index.md#翻译)
