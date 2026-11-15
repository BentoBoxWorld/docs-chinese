# 初始岛屿（蓝图） { #starter-islands-blueprints }

当玩家创建岛屿时，BentoBox 为他们粘贴一个初始岛屿。这些初始岛屿是**蓝图**，你在游戏中建造和保存。一个**包**将一个主世界、地狱和末地蓝图分组为创建岛屿菜单中的一个选择，有自己的图标、名称和描述。

每个游戏模式都带有一些包。你可以改变他们，添加你自己的，提供仅限 VIP 的岛屿，为它们收费，并在选择一个时运行命令。

!!! info "这个页面中的命令"
    命令以 BSkyBlock（`/bsbadmin`）显示。改用你的游戏模式的管理员命令，例如 AOneBlock 的 `/oba` 或 AcidIsland 的 `/acid`。`blueprint` 可以缩短为 `bp`。

## 制作初始岛屿 { #make-a-starter-island }

1. **建造它。** 在游戏模式的世界中建造岛屿，远离其他岛屿。在其中放置至少一个**基岩**方块：最高的基岩方块变成岛屿的中心，BentoBox 不会在没有一个的情况下保存蓝图。
2. **添加标志（可选）。** 放置一个标志，第一行写 `[spawn_here]`，位置是玩家应该出现的地方，面向他们应该看的方向。添加一个标志，第一行写 `[start]` 用于欢迎消息。参见[标志](#signs)。
3. **选择它。** 站在一个角落并运行 `/bsbadmin bp pos1`，然后在相对的角落运行 `/bsbadmin bp pos2`。使用这些，不是 WorldEdit 的选择。
4. **复制它。** `/bsbadmin bp copy`。如果岛屿将被粘贴到水或石头中（AcidIsland、CaveBlock、Poseidon），添加 `air`，所以周围的空气也被粘贴。添加 `biome` 来保留生物群系，或 `nowater` 来排除水方块。
5. **检查它。** 去某个空地方并运行 `/bsbadmin bp paste` 来查看你复制的内容。
6. **保存它。** `/bsbadmin bp save <name>`，例如 `/bsbadmin bp save vip_island`。
7. **提供给玩家。** 打开 `/bsbadmin bp` 并将蓝图放入包（下一部分）。

要替换游戏模式的默认岛屿而不是添加新岛屿，保存在其蓝图上（通常是 `island`、`nether-island` 和 `end-island`）。你会被要求确认。

!!! tip "保持较小"
    岛屿游戏模式的乐趣是从很少的东西成长。用刚好足够的方块和物品开始玩家。

**转换 WorldEdit 示意图：** 蓝图不是示意图，但你可以用 WorldEdit 粘贴示意图，添加基岩和标志，然后用上面的蓝图命令选择、复制和保存它。也为每个地狱和末地岛屿做这个。

## 包：创建岛屿菜单中的选择 { #bundles-the-choices-in-the-create-island-menu }

用 **`/bsbadmin bp`** 打开蓝图管理器。它列出包；点击一个来编辑它。

| 做… | 做这个 |
|---|---|
| 创建包 | 点击绿色横幅，然后在聊天中输入名称 |
| 将蓝图放入包 | 点击底部的蓝图使其发光，然后点击绿色（主世界）、红色（地狱）或黄色（末地）槽 |
| 清空槽 | 右键点击它 |
| 改变包的图标 | 在你自己的物品栏中点击物品 |
| 重命名它 | 右键点击主列表中的包，然后在聊天中输入名称 |
| 改变描述 | 在包内，点击其图标（左上角），然后在聊天中输入。颜色代码如 `&c` 有效 |
| 选择它在菜单中显示的位置 | 左键点击槽图标来后移它，右键点击来前移它 |
| 使其仅限 VIP | 点击绘画来需要权限。权限显示在图标上，例如 `bskyblock.island.create.vip_island` |
| 为它收费 | 点击金锭：左/右键点击添加/移除 1，shift 点击 100。需要 Vault 和经济插件 |
| 选择时运行命令 | 点击命令块并在聊天中输入命令 |
| 限制玩家可以选择它的次数 | 点击时钟。仅在玩家可以拥有多个岛屿时显示 |
| 删除它 | 右键点击 TNT |

每个游戏模式都有一个叫 `default` 的包，无法删除。当玩家没有选择时使用它（例如当岛屿在首次登入时自动创建时）。

包**必须**有一个主世界蓝图；如果没有，使用默认岛屿并记录错误。地狱和末地蓝图是可选的；没有他们，在那些世界中没有任何东西被粘贴。

**在管理器中或用 `/bsbadmin bp rename` 重命名包和蓝图**，不是通过重命名文件。

### 选择包时运行的命令 { #commands-when-a-bundle-is-chosen }

每次用包创建岛屿时运行命令，例如给启动工具包或设置等级。`[player]` 和 `[owner]` 被替换为玩家的名称。命令从控制台运行，除非他们以 `[SUDO]` 开头，这以玩家身份运行它们：

```
lp user [player] parent add skyblock-starter
[SUDO] kit starter
```

### 为包收费 { #charging-for-a-bundle }

用金锭在包上设置成本。玩家在用它创建或重置岛屿时支付，如果他们买不起无法选择它。这需要 BentoBox 的 `config.yml` 中的 `use-economy: true` 和带经济插件的 Vault；没有他们金锭不显示。

## 标志 { #signs }

| 标志的第一行 | 发生什么 |
|---|---|
| `[spawn_here]` | 玩家在这个位置出现，面向标志面向的方向。标志被移除。也在地狱和末地蓝图中工作 |
| `[start]` | 替换为游戏模式的地区文件中的欢迎文本（`bskyblock.sign.line0` 到 `line3`），以所有者的语言。该文本中的 `[name]` 变成所有者的名称 |
| 其他任何东西 | 按照编写被粘贴 |

**命名生物：** 在铁砧中重命名名签以包括 `[name]` 并在复制前将其放在你岛屿中的生物上。当岛屿被粘贴时，生物以岛屿所有者的名称命名。

## 所有蓝图命令 { #all-blueprint-commands }

| 命令 | 作用 |
|---|---|
| `/bsbadmin bp` | 打开蓝图管理器 |
| `/bsbadmin bp pos1`、`pos2` | 设置要复制的区域的角落 |
| `/bsbadmin bp copy [air] [biome] [nowater]` | 复制区域到你的剪贴板 |
| `/bsbadmin bp origin` | 设置粘贴原点到你看着的方块 |
| `/bsbadmin bp paste` | 粘贴你的剪贴板到你站的地方 |
| `/bsbadmin bp save <name>` | 将你的剪贴板保存为蓝图 |
| `/bsbadmin bp load <name>` | 加载蓝图到你的剪贴板来改变它 |
| `/bsbadmin bp list` | 列出蓝图 |
| `/bsbadmin bp rename <name> <new name>` | 重命名蓝图 |
| `/bsbadmin bp delete <name>` | 删除蓝图 |
| `/bsbadmin bp sink` | 切换这个蓝图粘贴时是否沉到海底 |

## 文件 { #the-files }

蓝图和包按游戏模式存储在 `plugins/BentoBox/addons/<GameMode>/blueprints/` 中：

- `<name>.blueprint`：蓝图，作为纯 JSON。较旧的 `.blu` 文件（压缩）仍会加载。
- `<bundle>.json`：包，作为纯 JSON。

你可以在服务器之间复制这些文件、保留在版本控制中或编辑它们。对于每个字段，参见[蓝图文件格式](Blueprint-Format.md)。

## 粘贴速度 { #pasting-speed }

复制和粘贴一点点地发生，所以大岛屿不会冻结服务器；一个大岛屿可能需要几秒钟。如果岛屿创建导致延迟，降低 BentoBox 的 `config.yml` 中的 `paste-speed`（每 tick 的方块数）。

## 故障排除 { #troubleshooting }

**"蓝图中必须至少有一个基岩方块！"**
向岛屿添加基岩方块，重新复制，然后保存。

**玩家出现在错误的位置，或掉落。**
添加 `[spawn_here]` 标志，在其上方有空气供玩家使用。

**岛屿周围被不应该在那里的水（或石头）间隙包围**，或来自世界的水流入其中。
用 `air` 复制所以岛屿周围的空间是蓝图的一部分。保持选择紧凑，因为空气使文件更大。

**我的新包不显示在创建岛屿菜单中。**
检查它有一个主世界蓝图，它不需要玩家缺少的权限，并且，如果它有使用限制，玩家没有用完它。使用 BentoBox 的 `config.yml` 中的 `hide-used-blueprints: true`，用完的包被隐藏。

**欢迎标志显示 `[start]`。**
`[start]` 文本来自游戏模式的地区文件。检查 `<gamemode>.sign.line0` 到 `line3` 在其中存在。

## 另请参见 { #see-also }

- [岛屿](About/IslandManagement.md)：创建、重置和调整岛屿大小
- [更大的创建岛屿菜单](../Tutorials/generic/Bigger-Create-Island-Menu.md)和[自定义菜单](../Tutorials/generic/Customizable-GUI.md)：玩家选择的菜单
- [蓝图文件格式](Blueprint-Format.md)：用于编辑文件
