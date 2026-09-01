# InvSwitcher

**InvSwitcher** 在不同世界之间分离玩家物品栏和其他方面。

由 [tastybento](https://github.com/tastybento) 创建和维护。

{{ addon_description("InvSwitcher") }}

以下内容在每个世界之间独立:

* 物品栏和盔甲
* 进度
* 饥饿度
* 经验值
* 生命值
* 游戏模式(创造、生存等)
* 金钱(按世界经济,1.18.0 新增 —— **自 1.19.3 起默认关闭**，通过 `options.money: true` 启用)

## 如何使用

1. 将插件 jar 文件放入 BentoBox 插件的 addons 文件夹
2. 重启服务器
3. 完成!

## Config.yml

InvSwitcher 有一个 `config.yml`,包含两个主要部分。

### 世界

列出 InvSwitcher 运行的游戏模式世界。下界和末地世界会自动包含。

```yml
worlds:
- acidisland_world
- oneblock_world
- boxed_world
- bskyblock_world
- skyblock-world
- caveblock-world
- poseidon_world
- stranger_world
- skygrid-world     # 在 1.19.2 添加到默认配置
- raft_world        # 在 1.19.2 新增
- brix_world        # 在 1.19.2 新增
- parkour_world     # 在 1.19.2 新增
- tradewinds_world
```

!!! warning "现有配置不被重写"
    新的默认世界只出现在全新安装上。如果你的 `config.yml` 早于 1.19.2 并且你运行 SkyGrid、Raft、Brix、Parkour 或 TradeWinds，手动将这些条目添加到 `worlds:` 列表并重启。未列出的世界会被静默地不管理 —— InvSwitcher 在启动时记录它挂接的世界，所以检查该列表以确认。

### 选项

控制每个世界(以及可选地每个岛屿)切换哪些玩家方面。

```yml
options:
  inventory: true
  health: true
  food: true
  advancements: true
  gamemode: true       # 游戏模式(生存/创造/等)
  experience: true
  ender-chest: true
  statistics: true
  money: false         # 按世界金钱(1.18.0 新增)。自 1.19.3 起默认关闭。需要 Vault。
  # 每个岛屿的物品栏切换(1.17.0 新增)
  # 世界级选项也必须为 true,岛屿选项才能生效。
  islands:
    active: true       # 总体启用每岛屿切换
    inventory: true    # 为玩家拥有的每个岛屿提供不同的物品栏
    health: false
    food: false
    advancements: false
    gamemode: false
    experience: false
    ender-chest: true
    statistics: false
    money: false       # 每岛屿钱包(1.18.0 新增)。false 表示仅按世界金钱。
```

将 `islands.active: true` 设置为允许拥有多个岛屿的玩家每个岛屿维护独立的物品栏(以及其他方面),而不仅仅是每个游戏模式世界。

### 经济

1.18.0 新增。**自 1.19.3 起默认关闭** —— InvSwitcher 不再将自身注册为 Vault 经济，除非你选择加入 `options.money: true`。启用后，InvSwitcher 会将自身注册为 Vault 经济提供者，并为**每个切换的世界保留独立的余额**。交易(商店买卖、`/pay`、jobs 等)会被路由到其所属世界的余额——即使目标玩家离线或身处其他世界。InvSwitcher 不管理的世界会传递给你现有的经济插件(如 EssentialsX);如果不存在其他经济插件,InvSwitcher 会自己处理所有世界。

!!! warning "需要 Vault"
    按世界金钱需要 [Vault](https://www.spigotmc.org/resources/vault.34315/) 插件。单独的经济插件是可选的——InvSwitcher 可以作为唯一的经济系统。如果你使用 **Bank** 插件,岛屿钱包也会变为按世界。

`economy:` 部分仅在 `options.money` 为 `true` 时使用:

```yml
economy:
  starting-balance: 0.0              # 玩家首次进入受管理世界时获得的余额(除非已导入)
  currency-name-singular: Dollar
  currency-name-plural: Dollars
  fractional-digits: 2               # 小数点后位数
  import-existing-balances: true     # 首次进入时一次性导入每个玩家的现有余额
  delegate-unmanaged-worlds: true    # 将不受管理的世界传递给之前的经济插件
  debug: false                       # 将每笔交易记录到控制台(冗长)
```

## 指令

1.18.0 新增。每个受管理的游戏模式都会获得自己的经济指令,作用域限定为该游戏模式的世界,因此无论你身处何处,`/bsb balance` 都会显示你的 BSkyBlock 余额,`/ai balance` 显示你的 AcidIsland 余额。

!!! tip
    `[player_command]` 和 `[admin_command]` 是根据你运行的游戏模式而不同的指令。

=== "玩家指令"

    | 指令 | 描述 |
    |---|---|
    | `/[player_command] balance` | 显示你在此世界的金钱余额 |
    | `/[player_command] pay <玩家> <金额>` | 向另一名玩家付款 |

=== "管理员指令"

    | 指令 | 描述 |
    |---|---|
    | `/[admin_command] eco give <玩家> <金额>` | 给予玩家金钱 |
    | `/[admin_command] eco take <玩家> <金额>` | 扣除玩家金钱 |
    | `/[admin_command] eco set <玩家> <金额>` | 设置玩家余额 |
    | `/[admin_command] eco balance <玩家>` | 显示玩家余额 |

## 权限

!!! tip
    `[gamemode]` 是一个根据你运行的游戏模式不同的前缀 —— 例如 `bskyblock.invswitcher.balance`。

经济指令仅在启用 `options.money` 和安装 Vault 时注册，所以这些权限仅在运行按世界经济的服务器上重要。*(自 1.19.2 起在 `addon.yml` 中声明 —— 在此之前这些节点未注册，所以指令被拒绝给除 ops 外的所有人。)*

=== "玩家权限"
    - `[gamemode].invswitcher.balance` - (默认：`true`) - 玩家可以使用 `balance` 指令。
    - `[gamemode].invswitcher.pay` - (默认：`true`) - 玩家可以使用 `pay` 指令。

=== "管理员权限"
    - `[gamemode].invswitcher.admin.eco` - (默认：`op`) - 玩家可以使用管理员 `eco` 指令。
    - `[gamemode].invswitcher.admin.eco.balance` - (默认：`op`) - 玩家可以使用管理员 `eco balance` 指令。
    - `[gamemode].invswitcher.admin.eco.give` - (默认：`op`) - 玩家可以使用管理员 `eco give` 指令。
    - `[gamemode].invswitcher.admin.eco.take` - (默认：`op`) - 玩家可以使用管理员 `eco take` 指令。
    - `[gamemode].invswitcher.admin.eco.set` - (默认：`op`) - 玩家可以使用管理员 `eco set` 指令。

!!! note
    玩家节点默认为 `true`，所以大多数服务器无需做任何事情。如果你的权限插件拒绝未列出的节点，将它们授予你的默认组。

## 它的作用

这个插件将为玩家在每个已安装的游戏模式及其对应的世界中提供独立的物品栏、生命值、饥饿度、进度和经验值。它使玩家能够独立地玩每个游戏模式。

## 一个例子

**BSkyBlock** 的物品栏、生命值、饥饿度、进度和经验值仅在其相应的世界之间共享:

- BSkyBlock_world
- BSkyBlock_world_nether
- BSkyBlock_world_the_end

**请注意:**

- 它不仅限于 BentoBox 世界。它适用于服务器上的所有世界(目前)。

## 更新日志

??? note "v1.19.3 新内容"
    **发布于：** 2026-08-04

    - ⚙️ **按世界金钱现在默认关闭。** InvSwitcher 不再将自身注册为 Vault 经济，除非你在 `config.yml` 中选择加入 `options.money: true`。除此之外，该功能没有任何改变。

    ⚙️ **现有配置不被重写** —— 新的默认值仅适用于全新安装。如果你的 `config.yml` 已经包含 `options.money: true` 并且你不希望 InvSwitcher 管理金钱，设置为 `false` 并重启。

    [发布 v1.19.3](https://github.com/BentoBoxWorld/InvSwitcher/releases/tag/1.19.3)

??? warning "v1.19.2 新内容 —— 回档修复、新权限和默认世界"
    **发布于：** 2026-08-04

    兼容性：BentoBox 3.17.0 · Paper Minecraft 1.21.5 – 26.1.2 · Java 21。

    - 🐛 **关机时在线的玩家物品栏不再回档。** BentoBox 在附属禁用后立即关闭其数据库，所以异步关闭保存丢失了竞速，被无声地丢弃 —— 玩家自上次世界更改以来所做的一切都被丢失，然后陈旧的快照在下次登录时被写回到其真实物品栏。关闭保存现在是同步的；常规游戏中的保存保持异步。在停止前注销的玩家从未受到影响，已经丢失的数据无法恢复。
    - 🔺 **经济指令对普通玩家有效。** 每个非 op 的 `/[player_command] balance` 和 `pay` 都因权限错误失败，因为 `addon.yml` 没有声明权限。这些节点现已注册 —— `[gamemode].invswitcher.balance` 和 `.pay` 默认为 `true`，管理员 `eco` 节点默认为 `op`。见上面的权限部分。如果你的权限插件拒绝未列出的节点，将玩家节点授予你的默认组。
    - ⚙️ **缺失的游戏模式世界添加到默认配置。** `skygrid-world`、`raft_world`、`brix_world` 和 `parkour_world` 不在已发货的 `worlds:` 列表中，所以全新安装无声地不管理它们。**现有配置不被重写** —— 如果你运行这些游戏模式，手动添加这些条目。
    - 📄 关于不运行第二个物品栏管理器（Multiverse-Inventories、PerWorldInventory、MultiInv）的新部分 —— 见[与其他物品栏插件的兼容性](#compatibility-with-other-inventory-plugins)。

    [发布 v1.19.2](https://github.com/BentoBoxWorld/InvSwitcher/releases/tag/1.19.2)

??? note "v1.19.1 新内容"
    **发布于：** 2026-07-02

    bug 修复版本 — 即插即用替换，无配置或本地化更改。

    - 🐛 **修复了每岛屿生命值死亡循环。** 启用每岛屿生命值的情况下，拥有多个岛屿的玩家在死亡后可能陷入无限重生/死亡屏幕。当其状态在死亡过程中被捕捉时，它记录了 `0` 的生命值；将该值加载回死亡岛屿上的活跃玩家会应用 `setHealth(0)`，在世界加载的那一刻杀死他们。InvSwitcher 现在从不向活跃玩家应用致命的存储生命值 — 存储值 `0`（仅由死亡中期产生）恢复满血，与原版重生行为相匹配。

    [发布 v1.19.1](https://github.com/BentoBoxWorld/InvSwitcher/releases/tag/1.19.1)

??? note "v1.19.0 新内容"
    **发布于：** 2026-06-21

    1.18.0 按世界经济版本的后续。即插即用替换 — 无配置或本地化更改。

    - 🐛 **独立经济现在可以自己工作。** InvSwitcher 注册了自己的按世界 Vault 经济，但 BentoBox 在附属启用前挂接 Vault，所以当 InvSwitcher 是服务器上唯一的经济时，那个早期钩子找不到任何内容并被丢弃 — 经济依赖的附属如 **Bank** 以*"需要 Vault"*禁用自己。InvSwitcher 现在在其提供者上线后向 BentoBox 注册一个新的 Vault 钩子，所以它可以作为服务器的唯一经济工作（无需单独的经济插件如 EssentialsX）。
    - 🐛 **离线经济交易报告的余额正确。** 管理员对离线玩家的 `eco give/set/take` 报告了过时的余额（例如给予 2,000 后显示"新余额：0.00"）。金钱总是正确地存储；确认消息在异步保存刷新之前重新读取了余额。指令现在报告由交易本身返回的权威余额，离线读写后路径得到加强，所以两个快速连续的交易不再会丢失更新。

    [发布 v1.19.0](https://github.com/BentoBoxWorld/InvSwitcher/releases/tag/1.19.0)

??? note "v1.17.0 新内容"
    **发布于:** 2026-03-31

    - **每岛屿物品栏切换。** 拥有多个岛屿的玩家现在可以在同一游戏模式中每个岛屿维护独立的物品栏(以及可选的生命值、饥饿度、经验值、末影箱、统计数据)。通过 `options.islands.active: true` 启用,并配置每个子选项。世界级选项也必须为 `true`,其对应的岛屿选项才能生效。
    - ⚙️ `config.yml` 中新增 `options.islands` 部分。
    - 错误修复:返回原始岛屿时物品栏丢失的问题。

    [发布 v1.17.0](https://github.com/BentoBoxWorld/InvSwitcher/releases/tag/1.17.0)

??? note "v1.17.1 新内容"
    **发布于：** 2026-05-09

    - 🐛 **修复了从 BentoBox 世界传送到非 BentoBox 世界时物品栏被清空的问题。** 此前，当玩家离开 BentoBox 游戏世界（如 BSkyBlock）进入非 BentoBox 世界（如默认主世界或第三方插件世界）时，他们的"外部"物品栏可能会丢失，因为每个非 BentoBox 世界都将数据存储在自己的键下。现在所有非 BentoBox 世界共享一个存储键，玩家的物品栏总能正确恢复。包含旧的按世界键存储数据的自动迁移。

    [发布 v1.17.1](https://github.com/BentoBoxWorld/InvSwitcher/releases/tag/1.17.1)

??? warning "v1.18.0 新内容 — 需要 BentoBox 3.17.0"
    **发布于：** 2026-05-31

    - 🔺⚙️🔡 **按世界金钱。** InvSwitcher 现在可以为每个游戏世界提供独立的经济,在它已经切换的物品栏、生命值、经验值和统计数据之外。启用 `options.money` 后,它会将自身注册为 Vault 经济提供者,并将每笔交易路由到正确世界的余额——即使玩家离线或身处其他世界。
    - ⚙️ **新增配置:** `options.money`、`options.islands.money` 以及一个 `economy:` 部分(起始余额、货币名称、小数位数、导入开关、委派开关、调试)。现有配置仍可正常工作;新键会以安全的默认值添加。
    - 🔡 **新增指令和占位符:** 每个游戏模式的玩家 `balance` 和 `pay`、管理员 `eco give/take/set/balance`,以及 `<gamemode>_invswitcher_balance` 和 `<gamemode>_invswitcher_balance_formatted` 占位符,已翻译为 BentoBox 附带的所有语言。
    - 🐛 进度在切换世界时不再错误地增加经验值。
    - 🐛 BentoBox 岛屿重置不再清空错误世界的物品栏——InvSwitcher 现在会改为清除正确世界的*已存储*数据。

    🔺 **需要 BentoBox 3.17.0:** InvSwitcher 现在会监听 BentoBox 的玩家重置事件(包括新的金钱重置事件),这些事件在 3.17.0 中引入。它无法在更旧的 BentoBox 版本上加载。

    🔺 **经济行为变更:** 启用 `options.money` 后,InvSwitcher 会成为服务器的 Vault 经济提供者。它不管理的世界会传递给你现有的经济(如 EssentialsX);受管理的世界获得各自的按世界余额。金钱功能需要 Vault 插件。

    [发布 v1.18.0](https://github.com/BentoBoxWorld/InvSwitcher/releases/tag/1.18.0)

## 占位符

{{ placeholders_source("InvSwitcher") }}

## 翻译

{{ translations("InvSwitcher") }}