# 岛屿 { #islands }

每个 BentoBox 游戏模式都建立在**岛屿**之上：属于一个玩家或团队的世界的受保护区域。（在 CaveBlock 或 Boxed 等游戏模式中，"岛屿"是一个洞穴或盒子，但工作方式相同。）这个页面涵盖了如何创建、调整大小、重置和删除岛屿、家点如何工作，以及如何清理旧岛屿。

!!! info "这个页面中的命令"
    命令以 BSkyBlock（`/island`、`/bsbadmin`）显示。其他游戏模式使用他们自己的命令名称，例如 AOneBlock 中的 `/ob`。权限以游戏模式的前缀开头，例如 `bskyblock.` 或 `aoneblock.`。对于玩家看到的内容，请将他们发送到[玩家指南](../Player-Guide.md)。

## 打开前：规划世界 { #before-you-open-plan-the-world }

游戏模式的 `config.yml` 中的两个设置**在岛屿存在后无法改变**。稍后改变它们意味着擦除世界和数据库，所以在玩家加入前决定：

```yaml
world:
  # Radius of each island's space, in blocks.
  # Island centres are twice this apart, so 400 puts centres 800 blocks apart.
  distance-between-islands: 400
  # How much of that space the owner protects to start with (a radius).
  # Can be raised later per island, up to distance-between-islands.
  protection-range: 50
```

- `distance-between-islands` 是岛屿能够成长的**最大**值。将其设置为你可能想给 VIP 或作为升级出售的最大大小。
- `protection-range` 是岛屿**开始**的地方。它是玩家可以建造和保护的区域。

你可能想查看的其他设置：`island-height`（起始岛屿的 Y 水平）、`max-islands`（限制世界中的岛屿数量，`0` = 无限制）和 `start-x`/`start-z`（也无法稍后改变）。

## 创建岛屿 { #creating-islands }

新玩家输入 `/island`。BentoBox：

1. 如果有多个初始岛屿可供选择，显示**创建岛屿**菜单（否则跳过）。
2. 查找下一个空闲位置，粘贴初始岛屿，并将玩家传送到那里。

你可以改变发生的事情：

| 设置（游戏模式 `config.yml`） | 默认值 | 作用 |
|---|---|---|
| `new-player-action` | `create` | 没有岛屿的玩家 `/island` 做什么 |
| `default-action` | `go` | 有岛屿的玩家 `/island` 做什么 |
| `create-island-on-first-login.enable` | `false` | 新玩家加入时自动创建岛屿 |
| `teleport-player-to-island-when-created` | `true` | 玩家的岛屿准备好时传送玩家 |

**初始岛屿的选择。** 创建岛屿菜单中的每个选择都是一个蓝图包。要使其仅对某些玩家可用（例如 VIP 岛屿），在 `/bsbadmin blueprint` 中将其设置为需要权限，然后给予 `bskyblock.island.create.<bundle-name>`。参见[初始岛屿（蓝图）](../Blueprints.md)。

## 岛屿大小（保护范围）{ #island-size-protection-range }

保护范围是所有者控制的岛屿中心周围的半径。玩家用 `/island info` 可以看到它；管理员可以用 `/bsbadmin range display` 在游戏中显示它。

给一些玩家更大的岛屿：

| 如何 | 命令或权限 |
|---|---|
| 按等级或 VIP，自动 | 给所有者 `bskyblock.island.range.<number>`。在岛屿创建时和所有者登入时检查 |
| 一个岛屿，手动 | `/bsbadmin range set <player> <range>`，或 `range add` / `range remove` 按数量改变 |
| 回到默认值 | `/bsbadmin range reset <player>` |

范围不能超过 `distance-between-islands`。像[升级](../../addons/Upgrades/index.md)这样的附属也可以将范围作为奖励添加；用 `/bsbadmin range removebonus <player>` 移除附属奖励。

## 家点 { #homes }

玩家用 `/island` 或 `/island go` 传送到他们的岛屿，并用 `/island sethome` 移动他们的家点。

