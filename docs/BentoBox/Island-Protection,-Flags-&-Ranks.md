# 岛屿保护、标志和等级

[TOC]

## 简介
玩家（甚至环境，如实体、活塞等）与岛屿的交互由一组**标志**控制，这些标志**确定*谁*或*什么*可以在岛上做什么**。这些标志主要由 BentoBox 处理和提供，但附加组件（例如 [Greenhouses](https://github.com/BentoBoxWorld/Greenhouses)）可以添加自己的标志。

在[此处](/en/latest/BentoBox/Flags)查看标志列表。

## 设置面板

**设置面板**是岛主可以编辑岛屿标志配置的 GUI。其他玩家，包括岛屿成员，只能查看它们。

可以使用以下指令打开此 GUI：`/[player_command] settings`（需要以下权限：`[gamemode].island.settings`）。

![设置面板的默认视图](https://user-images.githubusercontent.com/20014332/80591492-1689c100-8a1e-11ea-9a59-c55f35ab6ad9.png)

*设置面板的默认视图。*

管理员可以使用管理员设置指令更改玩家岛屿的设置：`/[admin_command] settings <player_name>`

### 保护选项卡

**保护选项卡**是打开设置面板时显示的选项卡。它包括**保护标志**。

**保护标志**是可以按[等级](#ranks)设置的标志。通过**左键**或**右键**单击标志的图标，岛主将在各个等级之间循环，以便根据玩家的等级允许或禁止标志所控制的交互。

![保护标志示例](https://user-images.githubusercontent.com/20014332/62974085-b31c1c80-be17-11e9-8b27-2fd4bf54ae87.png)

*保护标志示例。*

默认情况下，大多数保护标志设置为仅允许岛屿成员（或以上等级）进行交互。但是，有些最初也允许访客。请参阅[游戏模式的 config.yml]。

![默认情况下允许访客进行交互的保护标志示例](https://user-images.githubusercontent.com/20014332/62974359-553c0480-be18-11e9-8679-0033fd8bf8bd.png)

*默认情况下允许访客进行交互的保护标志示例。*

管理员可以使用管理员设置指令设置岛屿边界外的保护工作方式：`/[admin_command] settings`

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

### 自定义设置面板 { #customizing-the-settings-panel }

!!! new "BentoBox 3.23.0 新增"
    设置面板由模板文件布局，与其他[可自定义 GUI](/en/latest/Tutorials/generic/Customizable-GUI/) 相同。

设置面板的布局来自 `plugins/BentoBox/panels/settings_panel.yml`，BentoBox 首次启动时会生成该文件。游戏模式附属可以在自己的 `panels` 文件夹中提供自己的副本（例如 `plugins/BentoBox/addons/BSkyBlock/panels/settings_panel.yml`），该游戏模式将改用这个副本。默认文件完全还原了之前的面板外观，因此在你编辑它之前不会有任何变化。如果文件无法读取，BentoBox 会记录错误并显示内置面板。

每个按钮都通过 `data.type` 放置：

| 类型 | 显示内容 |
| --- | --- |
| `TAB` | 选项卡按钮。`data.tab` 为 `PROTECTION`、`SETTING` 或 `WORLD_PROTECTION`（玩家不在岛屿上时看到的只读视图）。不适用的选项卡不会显示，而是改用按钮的 `fallback`。 |
| `FLAG` | 分页标志列表中的一个格子。每页想显示多少个标志就放置多少个。使用 `data.flag: <FLAG_ID>` 时，该格子始终显示该标志，并且该标志会从分页列表中移出；锁定图标和更改设置图标就是这样放置的。 |
| `MODE` | 显示模式切换。可以在 `data` 中用 `basic-icon`、`advanced-icon` 和 `expert-icon` 为每种模式设置图标。 |
| `RESET` | 将所有标志重置为默认值。只有岛主能看到。 |
| `NEXT`、`PREVIOUS` | 翻页。仅在有可跳转的页面时显示。 |

**标题和选项卡名称是分开的。** 面板标题是模板的 `title`，默认为语言条目 `panels.settings.title`，翻译时会替换 `[tab]`（当前显示的选项卡名称）和 `[world_name]`。默认值只有 `[tab]`。每个选项卡按钮都有自己的 `title` 和 `description`，默认为 `protection.panel.PROTECTION.title` 等条目。因此，无论在模板还是语言文件中，都可以为标题和选项卡按钮设置不同的样式。

**描述（lore）布局。** 标志的描述由语言文件中的 `protection.panel.flag-item.description-layout`（保护标志）、`setting-layout`（设置）或 `menu-layout`（打开子面板的标志）构建。从 3.23.0 开始，这些布局可以包含 `[ranks]`（插入保护标志等级列表的位置）和 `[tooltips]`（插入模板中标志按钮 `actions` 工具提示的位置）。没有 `[ranks]` 时，等级列表会像以前一样追加在布局之后；没有 `[tooltips]` 时，工具提示会在一个空行之后追加。要将点击提示移到等级列表下方，请从布局中删除这些提示，把 `[ranks]` 和 `[tooltips]` 放在你想要的位置，并在模板的 `flag_button` 中将提示声明为工具提示。模板中标志按钮自身的 `title` 和 `description` 可以指定另一个语言条目，仅在该面板中用作名称和描述布局。

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

指令 `/[admin_command] switch`（权限 `[gamemode].mod.switch`）切换版主的绕过权限开关。默认情况下绕过权限**激活**（版主正在绕过保护）；运行该指令一次会关闭绕过，所以他们受到保护，如同普通玩家一样，再运行一次会打开。这影响上面的 `mod.bypassprotect` 和 `mod.bypass.*` 权限——它**不会**禁用原始操作员状态。

### 锁定、禁止和驱逐

岛屿锁定、禁止和驱逐有自己的绕过权限，与标志系统无关：

- `[gamemode].mod.bypasslock` ——进入锁定的岛屿。
- `[gamemode].mod.bypassban` ——进入你被禁止的岛屿。
- `[gamemode].mod.bypassexpel` 和 `[gamemode].admin.noexpel` ——无法被驱逐。
- `[gamemode].admin.noban` ——无法被禁止。

任何携带 Bukkit `NPC` 元数据的实体（例如 Citizens NPCs）也被允许通过锁定、禁止、PVP 和无敌访客检查，所以插件 NPC 不会被岛屿保护困住或伤害。

### 冷却时间和延迟

指令冷却时间和传送热身延迟可以跳过：

- `[gamemode].mod.bypasscooldowns` ——忽略指令冷却时间。
- `[gamemode].mod.bypassdelays` ——在延迟传送指令上跳过移动热身延迟。

### 永不受保护的

- **非 BentoBox 世界。** 保护仅存在于游戏模式世界（及其链接的标准下界/末地）。服务器的默认世界和其他插件的世界永远不会被检查。
- **"荒野"。** 当玩家在游戏模式世界内但不在任何岛屿上时，应用世界的默认标志设置而不是岛屿的——这些在下面的**管理员设置面板**中配置（或游戏模式的 `config.yml`）。
- **被删除的岛屿是异常的：** 在待删除的岛屿上，默认情况下没有任何允许——除了操作员和持有 `mod.bypassprotect` / `mod.bypass.<FLAG_ID>.everywhere` 权限的持有者，其绕过会首先检查。

## 管理员设置面板

**管理员设置面板**通过 `/[admin_command] settings`（不带任何参数）访问。它包含三个选项卡：

!!! new "BentoBox 3.23.0 新增"
    管理员设置面板由 `plugins/BentoBox/panels/admin_settings_panel.yml` 布局，方式与[玩家的设置面板](#customizing-the-settings-panel)相同。其选项卡类型为 `WORLD_SETTING`、`WORLD_DEFAULTS` 和 `ISLAND_DEFAULTS`；后两者需要 `[gamemode].admin.set-world-defaults` 权限，没有该权限时会被隐藏。同一个文件也用于布局 `/[admin_command] settings <player_name>`：每个世界选项卡都将一个岛屿选项卡（`PROTECTION`、`SETTING`）指定为其 `fallback`，当存在岛屿时显示该选项卡。

### 世界设置

切换应用于整个游戏世界的世界级设置标志。

### 世界默认保护

控制岛屿边界外活跃的保护标志（即对荒野中访客的保护）。

### 岛屿默认值

!!! new "BentoBox 3.14.0 新增"
    **岛屿默认值**选项卡是管理员设置面板中的新选项卡，允许管理员为**新创建的岛屿**设置应用的默认标志值。

之前，这些默认值只能在游戏模式的 `config.yml` 中更改。现在可以通过打开 `/[admin_command] settings` 并导航到**岛屿默认值**选项卡（第 3 个选项卡）在游戏中直接更改。

每个保护标志都显示其当前的默认等级——单击可在等级阶梯中循环。每个岛屿设置标志显示其当前的默认 `true`/`false` 状态——单击可切换。更改会立即保存到世界设置，对**创建更改后的所有新岛屿**生效。已有岛屿不受影响。