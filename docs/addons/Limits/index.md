# 限制

**Limits** 允许你在 BSkyBlock 和 AcidIsland 等游戏模式中限制岛屿方块和实体。

此插件旨在帮助限制引起卡顿的实体或方块,例如漏斗。它可用于限制普通方块和实体,但不是所有都可以限制。

由 [tastybento](https://github.com/tastybento) 创建和维护。

{{ addon_description("Limits") }}

## 安装

1. 将 Limits 插件 jar 文件放入 BentoBox 插件的 addons 文件夹

2. 重启服务器

3. 插件将创建一个数据文件夹,里面有一个 config.yml

4. 根据需要编辑 config.yml。

5. 如果进行了更改,请重启服务器

## 指令

有一个用户指令和一个管理员指令,都叫"limits"。管理员可以检查特定岛主的限制。两者都会显示一个带有限制和当前数量的 GUI 面板。

## 设置 - Config.yml

config.yml 有以下部分:

* blocklimits

* blocklimits-nether

* blocklimits-end

* blockgrouplimits *(1.29.0+)*

* blockgrouplimits-nether / blockgrouplimits-end *(1.29.0+)*

* worlds

* entitylimits

* entitylimits-nether

* entitylimits-end

* entitygrouplimits

此外还有以下顶级开关(除注明外均在 **1.29.0** 中新增)：`apply-member-limit-perms`、`show-limit-messages`、`stacked-plants-count-as-one` 和 `log-limits-on-join`。

!!! info "按维度限制 (1.28.2+)"
    自 **1.28.2** 起,方块数量、实体数量、限制和偏移量现在会**针对主世界、下界和末地分别独立追踪**。在 `blocklimits` 或 `entitylimits` 中定义的单个限制会分别应用于每个维度。例如 `HOPPER: 10` 允许主世界 10 个、下界 10 个、末地 10 个(整个岛屿共 30 个)漏斗。如需仅覆盖某个维度,请使用可选的 `-nether` / `-end` 部分。

    升级后首次加载时,你现有的单维度数据会自动迁移到**主世界**槽位。磁盘上的格式会发生变化,因此升级前请先备份,并注意升级后不支持降级。

### blocklimits

此部分列出了每种方块材料允许的最大方块数。不要使用非方块材料,因为它们无效。限制会独立应用于每个维度(主世界、下界、末地)。

生长和损坏变种会被规范化为其规范方块 —— `BAMBOO_SAPLING` 计为 `BAMBOO`，自 **1.30.0** 起 `KELP_PLANT` 计为 `KELP` —— 所以用作限制键的变种名称(例如 `KELP_PLANT` 或 `CHIPPED_ANVIL`)配置规范方块的限制。

### blocklimits-nether / blocklimits-end

可选部分,分别用于覆盖下界或末地的 `blocklimits` 默认值。它们在默认配置中是注释掉的;取消注释并添加条目即可设置特定维度的方块限制。

### worlds

此部分列出了特定世界的方块限制。你必须明确命名世界,例如 AcidIsland_world,然后列出材料和限制。世界命名的限制会覆盖上述特定世界的维度默认限制。

### entitylimits

此部分列出了玩家岛屿空间(保护区域和岛屿限制)内的默认实体限制。限制为 5 将允许最多 5 个实体。影响所有类型的生物生成。还包括矿车等实体。自 **1.28.2** 起,实体限制会独立应用于每个维度,因此下界和末地现在会被正确计数和限制(修复了区块卸载时下界/末地计数重置为零的长期问题)。

### entitylimits-nether / entitylimits-end

可选部分,分别用于覆盖下界或末地的 `entitylimits` 默认值。它们在默认配置中是注释掉的;取消注释并添加条目即可设置特定维度的实体限制。

注意:限制 GUI 中只显示前 49 个受限方块和实体。

### entitygrouplimits

!!! note "实验性功能"

以下功能仅在开发版本中可用,你可以在 ci.codemc.org 上找到。

```yaml
entitygrouplimits:
  friendly:
    limit: 2
    entities:
    - COW
    - SHEEP
  monsters:
    limit: 4
    entities:
    - ZOMBIE
    - CREEPER
```

### blockgrouplimits

!!! info "自 1.29.0 起"
    `entitygrouplimits` 的方块版对应功能：对一组方块材料共享一个限制。组内每个成员的数量会被累加并与组限制进行比对,因此玩家无法通过在相关方块之间转换(例如草方块 → 泥土)或分散到多个变种(活塞/粘性活塞)来规避限制。如果同时设置了 `blocklimits`,单个限制仍会叠加生效。

用 `icon`、共享的 `limit` 和 `materials` 列表定义一个命名组：

```yaml
blockgrouplimits:
  Pistons:
    icon: PISTON
    limit: 10
    materials:
    - PISTON
    - STICKY_PISTON
  Soil:
    icon: GRASS_BLOCK
    limit: 200
    materials:
    - GRASS_BLOCK
    - DIRT
    - DIRT_PATH
    - FARMLAND
```

可通过 `blockgrouplimits-nether` / `blockgrouplimits-end` 进行按环境覆盖,它们只覆盖已在 `blockgrouplimits` 中定义的某个组的数值限制：

```yaml
blockgrouplimits-nether:
  Pistons: 5
```

!!! warning "更改分组后请运行重新计数"
    在添加方块组(或更改下面的 `stacked-plants-count-as-one`)后,请运行 `/[player_command] limits recount`,使存储的计数与新的计数规则相匹配。

### ItemsAdder 和 Oraxen 自定义方块

!!! info "自 1.29.0 起"
    来自 **ItemsAdder** 和 **Oraxen** 的自定义方块可以直接在现有的 `blocklimits` 部分(及其 `-nether`/`-end` 和 `worlds:` 覆盖)中使用它们的 ID 进行限制。强制执行通过 BentoBox 钩子使用各插件自己的放置/破坏事件,仅在安装了对应插件时才会注册。含冒号的键需要加引号。

```yaml
blocklimits:
  "iafestivities:christmas/christmas_tree/green_orb": 5
  "oraxen:caveblock": 10
```

### 其他开关

=== "apply-member-limit-perms"
    !!! summary "说明"
        (**1.29.0+**) 设为 `true` 时,队伍成员的 `<gamemode>.island.limit.*` 权限会在其登录时并入岛屿的限制 —— 取最高值。合作者(coop)和信任玩家不是队伍成员,他们的权限永远不会生效。

        默认值：`false`

=== "show-limit-messages"
    !!! summary "说明"
        (**1.29.0+**) 设为 `false` 时,限制会被静默执行 —— 放置和生成仍会被阻止,但玩家不会收到到达限制的提示消息。

        默认值：`true`

=== "stacked-plants-count-as-one"
    !!! summary "说明"
        (**1.29.0+**) 设为 `true` 时,无论一根 `SUGAR_CANE`(甘蔗)、`BAMBOO`(竹子)或 `KELP`(海带，自 **1.30.0** 起)长多高,都只算作一株植物 —— 只计算基座段。更改此选项后请运行重新计数。

        默认值：`false`

=== "log-limits-on-join"
    !!! summary "说明"
        当岛屿拥有者加入时,将该岛屿的限制记录到控制台。自 **1.29.0** 起,此项**默认为 `false`**(此前默认为 `true`),因为它在拥有大量基于权限的限制的服务器上会刷屏控制台。如果你依赖该输出进行调试,可将其改回 `true`。

        默认值：`false`

### 自动实体重新计数 { #automatic-entity-recounts }

!!! info "自 1.30.2 起"
    实体计数以增量方式维护，所以任何遗漏的事件（嗅探蛋孵化、生物跨越传送门、崩溃前批量保存中丢失的增量）都可能导致计数偏离现实，除了手动重新计数外别无他法。这些选项在后台自动协调计数。它们**默认关闭**，因为重新计数会加载岛屿保护区域的所有区块：成本随保护范围的平方增长（范围 50 时每个世界 64 个区块，范围 400 时 2601 个）。重新计数是异步的，限流到一次一个岛屿，去重和按岛屿节流，仅重写**实体**计数——方块计数保持不变。重新计数*替换*计数而不是合并，所以仅当岛屿的区块被加载时才准确。

=== "recount-on-join"
    !!! summary "说明"
        当岛屿拥有者登录时，运行岛屿的仅限实体的后台重新计数。

        默认值：`false`

=== "recount-on-join-cooldown"
    !!! summary "说明"
        同一岛屿自动重新计数之间的最小秒数（与定期扫描共享）。

        默认值：`300`

=== "recount-periodic"
    !!! summary "说明"
        定期扫描在线岛屿以协调其实体计数，即使所有者保持登录状态。成本和注意事项与 `recount-on-join` 相同。

        默认值：`false`

=== "recount-periodic-interval"
    !!! summary "说明"
        定期扫描周期之间的秒数。

        默认值：`300`

=== "recount-periodic-batch"
    !!! summary "说明"
        每个扫描周期要协调的岛屿数。在高人口服务器上保持较小。

        默认值：`2`

=== "recount-max-chunks"
    !!! summary "说明"
        保护区域覆盖超过此数量区块/世界的岛屿永远不会自动重新计数；每个岛屿记录一次警告。1000 个区块对应约 240 的保护范围。通过 `recount` 和 `calc` 命令的手动重新计数不受影响。

        默认值：`1000`

## 权限

岛主可以拥有覆盖默认设置或世界设置的独占权限。支持两种格式:

1. `GAME-MODE-NAME.island.limit.MATERIAL.LIMIT` — 应用于所有维度。

    示例: `bskyblock.island.limit.hopper.10`

2. `GAME-MODE-NAME.island.limit.ENV.MATERIAL.LIMIT` — 仅应用于单个维度,其中 `ENV` 为 `overworld`、`nether` 或 `end` 之一 (1.28.2+)。

    示例: `bskyblock.island.limit.nether.hopper.5`

权限在玩家登录时激活。

使用权限是(在前面加上游戏模式名称,例如 acidisland):

```
GAMEMODE_NAME.limits.player.limits:
  description: 玩家可以使用 limits 指令
  default: true

GAMEMODE_NAME.mod.bypass:
  description: 玩家可以绕过限制 
  default: op

GAMEMODE_NAME.limits.admin.limits:
  description: 玩家可以使用管理员 limits 指令
  default: op
```

完整权限列表在[此处](Permissions)。

## 占位符

{{ placeholders_source(source="Limits") }}

!!! note "方块占位符名称"
    `[material]` 是不含 `minecraft:` 命名空间的小写 Minecraft 键，如 `%Limits_bskyblock_island_spawner_limit%`。来自 ItemsAdder 或 Oraxen 的自定义方块使用 `namespace_key`（例如 `itemsadder_ruby_block`），因为冒号在占位符名称中无效。在 1.28.0 到 1.30.0 版本之间，方块的 `_count`、`_limit` 和 `_base_limit` 占位符被错误地注册为带有内嵌的命名空间，无法解析；已在 **1.30.1** 中修复。


## 翻译

{{ translations("Limits") }}

## 无法限制的物品

有些物品（目前）无法限制。原因通常是因为有太多方法可以在不被跟踪的情况下移除物品。如果你是程序员并且可以找出如何解决这些问题，请提交 PR！

* 点燃的 TNT
* 唤魔者尖牙
* 羊驼唾沫
* 龙火球
* 区域效果云
* 末影信号
* 小火球
* 火球
* 扔出的经验瓶
* 潜影贝导弹
* 凋灵头颅
* 三叉戟
* 箭
* 光灵箭
* 雪球
* 鸡蛋
* 拴绳
* 末影水晶
* 末影珍珠
* 末影龙

!!! tip "物品展示框和画现在可以被限制 (1.29.0)"
    物品展示框、荧光物品展示框和画此前也在此列表中。自 **1.29.0** 起,实体计数是持久化且事件驱动的,因此这三者现在都可以像其他任何实体一样在 `entitylimits` 下配置。


## 对于开发者：豁免实体

!!! info "即将在 1.30.2 之后的下一个版本中推出"

另一个插件或附属可以生成 Limits 完全忽略的实体。这对于临时生物（如事件波或小游戏 NPC）很有用，这些不应消耗岛屿的实体限制。在 **spawn 消费者中**使用持久数据键 `limits:exempt`（任何值）标记实体，以便在 `CreatureSpawnEvent` 触发时标签已存在：

```java
NamespacedKey limitsExempt = NamespacedKey.fromString("limits:exempt");
world.spawn(location, Zombie.class, zombie ->
        zombie.getPersistentDataContainer().set(limitsExempt, PersistentDataType.BYTE, (byte) 1));
```

标记的实体：

- 永远不会被实体或组限制阻止
- 永远不会被计数，所以它不会使用岛屿的限制
- 当它死亡、被移除或通过传送门时不会改变任何计数
- 被跳过重新计数，包括 `calc` 命令和[自动实体重新计数](#automatic-entity-recounts)

同一岛屿上未标记的实体会照常受到限制。标签与实体一起保存，所以豁免在区块卸载和服务器重启后仍然有效。你不需要 Limits 作为依赖；如果你对其进行编译，`Limits.EXEMPT_KEY` 是相同的键。

!!! warning "仅在生成时添加标签"
    在实体生成时添加标签，之后永远不要添加或移除它。稍后标记的实体已被计数，移除时不会递减，之后移除标签会导致相反的问题。无论哪种情况，岛屿的计数都是错误的，直到下一次重新计数。


## 更新日志

??? note "v1.30.2 新内容 —— 自动实体重新计数"
    **发布于：** 2026-09-06

    一个活塞计数修复加上一个新的可选功能。兼容性：BentoBox API 2.7.1 · Paper Minecraft 1.21.11 – 26.2 · Java 21。

    - ⚙️ **自动实体重新计数（可选启用）。** 新的 `recount-on-join` 和 `recount-periodic` 选项在后台协调漂移的实体计数——见上文[自动实体重新计数](#automatic-entity-recounts)。六个新键（`recount-on-join`、`recount-on-join-cooldown`、`recount-periodic`、`recount-periodic-interval`、`recount-periodic-batch`、`recount-max-chunks`）自动添加到 `config.yml` 且使用安全的默认值，所以除非你启用它们，否则没有任何改变。在开启前读取配置注释。感谢 @daniel-skopek。
    - 🐛 **扩展活塞不再计数两次。** 管理员重新计数（`calc`）对每个扩展活塞计数其基座和头部，所以所有活塞都扩展的红石建造会翻倍计数（16 个粘性活塞显示为 32/30），每次重新计数都会放回错误的数字。重新计数现在仅计数基座，破坏两部分的爆炸递减一次。
    - 🐛 **穿越传送门的实体正确递减。** 实体穿越传送门，同时在岛屿保护范围外时，其源维度计数从未被递减。

    **活塞注意：** 活塞计数膨胀的岛屿在此版本进行一次重新计数（`/[admin_command] limits calc <player>`）后显示正确的数字。

    [发布 v1.30.2](https://github.com/BentoBoxWorld/Limits/releases/tag/1.30.2)

??? warning "v1.30.1 新内容 —— 如果你运行 Greenhouses 请重新计数"
    **发布于：** 2026-09-04

    两个准确性修复。兼容性：BentoBox API 2.7.1 · Paper Minecraft 1.21.11 – 26.2 · Java 21。无配置或区域设置更改。

    - 🐛 **方块计数和限制占位符再次有效。** 自 1.28.0 以来，每个方块占位符都注册为命名空间内嵌在其名称中，所以 `%Limits_bskyblock_island_spawner_limit%` 实际上是 `%Limits_bskyblock_island_minecraft:spawner_limit%`，PlaceholderAPI 返回其未解析。所有方块 `_count`、`_limit` 和 `_base_limit` 占位符，包括 `_overworld`、`_nether` 和 `_end` 变种，现在都注册在文档化的名称下。实体占位符从未受影响。
    - 🔺 🐛 **取消的生成被移除时实体计数不再漂移。** 当 Limits 在限制处取消生成，生成插件随后对该从不添加的实体调用 `remove()`（Greenhouses 做了这个），Paper 仍然触发 `EntityRemoveEvent`，Limits 为从不计数的生物递减计数，所以下一次生成溜过去（例如 4/3 的恶灵）。从不进入世界的实体移除现在被忽略。

    🔺 **重新计数注意：** 如果你运行 Greenhouses（或任何移除其无法生成的实体的插件），受影响岛屿的实体计数可能在旧版本下漂移降低。在受影响的岛屿上运行 `/[admin_command] limits calc <player>`，或让玩家运行 `/[player_command] limits recount`，使计数与现实相匹配。

    [发布 v1.30.1](https://github.com/BentoBoxWorld/Limits/releases/tag/1.30.1)

??? warning "v1.30.0 新内容 —— 建议重新计数海带"
    **发布于：** 2026-08-15

    两个计数准确度修复。兼容性：BentoBox API 2.7.1 · Paper Minecraft 1.21.11 – 26.2 · Java 21。无配置或本地化更改。

    - 🐛 **蜜蜂可以始终离开它们的蜂巢。** 蜜蜂退出蜂巢不是新蜜蜂 —— 它的计数在进入时已减少 —— 但退出仍然会被限制检查。在岛屿达到其蜜蜂限制时，释放被取消，服务器每几个刻重试，附近玩家被垃圾邮件轰炸"蜜蜂产生受限为…"，存储的蜜蜂永远被困。蜂巢退出现在在检查中被豁免，同时仍被计数，所以进入/退出循环保持净零。放置一个携带从未计数蜜蜂的蜂巢物品可以让岛屿略微超过其限制；这只是阻止进一步的产生和繁殖，直到种群下降。
    - 🔺 🐛 **海带列数计数正确。** 海带生长将 `KELP` 顶端转换为 `KELP_PLANT` 茎段，无 Bukkit 事件，所以旧方块从未被递减，海带计数仅增加，最终在幻影总数中阻止放置。`KELP_PLANT` 现在被规范化为 `KELP`（如 `BAMBOO_SAPLING`/`BAMBOO`）：生长是计数中立的，破坏列的基座递减每一段，`KELP` 参与 `stacked-plants-count-as-one`，变种名称如 `KELP_PLANT` 或 `CHIPPED_ANVIL` 用作限制键配置规范限制。

    🔺 **如果你限制海带，请重新计数。** 存储的海带计数在以前的版本下可能向上漂移。在受影响的岛屿上运行 `/[admin_command] limits calc <player>` —— 或让玩家运行 `/[player_command] limits recount` —— 使计数与现实相匹配。

    [发布 v1.30.0](https://github.com/BentoBoxWorld/Limits/releases/tag/1.30.0)

??? note "v1.29.1 新内容"
    **发布于：** 2026-07-23

    兼容性：BentoBox API 2.7.1 · Paper Minecraft 1.21.11 – 26.2 · Java 21。无配置或本地化更改——这是一个即插即用的替换版本。

    - 🐛 **自然繁殖现在会遵守实体限制。** 没有玩家参与的繁殖（蜜蜂、狐狸、村民驱动的繁殖装置等）此前完全绕过了限制检查，导致数量可能超出配置的上限。现在所有繁殖都会被检查。拥有 OP 或豁免权限的玩家仍然不受限制。
    - 🐛 **自动繁殖装置不再每刻重试。** 当繁殖因达到限制而被拒绝时，双亲都会进入繁殖冷却；除非确实有玩家在喂食，否则不会向附近玩家发送达到限制的提示消息。
    - 🐛 **玩家条目不再泄漏进实体跟踪映射。** 玩家此前会被加入实体—岛屿跟踪映射且从不移除。
    - 🐛 **`recount` 现在会统计船。** 管理员重新计数只统计矿车而跳过了船，导致船的计数被清零，而实时跟踪器之后无法恢复。

    感谢 [@daniel-skopek](https://github.com/daniel-skopek) 提供的修复。

    [发布 v1.29.1](https://github.com/BentoBoxWorld/Limits/releases/tag/1.29.1)

??? note "v1.29.0 新内容"
    **发布于：** 2026-07-10

    兼容性：BentoBox API 2.7.1 · Paper Minecraft 1.21.11 – 26.2 · Java 21。

    - ⚙️ **方块组限制。** 对一组方块材料共享一个限制(例如活塞 + 粘性活塞,或草/泥土/耕地),使玩家无法通过在相关方块之间转换来规避限制。在 `blockgrouplimits` 下配置,支持 `-nether`/`-end` 覆盖。详见上面的"配置"部分。
    - ⚙️ **ItemsAdder 和 Oraxen 自定义方块限制。** 直接在 `blocklimits` 中使用命名空间 ID 来限制自定义方块。
    - ⚙️ **队伍成员限制权限(可选启用)。** 设置 `apply-member-limit-perms: true` 后,队伍成员的 `island.limit.*` 权限可以为岛屿限制作出贡献,而不仅限于拥有者。
    - 🔡 **到达限制占位符与 API。** 新增 `%Limits_<gamemode>_island_reached_limits%` 占位符(以及 `_overworld`/`_nether`/`_end`)列出哪些限制已达上限,由新的 `Limits#getReachedLimits(...)` API 支持。关闭了追踪器中最古老的未决工单(2018 年提交)。
    - ⚙️ **可堆叠植物可算作一株。** 可选地将整根甘蔗或竹子算作一株植物(`stacked-plants-count-as-one`)。
    - ⚙️ **静默执行选项。** `show-limit-messages: false` 关闭到达限制的聊天消息,同时仍强制执行限制。
    - 🔡 **手动翻译材料/实体名称。** 本地化文件现在可以翻译 GUI 和到达限制消息中显示的方块/实体名称。
    - **物品展示框、荧光物品展示框和画现在可以在 `entitylimits` 下限制。**
    - 🐛 **修复：来自穿越传送门的生物导致的幽灵实体计数**(例如岛上没有鸡却显示 `Chicken 10/10`),以及铜傀儡建造绕过 `COPPER_CHEST` 限制的问题。
    - ⚙️ **`log-limits-on-join` 现在默认为 `false`** —— 如果你依赖该控制台输出,可将其改回 `true`。

    !!! warning "新配置选项不会自动添加"
        新键**不会**出现在现有的 `config.yml` 中 —— 请从上面的列表中添加你需要的键,或删除配置以重新生成。在添加方块组或更改 `stacked-plants-count-as-one` 后,请运行重新计数,使存储的计数与新的计数规则相匹配。

    [发布 v1.29.0](https://github.com/BentoBoxWorld/Limits/releases/tag/1.29.0)

??? note "v1.28.4 新内容"
    **发布于：** 2026-07-06

    以保持实体计数准确并可靠持久化为重点的维护版本。无需任何配置或本地化更改。

    - 🐛 **实体计数不再高于实际值。** 在某些生成/移除序列下，被跟踪的实体计数可能会超过岛屿上实际存在的实体数量，最终阻止本应被允许的生成。计数现在会与岛屿的真实数量保持同步。[[#273](https://github.com/BentoBoxWorld/Limits/pull/273)]
    - 🐛 **实体计数持久化已集中化。** 所有实体计数的变更现在都通过 `BlockLimitsListener` 进行，因此这些变更会被纳入正常的批量保存周期，而不是仅在附属禁用时才写入。这可以防止在非正常关闭或崩溃时丢失计数。[[#274](https://github.com/BentoBoxWorld/Limits/pull/274)]

    [发布 v1.28.4](https://github.com/BentoBoxWorld/Limits/releases/tag/1.28.4)

??? note "v1.28.3 新内容"
    **发布于：** 2026-06-29

    bug 修复版本 — 无数据、配置或本地化更改；即插即用替换，使每岛屿**实体计数**在服务器重启后可靠。

    - 🐛 **实体计数在重启后不再漂移。** 将每个实体链接到其岛屿的映射仅保存在内存中，每次重启时丢失。从区块重新加载的实体从未重新进入它，所以当他们稍后在岛屿**外**死亡或消失时，他们的计数从未递减，并缓慢上升。实体现在在其区块加载时重新注册，所以岛屿外移除现在正确递减。
    - 🩹 **区块卸载时不再增长映射。** 内存中映射现在在区块卸载时释放（并在重新加载时重建），防止长期运行的服务器上的无限增长。

    [发布 v1.28.3](https://github.com/BentoBoxWorld/Limits/releases/tag/1.28.3)

??? warning "v1.28.0 新内容 — 需要 Java 21"
    **发布于:** 2026-03-xx

    - 🔺 **现在需要 Java 21。** 请在升级前更新服务器的 Java 版本。
    - 修复:潜影箱物品复制漏洞,当物品从受限制的潜影箱移动时可能触发。
    - 修复:铜块在氧化过程中不能正确更新限制计数的问题。

    [在 GitHub 上查看发布记录](https://github.com/BentoBoxWorld/Limits/releases)

??? note "v1.28.1 新内容"
    **发布于:** 2026-03-xx

    - 修复:从旧版本迁移数据库时的迁移错误。
    - 修复:limits GUI 面板中方块限制显示不正确的问题。

    [在 GitHub 上查看发布记录](https://github.com/BentoBoxWorld/Limits/releases)

??? warning "v1.28.2 新内容 — 按维度限制(数据迁移)"
    **发布于:** 2026-06-13

    - 🔺⚙️ **按维度限制。** 方块数量、实体数量、限制和偏移量现在会针对主世界、下界和末地分别独立追踪,修复了区块卸载时下界/末地计数重置为零的长期问题([#43](https://github.com/BentoBoxWorld/Limits/issues/43))。单个 `blocklimits`/`entitylimits` 值现在会分别应用于每个维度,并新增了可选的 `blocklimits-nether`、`blocklimits-end`、`entitylimits-nether` 和 `entitylimits-end` 覆盖部分。
    - 🔺 **数据迁移。** 现有的单维度数据会在首次加载时迁移到**主世界**槽位。磁盘上的格式会发生变化,因此升级前请先备份;升级后不支持降级。
    - 🔺 **按维度权限。** 新的 6 段式格式 `<gamemode>.island.limit.<overworld|nether|end>.<KEY>.<NUMBER>` 可将限制限定到单个维度。现有的 5 段式格式仍然应用于所有维度。
    - 🐛 计数精度修复:床/门重复计数([#86](https://github.com/BentoBoxWorld/Limits/issues/86))、铁傀儡/雪傀儡的方块移除改为以南瓜为基准而非生成方块([#127](https://github.com/BentoBoxWorld/Limits/issues/127))、三个实体计数错误、达到限制时不再消耗刷怪蛋([#134](https://github.com/BentoBoxWorld/Limits/issues/134)),以及重新计数期间的计数泄漏。
    - 🩹 修复了因引用 1.21.9 铜块而在 Minecraft 1.21.8 及更早版本服务器上发生的 `NoSuchFieldError` 崩溃;这些材料现在按名称解析。
    - 🔡 所有捆绑的语言文件已从旧版 `&` 颜色代码转换为 MiniMessage,并在全部 21 种语言中同步了缺失的键。如果你自定义过任何语言字符串,请对照新文件进行检查。

    兼容性: BentoBox API 2.7.1 · Minecraft 1.21.5 – 26.1.2 · Java 21。

    [Release v1.28.2](https://github.com/BentoBoxWorld/Limits/releases/tag/1.28.2)