# 管理工具

BentoBox 为服务器管理员提供了一系列工具来管理游戏、调查问题并保持一切顺利运行 — 无需手动编辑文件。

## 管理面板

主要管理中心是**管理面板**，通过以下方式打开：
```
/bentobox manage
```
（或其别名 `/bbox manage`）

从这里你可以一目了然地查看所有运行的游戏模式、活跃岛屿和基本服务器健康状况。

## `/bentobox` 命令

所有顶级 BentoBox 管理都通过 `/bentobox`（别名 `/bbox`）进行：

| 命令 | 作用 |
|---|---|
| `/bentobox version` | 显示 BentoBox 版本和所有已加载的插件。**报告 bug 时始终包括此内容。** |
| `/bentobox manage` | 打开管理面板 GUI |
| `/bentobox reload` | 重新加载 BentoBox 配置文件和地区，无需完全服务器重启 |
| `/bentobox catalog` | 打开插件目录 |
| `/bentobox perms` | 显示 BentoBox 和所有插件的有效权限 |
| `/bentobox rank` | 列出、添加或移除自定义等级 |

## 每个游戏模式的管理员命令

每个游戏模式都有自己的管理员命令。对于 BSkyBlock 是 `/bsb`，对于 AcidIsland 是 `/acid admin` 等。这些为你提供特定于该游戏模式的控制：

| 命令 | 作用 |
|---|---|
| `/[admin] info <player>` | 显示玩家的岛屿的完整详细信息 |
| `/[admin] delete <player>` | 删除玩家的岛屿 |
| `/[admin] delete` | *(3.19.0)* 不带玩家参数时，在确认后软删除你**当前所站**的岛屿（如果该岛屿仍有队伍则会被拒绝） |
| `/[admin] undelete` | *(3.19.0)* 在区域文件被清除之前，清除你**当前所站**岛屿的待删除状态，使其变为无主 |
| `/[admin] register <player>` | 将无主岛屿注册给玩家。对于待删除的岛屿，现在会显示确认提示并取消删除，而不是拒绝操作 |
| `/[admin] setrange <player> <range>` | 更改玩家的岛屿保护范围 |
| `/[admin] range removebonus <player> [id]` | 从单个岛屿移除所有奖励保护范围，或仅移除给定 id 的范围 |
| `/[admin] range purgebonus <id>` | 从世界中的**每个**岛屿移除奖励范围 id — 理想情况下在卸载提供奖励范围的附属之后。扫描以异步运行，不会冻结大型服务器 |
| `/[admin] settings` | 打开管理员的世界设置面板 |
| `/[admin] settings <player>` | 打开特定玩家的岛屿设置面板 |
| `/[admin] why <player>` | 开始跟踪为什么玩家可以或不可以做某事（见下文） |
| `/[admin] reload` | 重新加载游戏模式的配置 |
| `/[admin] blueprint` | 打开蓝图管理器 GUI |

确切的管理员命令前缀取决于游戏模式的配置。请查看游戏模式的文档以获取其特定命令。

## "Why" 诊断工具

最有用的管理员工具之一是 `why` 命令。如果玩家报告他们在岛屿上不能做某事（或他们*可以*做他们不应该做的事情），运行：

```
/[admin_command] why <player>
```

之后，服务器控制台将记录该玩家采取的每个操作的原因 — 是否被允许或被阻止，以及哪个保护标志导致了它。这使得无需猜测即可轻松诊断配置错误的权限。

要停止跟踪，再次运行该命令。

## 管理员设置面板

管理员设置面板（使用 `/[admin] settings` 打开）控制全球范围的默认值 — 适用于游戏模式世界中任何地方的设置，而不仅仅是一个岛屿。这包括：

- 新岛屿的默认保护标志
- 全球范围的限制（例如爬行者爆炸伤害、活塞行为）
- 玩家设置面板的可见性设置（隐藏你不想让玩家改变的标志）

有关标志系统的完整说明，请参阅[保护](Protections.md)。

## 基于权限的控制

BentoBox 在很大程度上基于权限。几乎所有内容 — 从玩家可以拥有多少个家园，到他们是否可以飞行，再到他们的岛屿的大小 — 都可以通过通过你的权限插件（例如 LuckPerms）给予或扣除权限来控制。

!!! tip
    在控制台中运行 `/bentobox perms` 以查看 BentoBox 及其插件注册的所有权限的列表，采用 YAML 格式。这对于配置你的权限插件很有用。

## 数据库管理

BentoBox 支持多个数据库后端来存储岛屿和玩家数据：

