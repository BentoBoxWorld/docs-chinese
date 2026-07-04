# 岛屿保护、标志和等级

[TOC]

## 简介
玩家（甚至环境，如实体、活塞等）与岛屿的交互由一组**标志**控制，这些标志**确定*谁*或*什么*可以在岛上做什么**。这些标志主要由 BentoBox 处理和提供，但附加组件（例如 [Greenhouses](https://github.com/BentoBoxWorld/Greenhouses)）可以添加自己的标志。

在[此处](/en/latest/BentoBox/Flags)查看标志列表。

## 设置面板

**设置面板**是岛主可以编辑岛屿标志配置的 GUI。其他玩家，包括岛屿成员，只能查看它们。

可以使用以下命令打开此 GUI：`/[player_command] settings`（需要以下权限：`[gamemode].island.settings`）。

![设置面板的默认视图](https://user-images.githubusercontent.com/20014332/80591492-1689c100-8a1e-11ea-9a59-c55f35ab6ad9.png)

*设置面板的默认视图。*

管理员可以使用管理员设置命令更改玩家岛屿的设置：`/[admin_command] settings <player_name>`

### 保护选项卡

**保护选项卡**是打开设置面板时显示的选项卡。它包括**保护标志**。

**保护标志**是可以按[等级](#ranks)设置的标志。通过**左键**或**右键**单击标志的图标，岛主将在各个等级之间循环，以便根据玩家的等级允许或禁止标志所控制的交互。

![保护标志示例](https://user-images.githubusercontent.com/20014332/62974085-b31c1c80-be17-11e9-8b27-2fd4bf54ae87.png)

*保护标志示例。*

默认情况下，大多数保护标志设置为仅允许岛屿成员（或以上等级）进行交互。但是，有些最初也允许访客。请参阅[游戏模式的 config.yml]。

![默认情况下允许访客进行交互的保护标志示例](https://user-images.githubusercontent.com/20014332/62974359-553c0480-be18-11e9-8679-0033fd8bf8bd.png)

*默认情况下允许访客进行交互的保护标志示例。*

管理员可以使用管理员设置命令设置岛屿边界外的保护工作方式：`/[admin_command] settings`

### 设置选项卡

### 显示模式

从 [BentoBox 1.6.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/1.6.0) 开始，可以在设置面板中显示各种数量的标志，具体取决于**显示模式**。
它可以是 `BASIC`、`ADVANCED` 或 `EXPERT`。
可以通过单击设置面板右上角的金锭更改显示模式。

![更改显示模式](https://user-images.githubusercontent.com/20014332/80592558-f0652080-8a1f-11ea-9b7a-eaf3d585b753.png)

`BASIC` 是默认的显示模式，具有我们认为对管理岛屿至关重要的标志。

![基本保护标志](https://user-images.githubusercontent.com/20014332/80592424-b98f0a80-8a1f-11ea-94f5-3b2246b6ae61.png)

`ADVANCED` 具有更多标志，以允许进一步自定义岛屿。

![高级保护标志](https://user-images.githubusercontent.com/20014332/80592698-24d8dc80-8a20-11ea-93d5-3b1b8dbcd18d.png)

`EXPERT` 具有所有可用的标志。有太多标志以至于需要额外的页面。

![专家保护标志](https://user-images.githubusercontent.com/20014332/80592793-4df96d00-8a20-11ea-891e-8833578642e4.png)

### 隐藏标志

从 [BentoBox 1.4.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/1.4.0) 开始，管理员可以通过打开设置面板并在要隐藏的标志图标上++shift+左键++来隐藏 GUI 中的标志。
这将为图标应用"消失诅咒"附魔，并将导致相应的标志对玩家隐藏。
管理员可以通过重复相同的过程重新显示标志。

![默认标志](https://user-images.githubusercontent.com/20014332/80591609-45a03280-8a1e-11ea-9e37-4725d62cdb3c.png)

*玩家查看允许显示的所有基本标志。*

![消失诅咒](https://user-images.githubusercontent.com/20014332/80591692-6799b500-8a1e-11ea-9ab8-e076f47d2220.png)

*将"消失诅咒"应用于其中一个标志。*

![一堆隐藏的标志](https://user-images.githubusercontent.com/20014332/80591757-839d5680-8a1e-11ea-8864-83b09252a7b9.png)

*玩家查看基本标志，"活板门"标志被隐藏。*

## 等级

TODO.

* BANNED: -1（部分未使用）
* VISITOR: 0
* COOP: 200
* TRUSTED: 400
* MEMBER: 500
* SUB-OWNER: 900
* OWNER: 1000
* MOD: 5000（未使用）
* ADMIN: 10000（未使用）

## 绕过保护

保护标志仅在 BentoBox 游戏世界中强制执行，并且仅针对那些没有合法方式通过它们的玩家。有几种方式可以绕过保护——有些是有意的（岛屿等级），有些是给工作人员的（操作员状态和版主权限），还有些是结构性的（世界或标志类型）。

!!! tip
    下面权限中的 `[gamemode]` 是游戏模式的小写名称。对于 BSkyBlock，节点以 `bskyblock.mod…` 开头；对于 AcidIsland，则是 `acidisland.mod…`，以此类推。

### 岛屿等级——设计的方式

绕过保护标志的正常、设计的方式是在岛屿上拥有足够高的**等级**。每个保护标志都有一个所需的等级，任何等级大于或等于它的成员都可以执行该操作。这就是为什么所有者可以建造而访客不能——这不是真正的绕过，只是标志按配置工作。请参阅上面的[等级](#ranks)列表。

### 操作员

服务器操作员（`/op`）是最广泛的绕过。操作员通过 BentoBox 世界中的**每个保护标志**，可以进入锁定和被禁的岛屿，并且免受禁止和驱逐。

两个重要的注意事项：

- **操作员不绕过岛屿设置标志。** `SETTING` 类型的标志（岛屿切换，例如*允许 PVP*、*刷怪生成*等）在操作员检查之前被评估，所以操作员与任何其他玩家一样受到它们的约束。操作员状态仅覆盖*保护*标志。
- **管理员切换无法完全在玩家自己的岛屿上"撤销操作员"。** 即使切换打开（见下文），操作员仍然被允许在一个岛屿上，因为等级检查将操作员状态视为始终允许。要测试保护作为真正的非操作员，请移除操作员状态。

### 版主绕过权限

对于不应该是完全操作员的工作人员，保护可以用权限绕过。这些由管理员切换控制（见下文），所以版主可以切换自己的绕过以体验普通玩家会经历的世界。

- `[gamemode].mod.bypassprotect` ——绕过**所有**保护标志，在世界各地。
- `[gamemode].mod.bypass.<FLAG_ID>.everywhere` ——绕过**一个**命名标志（例如 `BREAK_BLOCKS`）在世界各地。
- `[gamemode].mod.bypass.<FLAG_ID>.island` ——绕过**一个**命名标志，但仅在玩家在岛屿上受阻的地方。

### 管理员"切换"——作为普通玩家测试

命令 `/[admin_command] switch`（权限 `[gamemode].mod.switch`）切换版主的绕过权限开关。默认情况下绕过权限**激活**（版主正在绕过保护）；运行该命令一次会关闭绕过，所以他们受到保护，如同普通玩家一样，再运行一次会打开。这影响上面的 `mod.bypassprotect` 和 `mod.bypass.*` 权限——它**不会**禁用原始操作员状态。

### 锁定、禁止和驱逐

岛屿锁定、禁止和驱逐有自己的绕过权限，与标志系统无关：

- `[gamemode].mod.bypasslock` ——进入锁定的岛屿。
- `[gamemode].mod.bypassban` ——进入你被禁止的岛屿。
- `[gamemode].mod.bypassexpel` 和 `[gamemode].admin.noexpel` ——无法被驱逐。
- `[gamemode].admin.noban` ——无法被禁止。

任何携带 Bukkit `NPC` 元数据的实体（例如 Citizens NPCs）也被允许通过锁定、禁止、PVP 和无敌访客检查，所以插件 NPC 不会被岛屿保护困住或伤害。

### 冷却时间和延迟

命令冷却时间和传送热身延迟可以跳过：

- `[gamemode].mod.bypasscooldowns` ——忽略命令冷却时间。
- `[gamemode].mod.bypassdelays` ——在延迟传送命令上跳过移动热身延迟。

### 永不受保护的

- **非 BentoBox 世界。** 保护仅存在于游戏模式世界（及其链接的标准下界/末地）。服务器的默认世界和其他插件的世界永远不会被检查。
- **"荒野"。** 当玩家在游戏模式世界内但不在任何岛屿上时，应用世界的默认标志设置而不是岛屿的——这些在下面的**管理员设置面板**中配置（或游戏模式的 `config.yml`）。
- **被删除的岛屿是异常的：** 在待删除的岛屿上，默认情况下没有任何允许——除了操作员和持有 `mod.bypassprotect` / `mod.bypass.<FLAG_ID>.everywhere` 权限的持有者，其绕过会首先检查。

## 管理员设置面板

### 世界设置

### 世界默认保护