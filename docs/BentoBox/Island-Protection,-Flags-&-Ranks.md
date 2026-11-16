# 岛屿保护、标志和等级 { #island-protection-flags-ranks }

[TOC]

## 简介 { #introduction }

玩家（或环境，如活塞、生物、火焰、爆炸）在 BentoBox 游戏世界中的一切活动都由**标志**控制。每个标志涵盖一种操作，例如破坏方块、打开箱子或伤害动物。大多数标志来自 BentoBox。[Greenhouses](https://github.com/BentoBoxWorld/Greenhouses) 等附属可以添加更多标志。

请查看[标志列表](Flags.md)以了解每个标志、其图标和默认值。

有三种类型的标志：

| 类型 | 控制内容 | 谁改变它 |
| --- | --- | --- |
| **保护标志** | 哪个[等级](#ranks)可以执行操作，例如*破坏方块*。在岛屿上是等级。在岛屿外对所有人打开或关闭。 | 岛屿所有者在自己的岛屿上。管理员控制世界和新岛屿。 |
| **设置标志** | 整个岛屿的开/关开关，例如*允许PVP*或*动物生成*。 | 岛屿所有者。 |
| **世界设置** | 整个游戏世界的开关，例如*爬行怪爆炸*。 | 仅管理员。 |

### 在岛屿上、在岛屿外和新岛屿 { #on-an-island-off-an-island-and-new-islands }

最常见的混淆是一个保护标志可以有**三个不同的值**，取决于玩家站在哪里和指的是哪个岛屿：

| 问题 | 在哪里设置 | 面板选项卡 |
| --- | --- | --- |
| **在这个岛屿上**谁可以做这个操作？ | 该岛屿的设置 | `/[player_command] settings` → **保护** |
| **在这个世界的任何岛屿外**任何人可以做什么？ | 世界的保护标志（游戏模式的 `config.yml` 中的 `world.flags`） | `/[admin_command] settings` → **世界保护** |
| **新岛屿**将从什么等级开始？ | 游戏模式的 `config.yml` 中的 `world.default-island-flags` | `/[admin_command] settings` → **岛屿默认值** |

改变其中一个永远不会改变其他的。特别是，**岛屿默认值对岛屿外没有影响**，**世界保护对岛屿没有影响**。

### 岛屿的边界 { #where-an-island-ends }

岛屿的保护不覆盖其整个网格方块。岛屿彼此相隔 `distance-between-islands`，但每个岛屿仅在其**保护范围**内受到保护，这是从岛屿中心在各个方向延伸 `protection-range` 个方块的正方形。可以通过 `/[admin_command] range` 或 `[gamemode].island.range.<number>` 权限为每个岛屿提高范围。

保护范围外的任何地方都算作**岛屿外**，即使它在岛屿的网格方块内。这包括岛屿之间的虚空、世界出生点周围的区域（如果它不是岛屿）以及 Boxed 等游戏模式中的荒野。在岛屿外，[世界保护](#world-protections)适用。

## 等级 { #ranks }

每个玩家在每个岛屿上都有一个等级：所有者、成员、访客等。保护标志设置**允许**执行操作的**最低等级**。任何处于该等级或更高等级的人都被允许。等级是数字，所以更高意味着更可信：

| 等级 | 值 | 谁拥有 |
| --- | --- | --- |
| 被禁止 | -1 | 被禁止进入岛屿的玩家。他们无法进入。 |
| 访客 | 0 | 不是岛屿一部分的任何人。 |
| 合作 | 200 | 使用 `/[player_command] team coop` 添加的玩家。当每个队伍成员都离线时移除。 |
| 信任 | 400 | 使用 `/[player_command] team trust` 添加的玩家。在登录间隔保留。 |
| 成员 | 500 | 队伍成员。 |
| 副所有者 | 900 | 用 `/[player_command] team promote` 晋升的队伍成员。 |
| 所有者 | 1000 | 岛屿所有者。 |
| 版主 | 5000 | 不给玩家。保留。 |
| 管理员 | 10000 | 不给玩家。保留。 |

因此，设置为*成员*的标志让成员、副所有者和所有者执行操作，但不让信任的玩家、合作者或访客执行。设置为*访客*的标志让所有人都执行。

附属可以在这些等级之间注册更多等级。

管理员可以使用 `/[admin_command] getrank <player>` 和 `/[admin_command] setrank <player> <rank>` 查看或更改玩家的等级。

## 岛屿设置面板 { #island-settings-panel }

**设置面板**是岛屿所有者配置其岛屿的地方。使用 `/[player_command] settings`（权限 `[gamemode].island.settings`）打开它。岛屿上的每个人都可以查看它。只有所有者可以更改它，以及所有者通过**更改设置**标志（工作台、顶行）允许的任何等级。

![设置面板的默认视图](https://user-images.githubusercontent.com/20014332/80591492-1689c100-8a1e-11ea-9a59-c55f35ab6ad9.png)

*设置面板的默认视图。*

该面板显示玩家站在其区域内的岛屿，或者如果他们在其他地方则显示他们自己的岛屿。管理员可以使用 `/[admin_command] settings <player_name>` 打开任何玩家的岛屿。

### 保护选项卡 { #protection-tab }

**保护**选项卡首先显示并列出岛屿的**保护标志**。

**左键单击**标志以提高其所需的等级，**右键单击**以降低。说明列出等级并突出显示当前等级。超过*所有者*会环绕到*访客*，反之亦然。

![保护标志示例](https://user-images.githubusercontent.com/20014332/62974085-b31c1c80-be17-11e9-8b27-2fd4bf54ae87.png)

*保护标志示例。*

新岛屿以[岛屿默认值](#island-defaults)选项卡上设置的等级开始。大多数标志以*成员*开始，所以访客可以看但不能摸。少数几个开始较低，所以访客可以使用它们。例如，*锁定*以*访客*开始，这意味着岛屿对访客开放。

![允许访客进行交互的保护标志示例。](https://user-images.githubusercontent.com/20014332/62974359-553c0480-be18-11e9-8679-0033fd8bf8bd.png)

*允许访客进行交互的保护标志示例。*

### 设置选项卡 { #settings-tab }

**设置**选项卡列出岛屿的**设置标志**：整个岛屿的开/关开关，例如 PVP、火焰蔓延、树叶腐烂和生物生成。单击设置以切换它。

每个设置还需要权限 `[gamemode].settings.<FLAG_ID>`（或 `[gamemode].settings.*`）。这让服务器可以完全从玩家那里夺走设置，例如阻止他们关闭 PVP。某些设置（例如 PVP）在更改之间有冷却时间。

该选项卡还有[命令等级](#command-ranks)图标。

### 世界保护视图 { #world-protection-view }

!!! new "在 BentoBox 3.22.0 中添加"

在世界中没有岛屿的玩家，也没有站在另一个岛屿区域内，会看到只读的**世界保护**选项卡。它显示管理员在[世界保护](#world-protections)选项卡上设置的任何人可能在岛屿外做什么。这仅供参考，无法从此处更改。

### 显示模式 { #display-mode }

根据**显示模式**，设置面板显示更多或更少的标志。该模式为 `BASIC`、`ADVANCED` 或 `EXPERT`。通过单击面板右上角的金锭来更改它。

![更改显示模式](https://user-images.githubusercontent.com/20014332/80592558-f0652080-8a1f-11ea-9b7a-eaf3d585b753.png)

`BASIC` 是默认值，显示大多数玩家需要的标志。

![基本保护标志](https://user-images.githubusercontent.com/20014332/80592424-b98f0a80-8a1f-11ea-94f5-3b2246b6ae61.png)

`ADVANCED` 显示更多标志以进行更精细的控制。

![高级保护标志](https://user-images.githubusercontent.com/20014332/80592698-24d8dc80-8a20-11ea-93d5-3b1b8dbcd18d.png)

`EXPERT` 显示每个标志并需要额外的页面。

![专家保护标志](https://user-images.githubusercontent.com/20014332/80592793-4df96d00-8a20-11ea-891e-8833578642e4.png)

!!! new "在 BentoBox 3.23.3 中更改"
    设置面板记住每个玩家最后选择的显示模式，并在下次打开时以该模式打开。一个模式由保护和设置选项卡共享。如果选项卡在所选模式中没有要显示的标志，它会显示下一个模式而不改变玩家的选择。管理员设置面板始终以 `EXPERT` 打开。

### 隐藏标志 { #hide-flags }

操作员可以对玩家隐藏标志：打开设置面板并 ++shift+左键++ 标志的图标。该图标获得"消失诅咒"光泽，玩家不再看到该标志。再做一次以显示它。隐藏的标志存储在游戏模式的 `config.yml` 中的 `world.hidden-flags` 中。

隐藏标志只会将其从面板中删除。该标志保持其当前值并仍然被强制执行。为了确保玩家无法更改标志，请先设置其值，然后隐藏它。

![默认标志](https://user-images.githubusercontent.com/20014332/80591609-45a03280-8a1e-11ea-9e37-4725d62cdb3c.png)

*玩家查看允许显示的所有基本标志。*

![消失诅咒](https://user-images.githubusercontent.com/20014332/80591692-6799b500-8a1e-11ea-9ab8-e076f47d2220.png)

*"消失诅咒"应用于其中一个标志。*

![一堆隐藏的标志](https://user-images.githubusercontent.com/20014332/80591757-839d5680-8a1e-11ea-8864-83b09252a7b9.png)

*玩家查看基本标志，"活板门"标志被隐藏。*

### 自定义设置面板 { #customizing-the-settings-panel }

!!! new "在 BentoBox 3.23.0 中添加"
    设置面板由模板文件布局，就像其他[可自定义 GUI](/en/latest/Tutorials/generic/Customizable-GUI/)一样。

设置面板的布局来自 `plugins/BentoBox/panels/settings_panel.yml`，BentoBox 在首次启动时写入该文件。游戏模式附属可以在其 `panels` 文件夹中提供自己的副本（例如 `plugins/BentoBox/addons/BSkyBlock/panels/settings_panel.yml`），该副本用于该游戏模式。默认文件完全再现了面板之前的样子，所以在你编辑它之前没有任何变化。如果无法读取该文件，BentoBox 会记录错误并显示内置面板。

每个按钮都通过 `data.type` 放置：

| 类型 | 显示内容 |
| --- | --- |
| `TAB` | 选项卡按钮。`data.tab` 是 `PROTECTION`、`SETTING` 或 `WORLD_PROTECTION`（玩家不站在岛屿上时获得的只读视图）。不适用的选项卡不会显示，按钮的 `fallback` 会被使用。 |
| `FLAG` | 分页标志列表中的一个插槽。放置尽可能多的标志，每页尽你所需。使用 `data.flag: <FLAG_ID>` 时，插槽始终显示该标志，标志离开分页列表；这是锁和更改设置图标的放置方式。 |
| `MODE` | 显示模式开关。可以在 `data` 中为每种模式设置图标，使用 `basic-icon`、`advanced-icon` 和 `expert-icon`。 |
| `RESET` | 将每个标志重置为其默认值。只有岛屿所有者看到。 |
| `NEXT`、`PREVIOUS` | 分页。仅在有可翻页时显示。 |

**标题和选项卡名称是分开的。** 面板标题是模板的 `title`，默认为区域条目 `panels.settings.title`，用 `[tab]`（显示的选项卡名称）和 `[world_name]` 翻译。默认只是 `[tab]`。每个选项卡按钮都有自己的 `title` 和 `description`，默认为 `protection.panel.PROTECTION.title` 等条目。所以你可以用一种方式设置标题和选项卡按钮的样式，在模板或区域中都可以。

**说明布局。** 标志的说明从区域中的 `protection.panel.flag-item.description-layout`（保护标志）、`setting-layout`（设置）或 `menu-layout`（打开子面板的标志）构建。截至 3.23.0，这些布局可能包含 `[ranks]`（插入保护标志等级列表的位置）和 `[tooltips]`（插入模板中标志按钮 `actions` 工具提示的位置）。没有 `[ranks]` 时，等级列表像以前一样追加在布局之后；没有 `[tooltips]` 时，任何工具提示都在空行后追加。要将点击提示移到等级列表下方，请从布局中删除它们，在所需位置放置 `[ranks]` 和 `[tooltips]`，并在模板的 `flag_button` 上将提示声明为工具提示。标志按钮在模板中的自己的 `title` 和 `description` 可能会命名不同的区域条目以仅用作该面板的名称和说明布局。

### 命令等级 { #command-ranks }

设置选项卡上的**命令等级**图标打开一个面板，岛屿所有者在其中选择可能使用每个队伍命令的最低[等级](#ranks)，例如谁可以邀请、踢出或设置岛屿的名称。**左键**和**右键**单击命令会循环通过等级，就像保护标志一样。操作员可以使用 ++shift+左键++，以与[隐藏标志](#hide-flags)相同的方式对玩家隐藏命令。

截至 BentoBox 3.23.3，玩家只看到他们有权使用的命令。如果你在你的服务器上拒绝命令的权限，例如 `[gamemode].island.border`，它也不再出现在此面板中。以前只检查了顶级命令，所以玩家无法运行的子命令仍然被列出。

#### 自定义命令等级面板 { #customizing-the-command-ranks-panel }

!!! new "在 BentoBox 3.23.3 中添加"
    命令等级面板由模板文件布局，就像[设置面板](#customizing-the-settings-panel)一样。

布局来自 `plugins/BentoBox/panels/command_ranks_panel.yml`，BentoBox 在首次启动时写入该文件。游戏模式附属可以在其 `panels` 文件夹中提供自己的副本，该副本用于该游戏模式。默认文件保持面板看起来与之前一样：每个命令一个地图，没有填充，仅占用命令需要的行数。如果无法读取该文件，BentoBox 显示内置面板。

每个按钮都通过 `data.type` 放置：

| 类型 | 显示内容 |
| --- | --- |
| `COMMAND` | 分页命令列表中的一个插槽。放置尽可能多的命令，每页；默认为 45。 |
| `NEXT`、`PREVIOUS` | 分页。仅在有可翻页时显示。 |

内置面板在 49 个命令处停止，所以任何超过该数量的命令都从不显示。模板改为分页。

可以在模板的 `reusable` 部分的 `command_button` 上更改命令的绘制方式：

- `icon` 替换默认的 `MAP`。
- `title` 是用作名称布局的区域条目（或文本），而不是 `protection.panel.flag-item.name-layout`。`[name]` 是命令，例如 `/island sethome`。
- `description` 是用作说明布局的区域条目（或文本），而不是 `protection.panel.flag-item.description-layout`。`[description]` 是来自 `protection.panel.flag-item.command-instructions` 的命令文本。等级列表添加在其后。
- `actions` 仅添加工具提示，这些工具提示添加在等级列表之后。点击本身始终按上面描述的方式工作。默认布局已包含点击提示。

例如，要将每个命令显示为纸张并填充空插槽：

```yaml
command_ranks_panel:
  title: protection.flags.COMMAND_RANKS.name
  type: INVENTORY
  background:
    icon: LIGHT_BLUE_STAINED_GLASS_PANE
    title: "&b&r"
  force-shown: 6
  content:
    # ... command_button 的行，以及分页按钮，如默认文件所示
  reusable:
    command_button:
      icon: PAPER
      data:
        type: COMMAND
```

## 管理员设置面板 { #admin-settings-panel }

在游戏世界中运行 `/[admin_command] settings`（**不带任何参数**）以打开**管理员设置面板**（权限 `[gamemode].admin.settings`）。它有三个选项卡。它们控制世界和新岛屿，而不是任何现有岛屿。

!!! tip
    每个游戏模式都有自己的管理员命令和自己的设置。为要更改的游戏模式运行命令，例如用于 BSkyBlock 的 `/bsbadmin settings` 或用于 AcidIsland 的 `/acid settings`。

!!! new "在 BentoBox 3.23.0 中添加"
    管理员设置面板由 `plugins/BentoBox/panels/admin_settings_panel.yml` 布局，其方式与[玩家的设置面板](#customizing-the-settings-panel)相同。其选项卡类型为 `WORLD_SETTING`、`WORLD_DEFAULTS` 和 `ISLAND_DEFAULTS`；最后两个需要 `[gamemode].admin.set-world-defaults` 权限，没有该权限会被隐藏。同一文件布局 `/[admin_command] settings <player_name>`：每个世界选项卡将岛屿选项卡（`PROTECTION`、`SETTING`）命名为其 `fallback`，这在有岛屿时显示。

在这些选项卡中所做的更改会立即保存到游戏模式的 `config.yml`。

### 世界设置 { #world-settings }

第一个选项卡列出**世界设置**标志：适用于整个游戏世界、岛屿内外的开关，例如*爬行怪爆炸*、*离线红石*或*访客保留库存*。单击标志以打开或关闭它。每个需要权限 `[gamemode].admin.world.settings.<FLAG_ID>`，操作员拥有该权限。

也可以从控制台或聊天设置世界设置：

```
/[admin_command] settings <FLAG_ID> <Active|Disabled>
```

!!! new "在 BentoBox 3.23.6 中添加"
    **始终允许的实体类型**项（铁锭）打开每种活生物实体类型的列表。绿色类型即使关闭了动物或怪物生成，也会在任何岛屿或世界中生成；铁傀儡默认为绿色，所以村庄铁农场继续工作。**全局生物生成**块列表仍然优先。该列表由 BentoBox 存储，而不是在游戏模式的 `config.yml` 中；请参阅[生物生成优先级](#mob-spawning-precedence)。需要 `[gamemode].admin.settings.ALLOW_MOBS`。

#### 每个世界设置的作用 { #what-each-world-setting-does }

这些是大多数服务器想要查看的世界设置。默认值适用于 BSkyBlock；其他游戏模式可能不同。每个标志都在[标志](Flags.md)中列出。

| 设置 | 作用 | 默认 |
|---|---|---|
| **始终允许的实体类型** | 无论动物和怪物生成标志如何说，都在任何岛屿或世界中生成的实体。使用它来让村庄铁农场在已关闭动物生成的服务器或岛屿上工作。铁傀儡默认被允许。块列表（*全局生物生成*）仍然获胜。请参阅[生物生成优先级](#mob-spawning-precedence)。 | 铁傀儡 |
| **箱子爆炸伤害** | 保护箱子免受爆炸（苦力怕、TNT、凋零、恶魂）摧毁。防止破坏但意味着箱子可用于制造防爆房间。 | 开启 |
| **清洁超平坦** | 如果世界生成器停止工作，新块区生成为平坦草地。此设置检测并修复这些块区。除非你有此问题，否则保持关闭——它是资源密集型的。 | 关闭 |
| **粗土耕作** | 防止玩家使用锄头将粗土转换为普通土壤。土壤在大多数游戏模式中稀缺且有价值；如果砾石容易获得，粗土耕作可以被利用来廉价生成它。 | 关闭（防止开启） |
| **苦力怕爆炸** | 防止苦力怕爆炸对岛屿方块的伤害。苦力怕是岛屿破坏的最常见原因。防止这种情况使游戏更容易，但减少了管理员支持负担。 | 开启 |
| **苦力怕访客点燃** | 防止访客在他人岛屿上使用燧石和钢铁激活苦力怕——一种常见的破坏方法。 | 开启 |
| **末地箱** | 阻止访问和制作末地箱，其可以在游戏模式世界之间走私物品。如果使用每世界末地箱插件，请禁用。 | 开启（阻止） |
| **末影人方块盗窃** | 防止末影人从岛屿上拿起方块。没有这个，玩家会失去他们自己没有移除的方块。 | 开启 |
| **地理限制生物** | 防止某些生物（例如凋零、飞行生物）离开它们生成的岛屿。如果它们越过边界，它们会被移除。 | 开启 |
| **访客保护** | 在另一玩家的岛屿上保护访客免受大多数伤害。也将访客传送到安全地方，如果他们掉进虚空。 | 开启 |
| **物品框架保护** | 防止物品框架被破坏或其物品被非成员击出。 | 开启 |
| **全局生物生成** | 设置哪些生物类型可以在世界任何地方生成，覆盖所有其他生成设置。例如，在服务器范围内禁用幻翼。 | 变化 |
| **岛屿外液体流动** | 停止熔岩和水在岛屿保护边界外流动，防止岛屿之间的圆石形成或洪水。 | 开启 |
| **岛屿外生物生成** | 防止生物在岛屿之间的区域生成，将生成集中在岛屿区域内。不推荐用于 AcidIsland 因为看起来不自然。 | 关闭 |
| **黑曜石舀取** | 允许玩家右键单击一个孤立的单个黑曜石方块，用空桶恢复熔岩。帮助在圆石生成器设置期间意外制造黑曜石的新玩家。 | 开启 |
| **离线植物生长** | 当没有队伍成员在线时，停止岛屿上的庄稼和植物生长，即使访客正在加载块区。 | 关闭 |
| **离线红石** | 当没有队伍成员在线时，禁用岛屿上的红石电路。 | 关闭 |
| **活塞超出边界** | 停止活塞将方块推出岛屿保护边界——这是破坏相邻岛屿的常见利用。 | 开启 |
| **传送时移除生物** | 当玩家传送到他们的岛屿家园时清除该区域的敌对生物，防止到达时突然死亡。 | 开启 |
| **刷怪笼类型保护** | 防止玩家使用生成蛋更改刷怪笼方块的生物类型。当刷怪笼作为奖励给出时有用。 | 开启 |
| **树木生长边界** | 防止树木在岛屿保护边界外生长。没有这个，树木可能会侵入其他岛屿或创建无法到达的方块。 | 开启 |
| **凋零伤害** | 限制凋零可能对岛屿内外造成的破坏。 | 开启 |

#### 生物生成优先级 { #mob-spawning-precedence }

自然和刷怪笼生物生成按此顺序决定。第一个匹配的规则获胜。

1. **全局生物生成**块列表（游戏模式配置中的 `protection.block-mobs`）。被阻止的类型永远不会生成。
2. **始终允许的实体类型**允许列表。允许的类型无论下面的标志如何都会生成。
3. 岛屿的**动物自然生成**、**怪物自然生成**、**动物刷怪笼生成**和**怪物刷怪笼生成**设置，或者当没有岛屿时这些标志的世界默认值。

由玩家直接造成的生成，例如繁殖、生成蛋或建造傀儡，永远不会被任何这些阻挡。

!!! note "允许列表存储位置"
    与其他世界设置不同，允许列表不在游戏模式的 `config.yml` 中。BentoBox 本身存储它，每个游戏模式一条记录，在其数据库中：使用默认平面文件数据库，它是 `plugins/BentoBox/database/CoreWorldSettings/<GameMode>.json`。第一次看到游戏模式时用 `IRON_GOLEM` 播种；之后只有管理员在面板中的编辑应用。清除记录恢复种子。

### 世界保护 { #world-protections }

第二个选项卡**世界保护**决定玩家可能在**任何岛屿保护范围外**做什么。这包括岛屿之间的虚空、出生点区域（如果它不是岛屿）以及荒野。请参阅[岛屿的边界](#where-an-island-ends)。

在岛屿外没有队伍也没有等级，所以这里的每个保护标志只是**对所有人打开或关闭**。单击标志切换它：

- **允许**：任何人可能在岛屿外做这个操作。
- **不允许**：没有人可以，除了操作员和有[绕过权限](#bypass-the-protection)的玩家。

默认情况下，大多数保护标志在岛屿外是**不允许**的，所以玩家不能在其岛屿外建造、破坏方块或使用物品。此选项卡需要 `[gamemode].admin.set-world-defaults`，每个标志还需要 `[gamemode].admin.world.settings.<FLAG_ID>`。操作员拥有两者。这些值存储在游戏模式的 `config.yml` 中的 `world.flags` 下。

!!! example "让玩家在岛屿之间建造桥梁"
    玩家只能在自己的岛屿上建造，所以他们不能桥接到邻居。要让他们在岛屿外建造：

    1. 站在游戏世界中，运行不带玩家名称的 `/[admin_command] settings`。
    2. 打开**世界保护**选项卡。它既不是第一个选项卡也不是**岛屿默认值**。
    3. 打开**放置方块**和**破坏方块**，加上玩家在那里可能需要的任何其他东西，例如桶、门或压力板。

    岛屿本身由其自己的设置保持保护。要让访客也从其他岛屿拿东西，请为新岛屿设置[岛屿默认值](#island-defaults)，或使用 `/[admin_command] settings <player>` 更改现有岛屿。

没有岛屿的玩家可以在 `/[player_command] settings` 中看到这些值（只读）。请参阅[世界保护视图](#world-protection-view)。

### 岛屿默认值 { #island-defaults }

!!! new "在 BentoBox 3.14.0 中添加"
    **岛屿默认值**选项卡设置**新创建的岛屿**开始的标志。以前，这只能在游戏模式的 `config.yml` 中完成。

第三个选项卡设置**新岛屿**中每个标志的起始值：

- 每个**保护标志**显示其默认等级。左键单击或右键单击循环通过等级。
- 每个**设置标志**显示其默认开/关状态。单击切换它。

这些值存储在游戏模式的 `config.yml` 中的 `world.default-island-flags` 和 `world.default-island-settings` 中。未在其中列出的标志使用标志的内置默认值。

更改仅适用于**在更改后**创建的岛屿。要将默认值推送到**现有**岛屿，运行 `/[admin_command] resetflags` 重置每个岛屿上的每个标志，或 `/[admin_command] resetflags <FLAG_ID>` 重置一个标志。这会覆盖岛屿所有者设置的任何内容，所以你会被要求确认。

此选项卡**不**控制玩家可能在岛屿外做什么。为此，使用[世界保护](#world-protections)。

### 更改玩家的岛屿 { #changing-a-players-island }

`/[admin_command] settings <player_name>` 打开该玩家岛屿的保护和设置选项卡，如所有者所见，所以管理员可以更改任何标志。`/[admin_command] settings spawn-island` 对出生岛屿做同样的事情。

也可以从命令行完成：

```
/[admin_command] settings <player_name> <FLAG_ID> <rank>              # protection flag, e.g. Visitor
/[admin_command] settings <player_name> <FLAG_ID> <Active|Disabled>   # setting flag
```

## 绕过保护 { #bypass-the-protection }

保护标志仅在 BentoBox 游戏世界内强制执行，仅针对没有通过它们的合法方式的玩家。保护可以通过多种方式被绕过——有些是有意的（岛屿等级），有些是针对员工的（操作员状态和版主权限），有些是结构性的（世界或标志类型）。

!!! tip
    下面权限中的 `[gamemode]` 是游戏模式的小写名称。对于 BSkyBlock，节点以 `bskyblock.mod…` 开头，对于 AcidIsland 则为 `acidisland.mod…` 等。

### 岛屿等级——设计方式 { #island-ranks-the-intended-way }

绕过保护标志的正常、设计方式是在岛屿上拥有足够高的**等级**。每个保护标志都有一个所需等级，任何等级大于或等于它的成员都被允许执行操作。这就是为什么所有者可以建造而访客不能——这不是真正的绕过，只是标志按配置工作。请参阅上面的[等级](#ranks)列表。

### 操作员 { #operators }

服务器操作员（`/op`）是最广泛的绕过。操作员通过 BentoBox 世界中的**每个保护标志**，可以进入锁定和被禁的岛屿，并且免受禁止和驱逐。

两个重要注意事项：

- **操作员不绕过岛屿设置标志。** `SETTING` 类型的标志（岛屿切换，例如*允许 PVP*、*生物生成*等）在操作员检查前被评估，所以操作员受到它们约束，就像任何其他玩家一样。操作员状态仅覆盖*保护*标志。
- **管理员开关无法完全在玩家自己的岛屿上"取消操作员"。** 即使打开开关（见下文），操作员仍被允许在岛屿上，因为等级检查将操作员状态视为始终允许。要测试作为真正的非操作员的保护，请移除操作员状态。

### 版主绕过权限 { #moderator-bypass-permissions }

对于不应该是完全操作员的员工，保护可以用权限绕过。这些由管理员开关控制（见下文），所以版主可以切换自己的绕过以体验普通玩家会经历的世界。

- `[gamemode].mod.bypassprotect` ——绕过**所有**保护标志，在世界各地。
- `[gamemode].mod.bypass.<FLAG_ID>.everywhere` ——绕过**一个**命名标志（例如 `BREAK_BLOCKS`）在世界各地。
- `[gamemode].mod.bypass.<FLAG_ID>.island` ——绕过**一个**命名标志，但仅在玩家在岛屿上会被阻止的地方。

### 管理员"开关"——作为普通玩家测试 { #the-admin-switch-testing-as-a-normal-player }

命令 `/[admin_command] switch`（权限 `[gamemode].mod.switch`）切换版主的绕过权限开关。默认情况下绕过权限**激活**（版主正在绕过保护）；运行命令一次切换绕过**关闭**，所以他们受到保护，就像普通玩家一样，再运行一次切换回开。这影响上面的 `mod.bypassprotect` 和 `mod.bypass.*` 权限——它**不会**禁用原始操作员状态。

### 锁定、禁止和驱逐 { #locks-bans-and-expels }

岛屿锁定、禁止和驱逐有自己的绕过权限，与标志系统无关：

- `[gamemode].mod.bypasslock` ——进入锁定的岛屿。
- `[gamemode].mod.bypassban` ——进入你被禁止的岛屿。
- `[gamemode].mod.bypassexpel` 和 `[gamemode].admin.noexpel` ——不能被驱逐。
- `[gamemode].admin.noban` ——不能被禁止。

任何携带 Bukkit `NPC` 元数据的实体（例如 Citizens NPC）也被允许通过锁定、禁止、PVP 和无敌访客检查，所以插件 NPC 不会被岛屿保护困住或伤害。

### 冷却和延迟 { #cooldowns-and-delays }

命令冷却和传送热身延迟可以跳过：

- `[gamemode].mod.bypasscooldowns` ——忽略命令冷却。
- `[gamemode].mod.bypassdelays` ——跳过延迟传送命令上的移动热身延迟。

### 永不受保护的 { #what-is-never-protected }

- **非 BentoBox 世界。** 保护仅在游戏模式世界中存在（及其链接的标准下界/末地）。服务器的默认世界和其他插件的世界永远不会被检查。
- **岛屿外区域遵循不同规则。** 当玩家在游戏模式世界中但在每个岛屿保护范围外时，[世界保护](#world-protections)适用，而不是任何岛屿的标志。
- **删除的岛屿是例外：** 在待删除的岛屿上，默认情况下不允许任何操作——除了操作员和拥有 `mod.bypassprotect` / `mod.bypass.<FLAG_ID>.everywhere` 权限的持有者，其绕过首先被检查。

## 故障排除 { #troubleshooting }

**玩家无法在岛屿之间建造或破坏方块。**
该区域在岛屿外，所以[世界保护](#world-protections)选项卡适用。打开你需要的标志。改变岛屿默认值不会帮助。

**我改变了岛屿默认值但现有岛屿没有改变。**
岛屿默认值仅适用于之后创建的岛屿。使用 `/[admin_command] resetflags` 将其应用到现有岛屿，或使用 `/[admin_command] settings <player>` 改变单个岛屿。

**玩家无法改变设置，即使他们拥有岛屿。**
该设置可能需要 `[gamemode].settings.<FLAG_ID>` 权限，或设置处于冷却中。

**我是操作员，无法测试保护是否工作。**
操作员绕过每个保护标志。使用非操作员账户测试。`/[admin_command] switch` 仅关闭版主绕过权限，不会禁用操作员状态。

**我不知道哪个标志阻止了操作。**
运行 `/[admin_command] why <player>` 将该玩家的每个保护检查记录到控制台，然后执行操作。日志命名标志、位置和结果。再运行一次命令以停止。

**`why` 说操作被允许，但玩家仍被阻止。**
BentoBox 之外的东西在阻止它：另一个插件，或服务器本身（例如 `server.properties` 中的出生保护）。

**我应该在 BentoBox 世界中使用 WorldGuard 吗？**
你不需要它：BentoBox 保护岛屿和其间的空间。如果你在那里使用 WorldGuard，其区域和 BentoBox 的标志都适用，这可能会意外阻止事物。将 WorldGuard 区域保持在游戏模式世界外，或在有东西被阻止时首先检查。
