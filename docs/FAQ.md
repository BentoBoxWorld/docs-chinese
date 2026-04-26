# 常见问题解答

本 FAQ 按照问题在 [BentoBox Discord](https://discord.bentobox.world) `#support-en` 频道中的出现频率排列——最常见的问题在最上方，罕见或旧版问题归纳在底部。

!!! info "诊断速查表——在寻求帮助*前*请先运行以下命令"
    - `/bentobox version` — 显示 BentoBox 及插件版本和服务器构建信息
    - `/[admin_command] why <玩家>` — 精确说明是哪个 BentoBox 标志（如果有）阻止了玩家的操作；这是调试"我无法破坏/放置/交互"问题的最快方法
    - `/papi parse me <占位符>` — 验证某个 PlaceholderAPI 占位符是否在你的服务器上正常解析

## 目录

- [安装与版本](#安装与版本)
- [世界与生成](#世界与生成)
- [生物、刷怪与实体](#生物刷怪与实体)
- [岛屿：大小、保护与重置](#岛屿大小保护与重置)
- [团队、合作与访客](#团队合作与访客)
- [占位符](#占位符)
- [AOneBlock](#aoneblock)
- [Level 插件](#level-插件)
- [Challenges 插件](#challenges-插件)
- [数据库与存储](#数据库与存储)
- [自定义：语言、颜色与蓝图](#自定义语言颜色与蓝图)
- [杂项](#杂项)
- [API 与插件开发](#api-与插件开发)
- [较少见/旧版问题](#较少见旧版问题)
- [来源](#来源)

## 安装与版本

### 如何安装 BentoBox、BSkyBlock 以及所有其他插件？

开始的最简单方式是从 [https://download.bentobox.world](https://download.bentobox.world) 下载一套插件和 BentoBox。
你也可以查看[本教程](BentoBox/Install-Bentobox.md)来了解其他方法。
**欢迎加入我们的社区！**

### 我的 Minecraft 版本需要哪个 BentoBox 版本？

BentoBox 主版本号与 Minecraft 版本对应：

- **BentoBox 3.x** — Minecraft **1.21.3 及更新版本**
- **BentoBox 2.7** — Minecraft **1.21.1**
- **BentoBox 2.6** — Minecraft **1.20.6**

升级服务器的 Minecraft 版本时，必须同时升级 BentoBox（以及对应的插件），反之亦然。使用更新的 BentoBox 配合旧版 Minecraft 将无法启动；在更新的 Minecraft 上使用旧版 BentoBox 通常会产生粒子缺失错误、"执行此命令时发生内部错误"提示，或 GUI 异常。旧版本可以在每个项目的 GitHub *Releases* 页面找到。

### 我的 BentoBox 版本需要哪些插件版本？

选择发行说明针对相同 BentoBox 主版本的插件。最简单的方式是从 [https://download.bentobox.world](https://download.bentobox.world) 下载"整合包"，其中始终包含兼容的插件套装。将 BentoBox 3.x 与需要 BentoBox 2.x 的插件混用（或反之）是插件加载失败最常见的原因。

### 尝试创建岛屿时提示"执行此命令时发生内部错误"是什么原因？

几乎在所有情况下，这是 BentoBox 与 Minecraft 版本不匹配（见上文）。运行 `/bentobox version` 并确认 BentoBox 主版本与 Minecraft 版本一致。如果一致，请在报告问题时提供完整的服务器日志（而不仅仅是聊天框中的错误）。

## 世界与生成

### 如何将 BentoBox 世界设置为服务器的默认世界？

按步骤遵循[将 BentoBox 世界设置为服务器默认世界](BentoBox/Set-a-BentoBox-world-as-the-server-default-world.md)的教程。人们常忽略的两点是：(1) 在 `bukkit.yml` 中为世界设置正确的生成器；(2) 在 `server.properties` 中将 `level-name` 设置为 BentoBox 世界名称。遗漏任何一步都会导致生成超平坦区块——请参阅本页底部的[我的世界中正在生成超平坦区块](#我的世界中正在生成超平坦区块)。

### 我可以在同一台服务器上运行两种游戏模式（例如 BSkyBlock 和 Boxed）吗？

可以——你不能在**同一个世界**中运行两种游戏模式，但每个 BentoBox 游戏模式插件都会创建并管理自己的世界，因此并排安装多个游戏模式插件只需添加多组世界即可。玩家通过对应的 `/island`（或 `/box`、`/ob` 等）命令选择要玩的模式。要移除某个游戏模式，直接删除对应的插件 jar 文件即可；删除世界文件夹是可选的。

### 如何完全重置 BentoBox / 清除所有岛屿？

停止服务器，删除游戏模式的世界文件夹（例如 `bskyblock_world`、`bskyblock_world_nether`、`bskyblock_world_the_end`），并删除 `plugins/BentoBox/database/Island/` 和 `plugins/BentoBox/database/Players/` 中对应的文件（如果使用 SQL，则删除对应的行）。下次启动时，BentoBox 会重新生成所有内容。

### 如何更改岛屿间距离？

所有游戏模式都有一个岛屿间距离的配置项。在 BSkyBlock 中，该选项名为 `distance-between-islands`，位于 config.yml 文件中：

```
# 岛屿半径（以方块为单位）。（因此岛屿间距为该值的两倍）
  # 每个维度（主世界、地狱和末地）的值相同。
  # 该值在游戏运行中无法更改，如果值不同，插件将无法启动。
  # /!\ BentoBox 目前不支持在游戏中更改此值。如需更改，请完全重置数据库和世界。
  distance-between-islands: 400
```

BSkyBlock 默认值为 400，意味着玩家将相距 800 个方块，玩家的保护区域最大可达 400。

大多数情况下，默认设置足够使用。一旦游戏开始运行，**你无法更改此值**。如果尝试更改，BentoBox 将拒绝启动并在控制台输出如下警告：

```
[14:08:20 ERROR]: [BentoBox] *****************CRITIAL ERROR!******************
[14:08:20 ERROR]: [BentoBox] Island distance mismatch!
World 'bskyblock_world' distance 800 != island range 400!
Island ID in database is BSkyBlock99ea1c15-f5f8-410a-9019-d6b843a5a254.
Island distance in config.yml cannot be changed mid-game! Fix config.yml or clean database.
[14:08:20 ERROR]: [BentoBox] Could not load islands! Disabling BentoBox...
[14:08:20 ERROR]: [BentoBox] *************************************************
```
这是一种保护机制——若更改后强行继续，岛屿可能会相互重叠，导致玩家极度不满！

**但我刚刚建立服务器！如何更改此值并清理数据库？**

以下步骤适用于默认的 JSON 数据库（平面文件）：

1. 停止服务器
2. 将 config.yml 中的岛屿距离值改为所需数值。
3. 如果没有运行其他 BentoBox 游戏，或想重置一切，删除 `plugins/BentoBox/database` 和 `plugins/BentoBox/database_backup` 文件夹
4. 删除游戏模式创建的世界文件夹，BSkyBlock 默认为：`bskyblock_world`、`bskyblock_world_nether`、`bskyblock_world_the_end`
5. 重启服务器。

如果服务器已在运行其他 BentoBox 游戏模式，步骤稍微复杂：
1. 停止服务器
2. 将 config.yml 中的岛屿距离值改为所需数值。
3. 打开 `plugins/BentoBox/database/Island` 文件夹，删除所有以你的游戏模式名称开头的文件，例如 `BSkyBlock99ea1c15-f5f8-410a-9019-d6b843a5a254.json`
4. 删除游戏模式的世界文件夹（BSkyBlock 默认为：`bskyblock_world`、`bskyblock_world_nether`、`bskyblock_world_the_end`）
5. 重启服务器。

如果使用 MySQL 等其他数据库，步骤相同，但需要使用 SQL 命令来删除数据库、表或条目。

### 如何启用地狱传送门相互链接？

BentoBox 1.16 中实现了传送门正确链接的选项。但该选项仅在 server.properties 中启用了 `allow-nether` 且在 bukkit.yml 中启用了 `allow-end` 时才有效。

在游戏模式配置中找到 `create-and-link-portals` 选项并设置为 `true` 以启用传送门链接。

找到 `create-obsidian-platform` 选项并设置为 `true` 以启用正确的末地黑曜石平台（与原版末地相同）。

注意，启用这些选项会开放与原版 Minecraft 相同的无限黑曜石生成漏洞。

### 如何在 Boxed 中禁用结构生成？

在 Boxed 的 `config.yml` 中有一个 `structures` 列表。从该列表中删除条目可防止这些结构在新创建的领地区域中生成。已有领地不受影响。

### 我可以将 Multiverse 与 BentoBox 一起使用吗？

Multiverse 通常可与大多数游戏模式配合使用，但 **Boxed 和 Poseidon 例外**，这两者需要在 `bukkit.yml` 中设置自己的世界生成器。若对这两者使用 Multiverse，世界将无法正确生成。MyWorlds 是一个常用的替代方案。

## 生物、刷怪与实体

### 为什么我的鱼、海豚或鱿鱼只在 y -63 的基岩附近生成？

这是一个 [Mojang 平坦世界 bug](https://github.com/BentoBoxWorld/BentoBox/issues/2593)，影响 Minecraft 1.21.2+：水生生物只在平坦世界底部附近生成。新版 BentoBox 创建的新世界已包含此问题的修复方案。已有世界需要手动对世界的 level data 进行 NBT 编辑——游戏内无法修复。

### 为什么岛屿上根本没有生物生成？

以 `/op` 权限站在岛屿上，查看服务器控制台：

1. BentoBox 会打印出哪个插件（如有）取消了生成事件。如果没有打印信息，说明 Minecraft 根本没有尝试生成——请检查 `bukkit.yml` 中的 `spawn-limits` 和 `gamerule` 设置，以及你的世界插件（Multiverse、MyWorlds 等）和 `/[admin_command]` 设置。
2. 检查游戏模式 `config.yml` 的 `world.spawn-limits` 部分。
3. 对于无法被敌对生物攻击的访客，请查看*访客保护*标志。

## 岛屿：大小、保护与重置

### 如何增加玩家的岛屿大小？

每个岛屿都有一个受保护区域。你可以将保护区域增加到岛屿间距离的值。有三种机制，在某些游戏模式（尤其是 Boxed）中必须选择**其中一种**，因为它们互斥：

- **权限** — 授予 `[gamemode].island.range.<数字>`（例如 `bskyblock.island.range.150`）。权限仅在玩家登录时检查，所以所有者必须重新连接才能生效。如果岛屿所有者更换，岛屿范围将调整为新所有者的权限，若无权限则恢复为默认范围。
- **管理员命令** — `/[admin_command] range set <玩家> <数字>` — 立即生效。
- **进度（仅 Boxed 默认）** — 领地随所有者解锁进度而增大。若要在 Boxed 中改用命令或权限，在 Boxed 配置中设置 `ignore-advancements: true`。

保护范围永远不能超过游戏模式的 `distance-between-islands` 值。请记住，保护范围适用于整个岛屿。

### 为什么我的 Boxed 领地在每次重启后缩回默认大小？

这是进度模式的正常行为：启动时，BentoBox 会根据所有者解锁的进度重新计算领地大小。要么让所有者解锁更多进度，要么在 Boxed 配置中设置 `ignore-advancements: true` 并改用命令/权限。

### 如何防止玩家看到附近的岛屿？

隐藏相邻岛屿所需的 `distance-between-islands` 最小值为：

```
distance-between-islands ≥ max_protection_range + (服务器视距 × 16) / 2
```

例如，最大保护范围为 50（100×100 的岛屿），视距为 11 个区块时：

```
distance-between-islands ≥ 50 + (11 × 16) / 2 = 138
```

`distance-between-islands` 在游戏中途无法更改，需要完全重置（参见[如何更改岛屿间距离？](#如何更改岛屿间距离)）。

### 我可以出售岛屿升级/让玩家付费扩展岛屿吗？

BentoBox 没有内置商店。`#support-en` 的置顶消息中介绍了两种社区方案：(1) 将 [Upgrades 插件](addons/Upgrades/index.md)与 Vault 经济结合使用；(2) 使用任意外部 GUI/商店插件，在购买时授予 `[gamemode].island.range.<数字>` 权限。

### 为什么岛屿边界显示了新大小，但玩家仍然无法在那里建造？

视觉边界显示的是保护范围。如果玩家已获得更高范围的权限但尚未重新登录，边界仍显示旧的半径。让他们重新加入（或使用立即生效的管理员范围命令）即可。

## 团队、合作与访客

### 团队、合作、信任和访问有什么区别？

- **访客** — 任何传送到或走上他人岛屿的玩家。默认情况下，他们无法破坏、放置或与大多数方块交互。
- **合作** — 通过 `/island coop <玩家>` 授予的临时升级。持续到玩家下线（可配置）。合作等级可在*设置 → 保护*中调整。
- **信任** — 通过 `/island trust <玩家>` 授予的持久升级。下线后仍有效。
- **团队成员** — 通过 `/island team invite <玩家>` 授予。被邀请者必须接受，**且在此过程中会失去自己的岛屿**。每个岛屿只有一名所有者；团队成员不是所有者。
- **所有权转让** — `/island team setowner <玩家>` 可转让所有权。

对于以上所有情况，各保护操作所需的确切等级可在岛屿 `设置` GUI 的*保护标志*和*命令等级*选项卡中配置。

### 如何让他人帮我建造而不给他们我的岛屿？

使用**信任**。信任在下线后仍然有效，你可以通过岛屿设置菜单精确配置受信任玩家可以执行哪些操作。

## 占位符

### 如何在聊天/Tab/计分板中显示 BentoBox 占位符？

你需要安装 [PlaceholderAPI](https://www.spigotmc.org/resources/placeholderapi.6245/)，以及一个本身支持 PlaceholderAPI 的聊天/Tab/计分板插件。完整的占位符列表请见[占位符](BentoBox/Placeholders.md)。要验证占位符是否正常工作，运行：

```
/papi parse me %bentobox_island_name%
```

如果返回了一个值，说明占位符本身没有问题，问题出在你的聊天/Tab/计分板插件的配置上。

### 为什么 `%Level_<gamemode>_island_level%` 返回空值？

按顺序检查以下三点：

1. Level 插件已安装并对该游戏模式启用。
2. 玩家至少运行过一次 `/[player_command] level`——默认情况下，等级只有在玩家运行命令时才会计算。（你可以在 Level 插件配置中启用 `calculate-level-on-login` 以在玩家加入时计算。）
3. 由该玩家运行 `/papi parse me %Level_<gamemode>_island_level%` 是否返回一个数字。如果是，问题出在你的聊天/Tab 插件，而非 BentoBox。

## AOneBlock

### 如何在阶段中添加自定义方块（或 ItemsAdder / Oraxen 方块）？

编辑 `plugins/BentoBox/addons/AOneBlock/phases/` 中对应的阶段文件。阶段文件使用旧版简写语法或显式 `block-data` 语法——参见 [AOneBlock 阶段配置文件](gamemodes/AOneBlock/index.md#phase-config-files)中的示例。对于 ItemsAdder / Oraxen 方块，你需要使用方块形式（而非物品形式），且阶段条目必须使用 `block-data` 配合底层命名空间 ID。

### 如何编辑阶段箱子中的战利品？

放置一个箱子，填入想要的物品，然后看着它运行 `/[admin_command] setchest`。箱子的内容（以及任何容器 NBT）将被写入阶段文件。

### 玩家第一次加入时在世界出生点生成而不是获得岛屿——如何修复？

在 AOneBlock 的 `config.yml` 中，启用*首次登录时创建岛屿*选项。没有此选项，第一次加入的玩家会在服务器出生点落地，需要手动运行 `/island create`。

### 为什么魔法方块在大型生物生成时会清除附近的方块？

这是有意为之的。AOneBlock 会清除生成实体边界框内的方块，防止玩家在魔法方块上方放置立方体来困住它（否则会立即杀死生成的生物）。可以在 AOneBlock 配置中设置 `mobs-clear-blocks: false` 来禁用此行为，但代价是允许该漏洞被利用。

## Level 插件

### 为什么我的等级没有实时更新？

岛屿等级只有在玩家运行 `/[player_command] level` 时才会计算，如果启用了 Level 插件配置中的 `calculate-level-on-login` 则在登录时计算。没有持续追踪——每次方块变化都重新计算整个岛屿会消耗过多资源。

### 为什么我的自定义 Oraxen / ItemsAdder / 自定义方块没有被计入？

Level 插件只计算其 `blockconfig.yml` 中列出的方块。来自物品添加插件的自定义方块必须在那里明确添加并指定你希望它们得分的值。如果条目缺失，该方块会回退到其底层基础方块的值（或者如果该方块也未列出，则为零）。

### 我应该在 Boxed 中使用 Level 插件吗？

通常不建议——Boxed 世界预填充了地形，所以岛屿的"等级"主要由底层区块而非玩家建造的内容决定。Level 插件应用于虚空类游戏模式（BSkyBlock、AOneBlock、AcidIsland），在那里它才真正反映玩家的努力成果。

## Challenges 插件

### 我运行了 `/[admin_command] challenges`，菜单是空的——如何获取默认挑战？

打开菜单，点击*资料库*，选择一套默认挑战（例如 BSkyBlock 的"default"），然后在提示时在聊天中输入 `confirm` 确认。默认挑战已与插件捆绑，但不会自动加载——每个游戏模式需要手动导入一次。

### 我可以从不同的世界/主世界运行挑战吗？

不可以。挑战绑定到创建它们时所在的游戏模式世界。如果你想在主世界中实现任务类内容，需要使用单独的任务插件。

## 数据库与存储

### 需要哪个版本的数据库？

最低要求版本：

* **MySQL** 5.7 或更高
* **MariaDB** 10.2.3 或更高
* **MongoDB** 3.6 或更高
* **SQLite** 3.28 或更高
* **PostgreSQL** 始终建议使用最新版本

### 我的 BentoBox 世界文件夹非常大——如何缩减？

两大占用空间的因素是：(1) 从未回来的玩家生成的区块；(2) 重置后遗留的旧岛屿区域。回收空间的方法：

- **BentoBox 3.15.0+：** 使用 `/[admin_command] purge <days>` ——该命令现在可以一步完成识别废弃岛屿*并*删除其区域文件。对于软删除的岛屿（在重置或 `/admin delete` 后标记的岛屿），运行 `/[admin_command] purge deleted` 回收其区域文件。清除后重启服务器以清空 Paper 的区块缓存。
- **旧版 BentoBox：** 使用 `/[admin_command] purge <days>` 标记岛屿，然后运行 `/[admin_command] purge regions` 删除区域文件。
- **操作前务必备份世界文件夹。**
- 对于非常旧的世界，可以使用 Regionerator 等第三方工具裁剪未使用的区块。

### MariaDB 和 MySQL 有区别吗？

有。在 BentoBox 的 `config.yml` 中必须设置正确的 `database` 类型：如果你的服务器是 MariaDB，选 `MARIADB`；如果是 MySQL，选 `MYSQL`。两者的传输协议相似，但 JDBC 驱动程序和保留字列表差异足以导致混用时在启动时出现连接或查询错误。

### 如何从 JSON 迁移到 MySQL/MariaDB？

参见[数据库转换](BentoBox/Database-transition.md)。简要步骤：停止服务器，在 `config.yml` 中更改数据库类型，启动服务器并启用 `database-transition`——BentoBox 会在启动时将所有记录复制到新数据库，然后禁用 `database-transition` 并重启。

## 自定义：语言、颜色与蓝图

### 如何制作自定义岛屿？

你所说的是我们的**内置原理图格式**，我们称之为**_蓝图_**。
[蓝图页面](BentoBox/Blueprints.md)提供了所有开始使用蓝图的相关信息，以及一些提示和技巧。
你也可以看看[这个视频](https://youtu.be/4gvaG89uxAs)，虽然有些过时，但可能帮助你在几分钟内创建第一个蓝图。

### 如何更改语言字符串/消息？

语言文件位于 `plugins/BentoBox/locales/`（BentoBox 核心）和 `plugins/BentoBox/addons/<插件名>/locales/`（每个插件）下。编辑对应的 `<语言>.yml` 文件。如果只想使用一种语言，在 BentoBox 的 `config.yml` 中设置 `default-language` 并移除玩家切换语言的权限。

### 如何更改 `[BentoBox]` 聊天前缀？

在 `plugins/BentoBox/locales/en-US.yml`（或你使用的语言文件）中找到 `prefixes:` 下的条目。每个插件也可能在其语言文件中有自己的前缀。

### 如何在消息中使用十六进制（RGB）颜色？

使用 `&#RRGGBB`，例如 `&#ff8800Hello` 显示橙色。这在 BentoBox 接受颜色代码的任何地方均有效。注意，某些外部聊天格式化插件可能需要它们自己的十六进制语法——BentoBox 无法控制这一点。

### 我在哪里可以帮助将 BentoBox 翻译成我的语言？

[https://download.bentobox.world/translate.html](https://download.bentobox.world/translate.html) — 翻译通过 Crowdin 管理，并自动拉取到发行版本中。

## 杂项

### 为什么我的魔法鹅卵石生成器什么都不做？

玩家必须先通过 `/[player_command] generator` **激活**一个生成器，并从 GUI 中选择一个。仅仅放置熔岩和水而不激活生成器只会产生原版鹅卵石。

### 如何预先生成岛屿以便玩家无需等待？

没有内置的预生成器，但你可以编写 `/[admin_command] register <虚拟玩家>` 脚本来提前创建岛屿。对于区块预生成，可以使用 Chunky 等服务器端工具。

## API 与插件开发

### 如何开始为 BentoBox 编写插件？有 API 吗？

是的，绝对有 API。
编写插件与编写普通插件非常相似，只是有更多 API 可用，涵盖团队、保护、命令、面板和粘贴等功能。

按照[本教程](Tutorials/api/Create-an-addon.md)来创建你的第一个插件！

## 较少见/旧版问题

本节的问题现在很少出现，但保留答案供仍然遇到这些问题的服务器参考。

### 我的世界中正在生成超平坦区块

*相关问题：*
[BentoBox#1212](https://github.com/BentoBoxWorld/BentoBox/issues/1232),
[BSkyBlock#247](https://github.com/BentoBoxWorld/BSkyBlock/issues/247)。

![超平坦世界](https://static.planetminecraft.com/files/resource_media/screenshot/1215/2012-04-15_205556_2000620.jpg)
*超平坦世界。（图片来源：[1213videogamer on PlanetMinecraft](https://www.planetminecraft.com/member/1213videogamer/)）。*

如果你开始看到世界中生成超平坦区块，这是因为世界生成器不再为该世界工作。原因有几种，按可能性排列如下。

**我们强烈建议你恢复到发生此情况之前的备份**。
虽然我们提供了在没有备份时的恢复指导，但**不保证其有效性**。此外，这些解决方案**旨在尽可能解决问题，但会忽略对性能或玩家岛屿的影响**。请知情后再使用。

作为临时修复，管理员设置控制台中有一个设置可以删除超平坦区块。这是修复损害的主要工具，但除非修复根本原因，否则只会造成严重卡顿而无法彻底解决。

无论如何，**请立即停止服务器以防止对世界造成进一步损害**。

#### 原因

##### BentoBox 或游戏模式插件不再运行

**为什么？**

BentoBox 或游戏模式插件未在服务器上启用。
这可能发生在你将 BentoBox 或游戏模式插件更新到与你的服务器或某个插件不兼容的版本时。

**解决方案**

调查为什么 BentoBox 或游戏模式插件不再启用。
阅读日志以找到启动时的错误。
尝试每次添加一个插件来启动服务器，找出哪个插件导致了问题。

##### `bukkit.yml` 中没有为此世界设置生成器

**为什么？**

这通常是问题所在。
在将服务器的默认世界设置为游戏模式插件的世界时，忘记在 `bukkit.yml` 文件中为该世界指定正确的生成器。

**解决方案**

确保你彻底遵循了[本教程](BentoBox/Set-a-BentoBox-world-as-the-server-default-world.md)的每一步。

##### 游戏模式配置中的 `use-own-generator` 选项设置为 `true`

**为什么？**

这是一个常见错误。

用户往往误解此选项，以为它可以激活"魔法"鹅卵石生成器（但[那是一个插件](addons/MagicCobblestoneGenerator/index.md)！）。
这不是该选项的设计目的，配置文件中关于此选项的注释已清楚说明：

```yaml
# 使用你自己的世界生成器。
# 在这种情况下，插件不会生成任何东西。
# 如果使用，你必须在 bukkit.yml 文件中指定世界名称和生成器。
# 参见 https://bukkit.gamepedia.com/Bukkit.yml
use-own-generator: false
```

如果你忘记在 `bukkit.yml` 文件中指定世界名称和对应的插件名称作为生成器，也会发生此问题。

**解决方案**

如果你不打算使用外部插件生成世界，将此选项设置回 `false`。

否则，确保你在 `bukkit.yml` 文件中正确指定了世界名称和对应的插件名称作为生成器。

##### 另一个插件试图控制此世界的生成器

**为什么？**

虽然非常罕见，但仍可能发生。

一些插件，尤其是世界管理类插件（如 Multiverse），往往提供可以覆盖我们世界生成器的设置。

**解决方案**

检查所有插件，找出最可能导致问题的那个。
首先调查与世界交互的世界管理插件或自定义插件。
向其开发者报告问题，或修复涉及的配置文件。

##### BentoBox 或游戏模式插件中存在 bug

**为什么？**

*哎呀！*

如今这种情况极为罕见，但出于某些原因仍可能发生。

**解决方案**

确认这确实是 BentoBox 相关的 bug：从服务器逐一移除所有插件，直到只剩 BentoBox。

如果问题不再出现，说明是另一个插件导致的。
在这种情况下，请参阅[本节](https://bentobox-world.readthedocs.io/en/latest/FAQ/#another-plugin-is-trying-to-control-the-generator-of-this-world)。

如果问题仍然存在，说明这是一个 BentoBox bug。
请[在我们的 bug 追踪器上报告](https://github.com/BentoBoxWorld/BentoBox/issues)。

#### 如何清理超平坦区块？

如果有备份，使用备份将服务器世界和 BentoBox 数据库恢复到之前的状态。

如果没有备份，登录服务器并使用 `/[admin-command] settings` 命令打开管理员设置面板。
找到"*清理超平坦*"标志并切换开启。
根据你的设置、语言和运行的 BentoBox 版本，名称、图标或描述可能有所不同，但我们相信你一定能找到该标志！

![图片](https://user-images.githubusercontent.com/20014332/77770414-8256c380-7045-11ea-8ab6-8efe31d6fb87.png)
*BSkyBlock 管理员设置面板中的清理超平坦标志*。

该标志会**随时间慢慢再生世界中的超平坦区块**。
这发生在区块被加载时，所以你可能需要传送到这些区块强制再生，或者让该标志开启数天。
**不要忘记在某个时候关闭该标志！**
它相当占用资源……

### 玩家创建岛屿时服务器延迟！

粘贴岛屿或生成区块是此问题的主要原因。

首先，粘贴速度可能对你的服务器来说太快了。
尝试降低它。
在 BentoBox 的 `config.yml` 中找到以下设置：

```yaml
# 粘贴蓝图时每个 tick 粘贴的方块数。
# 较小的值有助于减少明显卡顿，但会使粘贴花费稍长时间。
# 较大的值会使粘贴花费更少时间，但这种优势很快就会被
# 必须加载的区块数量所抵消，通常会导致服务器卡死。
paste-speed: 64
```

如果你在运行 timings，`BlueprintPaster` 任务理想状态是耗时较长但占用每 tick 时间的百分比较低。

如果服务器在粘贴岛屿时仍然挣扎，则说明它在生成区块时遇到困难。
作为插件我们对此几乎无能为力，但以下是一些缓解措施：

* 尝试减少游戏模式配置文件中的"岛屿间距离"设置。
较低的值意味着需要生成更少的区块。
这需要完全重置世界和数据库。
* 使用 Paper 作为服务器软件。
Paper 支持异步区块生成。
* 预生成世界。
尤其是对于生成器资源密集的游戏模式，如 CaveBlock 或 SkyGrid。

### 我无法在岛屿上放置树苗！

*相关问题：*
[BentoBox#277](https://github.com/BentoBoxWorld/BentoBox/issues/277)。

如果没有向玩家显示任何无法放置树苗的消息，则说明 BentoBox **不是**此问题的原因。

如果你在服务器上使用 **GriefPrevention**，该插件有一个[配置选项](https://github.com/TechFortress/GriefPrevention/wiki/Setup-and-Configuration#preventing-tree-grief)可防止玩家放置所谓的"天空树"。

## 来源

上述来自 Discord 的条目整理自 `#support-en` 频道，时间范围为 2025 年 1 月至 2026 年 4 月。各主题示例讨论帖（每个主题一条，供参考）：

- 版本与兼容性 — [discord 讨论帖](https://discord.com/channels/272499714048524288/310623455462686720/1490517535152410745)
- 世界与生成 — [discord 讨论帖](https://discord.com/channels/272499714048524288/310623455462686720/1488648048589672488)
- 生物刷怪 — [discord 讨论帖](https://discord.com/channels/272499714048524288/310623455462686720/1475550306799583316)
- 权限与等级 — [discord 讨论帖](https://discord.com/channels/272499714048524288/310623455462686720/1480457734842220566)
- 岛屿创建与重置 — [discord 讨论帖](https://discord.com/channels/272499714048524288/310623455462686720/1468577190126948455)
- 岛屿大小与保护 — [discord 讨论帖](https://discord.com/channels/272499714048524288/310623455462686720/1471174102957031506)
- 团队与合作 — [discord 讨论帖](https://discord.com/channels/272499714048524288/310623455462686720/1467986323137757357)
- 占位符 — [discord 讨论帖](https://discord.com/channels/272499714048524288/310623455462686720/1465642012341698713)
- Level 插件 — [discord 讨论帖](https://discord.com/channels/272499714048524288/310623455462686720/1459181292175360162)
- AOneBlock — [discord 讨论帖](https://discord.com/channels/272499714048524288/310623455462686720/1466486743287988346)
- Challenges — [discord 讨论帖](https://discord.com/channels/272499714048524288/310623455462686720/1426655803473133795)
- 数据库与存储 — [discord 讨论帖](https://discord.com/channels/272499714048524288/310623455462686720/1461304120668323910)
- 本地化 — [discord 讨论帖](https://discord.com/channels/272499714048524288/310623455462686720/1482135823947272203)
- Border 插件 — [discord 讨论帖](https://discord.com/channels/272499714048524288/310623455462686720/1462044129448951872)
- Bank 插件 — [discord 讨论帖](https://discord.com/channels/272499714048524288/310623455462686720/1440031441995169833)
- BSkyBlock — [discord 讨论帖](https://discord.com/channels/272499714048524288/310623455462686720/1486436566032318474)
- Boxed — [discord 讨论帖](https://discord.com/channels/272499714048524288/310623455462686720/1415368394374647948)
- 错误与崩溃 — [discord 讨论帖](https://discord.com/channels/272499714048524288/310623455462686720/1441184039175327757)