默认情况下，每个岛屿有一个家点。要允许更多命名的家点：

```yaml
island:
  max-homes: 1    # game mode config.yml
```

或给所有者 `bskyblock.island.maxhomes.<number>`。玩家然后使用 `/island sethome <name>`、`/island go <name>` 和 `/island homes`。管理员可以用 `/bsbadmin maxhomes <player> <number>` 改变一个岛屿。

`/island go <name>` 即使玩家弄错大写字母或只输入名称的开始也能找到家点。在 Minecraft 26 及更高版本上，输入 `/island go` 的有多个家点的玩家会得到一个弹出窗口来选择一个（BentoBox 的 `config.yml` 中的 `island.dialogs.go-picker`）。

**地狱和末地中的家点**（当游戏模式有岛屿地狱和末地世界时）由 `island.sethome.nether.allow` 和 `island.sethome.the-end.allow` 控制。

| 管理任务 | 命令 |
|---|---|
| 将玩家的家点放回默认位置 | `/bsbadmin resethome <player>` |
| 删除玩家的所有命名家点 | `/bsbadmin deletehomes <player>` |
| 去玩家的岛屿 | `/bsbadmin tp <player>` |

## 岛屿名称 { #island-names }

玩家用 `/island setname <name>` 命名他们的岛屿，用 `/island resetname` 移除名称。名称显示在排行榜、传送点和占位符中。

在 **BentoBox 的** `config.yml` 中设置规则：

```yaml
island:
  name:
    min-length: 4
    max-length: 20
    uniqueness: false   # true = no two islands in a game mode can share a name
```

玩家需要 `bskyblock.island.name.format` 在名称中使用颜色。管理员可以通过站在岛屿上并运行 `/bsbadmin resetname` 来清除冒犯性的名称。

## 重置岛屿 { #resetting-islands }

`/island reset` 给玩家一个新岛屿。**旧岛屿被删除。** 只有所有者可以重置；任何团队成员都会从岛屿中移除。

在游戏模式的 `config.yml` 中控制它：

```yaml
island:
  reset:
    reset-limit: -1   # -1 = unlimited, 0 = no resets, 2 = two resets (three islands in total)
```

并在 BentoBox 的 `config.yml` 中：

```yaml
island:
  cooldown:
    time:
      reset: 300        # seconds a player must wait between resets
  confirmation:
    commands:
      reset: true       # players must confirm before resetting
```