- **JSON（平面文件）** — 默认值；易于设置，无需额外软件
- **MySQL** (5.7+)
- **MariaDB** (10.2.3+)
- **MongoDB** (3.6+)
- **SQLite** (3.28+)
- **PostgreSQL**

数据库类型在 BentoBox 的 `config.yml` 中设置。要在不丢失数据的情况下从一个数据库类型迁移到另一个数据库类型，请使用：
```
/bentobox migrate
```

!!! warning
    迁移数据库前始终进行完整备份。

## 不重启即重新加载

更改配置文件后，你可以在不完全重启服务器的情况下应用它：
```
/bentobox reload
```
这将重新加载 BentoBox 和所有插件，包括地区。请注意，某些更改（如世界生成设置）始终需要完全重启才能生效。

## 更新日志

!!! note "v3.21.0 新内容 — 模态对话框"
    **发布于：** 2026-07-22

    一个提升玩家体验的版本。兼容性：Paper Minecraft 1.21.5 – 26.2，Java 25+。

    - ⚙️ 🔡 **为高摩擦流程引入模态对话框。** 敏感命令的确认、`/island go` 的目的地选择器、队伍邀请，以及首次加入时的游戏模式选择器，现在都可以显示为真正的模态对话框——玩家不会看错，也无法一划而过。`config.yml` 中新增的 `island.dialogs` 小节为每个流程提供一个开关：`confirmations`、`go-picker` 和 `team-invites` **默认开启**，`game-mode-selection` **默认关闭**，因为它天生就具有打断性。对话框需要 Minecraft 26+ 的服务端；在更旧的版本上，所有开关都会被忽略并沿用经典的聊天/命令行为，因此无需做任何处理。
    - **更宽容的 `/island go` 匹配。** `/island go myisland`、`hom`，以及大小写不对或中间多打了一个空格的名称，现在都会把玩家传送到他想去的地方，而不是因为精确匹配失败而抛出完整的目的地清单。参见[家园位置](IslandManagement.md#home-locations)。
    - 🔡 **本地化说明：** 全部 22 个内置本地化文件都新增了对话框相关的键（`general.dialogs.*`，以及确认命令、`island go` 和队伍邀请命令下的对话框与选择器键）。请重新生成或更新任何自定义本地化文件。
    - 🔧 **插件开发者**可以使用与核心相同的 `world.bentobox.bentobox.api.dialogs` API——参见[模态对话框](../Developer-Documentation.md#modal-dialogs)。

    [发布 v3.21.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.21.0)

??? note "v3.20.0 新内容 — 命令建议与核心结构抑制"
    **发布于：** 2026-07-11

    一个提升使用体验的版本。兼容性：Paper Minecraft 1.21.5 – 26.2，Java 25+。除非你主动启用，否则升级后行为不变。

    - 🔡 ⚙️ **"你是不是想输入"命令建议。** 输错的命令（如 `/teams` 或 `/island invit Floris`）现在会给出最接近的 BentoBox 命令——可点击，或在 30 秒内输入 `yes`/`y` 接受——而不再直接抛出帮助文本。建议会匹配所有命令树中的标签和别名，按权限过滤，并根据玩家所在的游戏模式世界来消除歧义。`config.yml` 中 `general.did-you-mean` 下新增两个开关 `unknown-commands` 和 `subcommands`，两者都**默认开启**；将任一项设为 `false` 并执行 `/bbox reload` 即可禁用。
    - ⚙️ 🔺 **面向所有游戏模式的核心原版结构抑制。** 禁用某个原版结构现在是一项核心设置，不再需要逐个附属去处理。`config.yml` 中新增的 `world.disabled-structures` 列表（应用于每个 BentoBox 主世界/下界/末地）会阻止所列结构生成，**并**在结构搜索中跳过它们——`/locate`、末影之眼、探险家/藏宝图、海豚以及村民制图师交易——从而修复长期存在的 `/locate` 主线程冻结问题和出生点附近的结构泄漏。键名对大小写和分隔符不敏感（`trial_chambers`、`ancient-city`）。游戏模式可以逐结构覆盖该列表。**该列表默认为空，因此在你主动启用之前行为不变。**
    - 🔌 **Nexo 钩子。** BentoBox 现在可以放置和检测 [Nexo](https://nexomc.com/) 自定义方块和物品，与其他自定义物品集成并列。
    - 🔌 **Oraxen 方块放置。** `OraxenHook.placeBlock` 向附属公开 Oraxen 自定义方块放置能力，与其他自定义方块钩子相匹配。
    - 🔡 **本地化说明：** 所有 22 个内置本地化文件都新增了三个 `general.did-you-mean` 键，且在每个非英文文件中补全了此前缺失的键 `commands.admin.team.setowner.specify-island`。请重新生成或更新任何自定义本地化文件。

    [发布 v3.20.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.20.0)

??? warning "v3.19.0 新内容 — 现在会遵循床/重生锚的重生点"
    **发布于：** 2026-07-08

    兼容性：Paper Minecraft 1.21.5 – 26.2，Java 25+。

    - 🔡 **新增 `FISHING` 保护标志。** 阻止玩家从岛屿外向受保护区域内钓鱼（该标志检查鱼钩的位置）。默认为访客等级，因此在你提高它之前不会有任何变化。
    - 🔺 **现在会遵循床和重生锚的重生点。** 当床或已充能的重生锚位于你作为成员的岛屿上时，在岛屿上死亡现在会将你重生到那里。由新的 `BED_ANCHOR_RESPAWN` 世界设置控制（**默认启用**）；希望保留旧的"始终在岛屿家园重生"行为的经济敏感型服务器应将其禁用。
    - 🐛 **末地出口传送门不再把你丢到世界出生点。** 在多游戏模式服务器上，跳入末地出口传送门现在会将你送往安全的岛屿家园。
    - 🐛 **物品展示框和画在蓝图中得以保留。** 展示框保持其朝向和内容，画恢复其图案，而不是脱落或朝向错误的方向。
    - 🔡 **恢复待删除的岛屿。** 新增 `/[admin] undelete`、站立式 `/[admin] delete`（不带玩家参数）以及 `/[admin] register` 上的确认提示，现在可以在区域文件被清除之前拯救软删除的岛屿（见上面的"每个游戏模式的管理员命令"表）。
    - ⚙️ **BlueMap 岛屿图层在重载后得以保留。** 拥有者标记和区域框在 `/bluemap reload` 后不再消失。`config.yml` 中新增的 `bluemap` 部分添加了 `island-markers` 和 `island-areas` 开关（两者都默认为 `true`），与 Dynmap 开关相对应，还包括标记自定义。
    - ⚙️ **可配置的队伍面板按钮图标 + 成员/候选人文本。** 队伍面板中的 STATUS、RANK 过滤和 INVITE 按钮现在遵循 `team_panel.yml` 中设置的 `icon:`，成员/候选人按钮的名称和描述现在由本地化键驱动。默认值完全重现之前的外观。
    - ⚡ **设置 GUI 的连击不再导致 MSPT 飙升。** 通过原地刷新面板和翻译缓存，连点 `/is settings` 从约 30–40 MSPT 降至可忽略不计。

    [发布 v3.19.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.19.0)

??? warning "v3.18.0 新内容 — Minecraft 26.2 支持需要 Java 25（服务器）"
    **发布于：** 2026-06-27

    - 🔺 **Minecraft 26.2 支持 + Java 25。** BentoBox 现在运行在 Minecraft 26.x 系列上（运行时支持 26.2），构建已迁移到 Java 25 工具链。**你的服务器必须运行在能够支持 Java 25 的 Paper 26.x 构建上。** 已构建的附属 jar 保持不变 — 只有重新编译此版本的附属*开发者*需要将他们自己的构建迁移到 Java 25。兼容性：Paper Minecraft 1.21.5 – 26.2，Java 25+。
    - ⚙️ **Dynmap 岛屿标记/区域切换。** `config.yml` 中的新 `dynmap` 部分添加了 `island-markers`（每个岛屿中心的房屋图标）和 `island-areas`（保护区域边框框）开关。两者都默认为 `true`，保持现有行为；将任一项设置为 `false` 并运行 `/bbox reload` 以在岛屿密集时隐藏地图上的这些叠加层。
    - **管理员范围奖励管理。** 新增 `/[admin] range removebonus` 和 `/[admin] range purgebonus` 命令用于清除单个岛屿或每个岛屿的奖励保护范围 — 理想情况下在卸载提供奖励范围的附属之后（见上面的"每个游戏模式的管理员命令"表）。
    - 🐛 `/is team setowner` 在转移给现有队伍成员时不再被岛屿限制所阻挡。
    - 🐛 Vault 钩子现在在附属启用后重试，修复了依赖加载顺序的经济集成。

    [发布 v3.18.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.18.0)

??? note "v3.18.1 新内容"
    **发布于：** 2026-07-01

    维护版本。

    - 🐛 **多行物品栏名称 & 名称保持颜色。** GUI 工具提示的第一行之后的文本不再回退到默认紫色 — 序列化程序现在在每个换行符后重新发射活跃颜色（和装饰），修复了所有附属中的工具提示。

    [发布 v3.18.1](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.18.1)