从玩家身上清除什么（物品栏、末地箱、金钱、XP）在新岛屿上由[团队和等级](Teams.md#what-happens-to-items-and-money-when-players-join-or-leave)中描述的 `on-join` 选项设置。

给玩家更多重置，改变他们的重置计数：

| 命令 | 效果 |
|---|---|
| `/bsbadmin resets reset <player>` | 回到 0 次重置使用 |
| `/bsbadmin resets set <player> <number>` | 设置他们使用了多少次重置 |
| `/bsbadmin resets add <player> <number>` | 计算更多重置为已使用 |
| `/bsbadmin resets remove <player> <number>` | 给予重置回 |

没有额外重置的权限；使用这些命令，例如从排名或商店插件。

## 删除岛屿 { #deleting-islands }

| 我想要… | 命令 |
|---|---|
| 删除玩家的岛屿 | `/bsbadmin delete <player>` |
| 删除我站着的岛屿 | `/bsbadmin delete`（仍有团队时被拒绝） |
| 在清理运行前撤销删除 | 站在其上并运行 `/bsbadmin undelete` |
| 给已删除或无主的岛屿一个玩家 | 站在其上并运行 `/bsbadmin register <player>` |
| 移除所有者但保留方块 | `/bsbadmin unregister <owner>` |

删除岛屿会立即移除所有者，所以玩家可以创建新的。**方块**稍后被移除，当区域文件被清理时（见下方）。直到那时，`undelete` 或 `register` 可以恢复岛屿。

## 清理旧岛屿 { #cleaning-up-old-islands }

已删除和重置的岛屿，以及从未回来的玩家的岛屿占用磁盘空间。BentoBox 通过删除世界的**区域文件**（每个涵盖 512×512 块区域）来移除它们，一旦没有活跃岛屿在其中。

**自动清理**在 BentoBox 的 `config.yml` 中设置：

```yaml
island:
  deletion:
    housekeeping:
      deleted-sweep:
        enabled: true         # clean up deleted and reset islands
        interval-hours: 24
      age-sweep:
        enabled: false        # also clean up islands nobody has visited
        interval-days: 30
        min-age-days: 60
  purge-level: 10             # never purge islands above this level (needs Level)
```

已删除岛屿的扫描是安全的并且默认打开。年龄扫描默认关闭，因为它移除了从未删除的被遗弃岛屿。

**手动清理：**

| 命令 | 作用 |
|---|---|
| `/bsbadmin purge <days>` | 删除没有人接触了那么多天的区域文件中的岛屿 |
| `/bsbadmin purge deleted` | 现在清理已删除的岛屿，而不是等待扫描 |
| `/bsbadmin purge unowned` | 标记没有所有者的岛屿为可删除 |
| `/bsbadmin purge protect` | 站在岛屿上并运行此来保护它不被所有清理 |

清理会跳过有在线玩家的岛屿、生成岛屿、受保护的岛屿和 `purge-level` 之上的岛屿。

!!! warning "先备份"
    清理会从磁盘删除区域文件且无法撤销。在你的第一次清理前备份世界文件夹。与活跃岛屿共享区域文件的岛屿保持直到该区域清晰。

## 每个玩家多个岛屿 { #multiple-islands-per-player }

如果允许的话，玩家可以在游戏模式中拥有多个岛屿：

```yaml
island:
  concurrent-islands: 1          # BentoBox config.yml: default for all game modes

world:
  concurrent-islands: 1          # game mode config.yml: 0 = use BentoBox's value
  disallow-team-member-islands: true
```

或给玩家 `bskyblock.island.number.<number>`。参见[多个岛屿](../ConcurrentIslands.md)了解玩家如何创建和在岛屿之间切换。

## 找出有关岛屿的信息 { #finding-out-about-an-island }

| 命令 | 显示 |
|---|---|
| `/island info` | 你所在岛屿的所有者、团队、大小和位置 |
| `/bsbadmin info [player]` | 完整详细信息：所有者、成员、范围、家点、重置、死亡等。没有名字时是你所在的岛屿 |
| `/bsbadmin why <player>` | 记录为什么玩家可以或不能做某事。参见[管理工具](AdminTools.md) |

## 故障排除 { #troubleshooting }

**改变 `distance-between-islands` 后服务器不会启动。**
在岛屿存在后无法改变。放回旧值。

**VIP 权限获得更大岛屿或更多家点没有应用。**
权限对岛屿**所有者**进行检查，当他们登入时（对于范围，在岛屿创建时）。让所有者登出并重新登入。

**玩家没有重置了。**
`/bsbadmin resets reset <player>`。

**已删除的岛屿仍在那里。**
其方块在区域文件被清理时消失，在下一个已删除岛屿扫描时（默认 24 小时），或运行 `/bsbadmin purge deleted`。如果另一个活跃岛屿共享区域文件，方块保持。

**磁盘使用量继续增长。**
确保启用了 `deleted-sweep`，并考虑 `/bsbadmin purge <days>` 或被遗弃岛屿的年龄扫描。

## 另请参见 { #see-also }

- [玩家指南](../Player-Guide.md)：你的玩家使用的命令
- [团队和等级](Teams.md)
- [保护、标志和等级](../Island-Protection,-Flags-&-Ranks.md)
- [初始岛屿（蓝图）](../Blueprints.md)
- [多个岛屿](../ConcurrentIslands.md)
- [管理工具](AdminTools.md)
