# ControlPanel

**ControlPanel** 为你的玩家提供一个可点击的 GUI 菜单来运行他们最常用的岛屿命令——无需输入。服务器管理员可以使用简单的 YAML 文件构建完全可自定义的面板，支持多种点击操作、自定义图标和实时占位符。

由 [BONNe](https://github.com/BONNe) 创建和维护。

{{ addon_description("ControlPanel") }}

## 安装

1. 将 ControlPanel 插件 jar 放入 BentoBox 插件的 `addons` 文件夹。
2. 重启服务器。ControlPanel 将在 `plugins/BentoBox/addons/ControlPanel/` 内创建一个默认的 `controlPanelTemplate.yml`。
3. 编辑 `controlPanelTemplate.yml` 来构建你的面板（见下面的[配置](#configuration)）。
4. 用管理员命令导入面板：
```
/{admin} cp import
```

!!! tip
    将 `{admin}` 替换为你的游戏模式的管理员命令标签，例如 BSkyBlock 的 `bsb`、AOneBlock 的 `oa`、AcidIsland 的 `acid`。

## 命令

### 玩家命令

| 命令 | 描述 | 权限 |
|---|---|---|
| `/[label] controlpanel` | 打开玩家分配的控制面板 | `[gamemode].controlpanel` |
| `/[label] cp` | 上述命令的快捷别名 | `[gamemode].controlpanel` |

将 `[label]` 替换为游戏模式的玩家命令，例如 BSkyBlock 的 `island` 或 AOneBlock 的 `ob`。

显示的面板取决于玩家的权限。没有特定面板权限的玩家会看到标记为 `defaultPanel: true` 的面板。如果玩家通过 `[gamemode].controlpanel.panel.<suffix>` 有特定面板的权限，则会显示该面板。

### 管理员命令

| 命令 | 描述 | 权限 |
|---|---|---|
| `/{admin} cp import` | 从 `controlPanelTemplate.yml` 导入面板 | `[gamemode].controlpanel.admin` |
| `/{admin} cp import <filename>` | 从自定义 YAML 文件导入面板 | `[gamemode].controlpanel.admin` |

文件名不需要 `.yml` 扩展名——它会自动添加。文件必须位于 `plugins/BentoBox/addons/ControlPanel/`。

!!! warning
    如果游戏模式已存在面板，导入将要求确认后再替换它们。

## 权限

| 权限 | 默认值 | 描述 |
|---|---|---|
| `[gamemode].controlpanel` | `true` | 允许玩家打开控制面板 |
| `[gamemode].controlpanel.admin` | `op` | 允许使用管理员导入命令 |
| `[gamemode].controlpanel.panel.default` | `true` | 授予对默认面板的访问权限 |
| `[gamemode].controlpanel.panel.<suffix>` | — | 授予对具有给定后缀的自定义面板的访问权限 |

将 `[gamemode]` 替换为小写游戏模式名称，例如 `bskyblock`、`acidisland`、`aoneblock`、`caveblock`、`skygrid`。

!!! note
    如果玩家有多个面板权限，将显示他们有权访问的第一个标记为 `defaultPanel: true` 的面板。如果玩家具有通配符 `*` 权限，将使用第一个定义的默认面板。

## 配置

ControlPanel 使用两个文件：

- `config.yml` — 通用插件设置
- `controlPanelTemplate.yml` — 定义面板和按钮

两者都位于 `plugins/BentoBox/addons/ControlPanel/`。

### config.yml

主配置文件有一个设置：

??? note "disabled-gamemodes"
    ControlPanel 不应操作的游戏模式插件名称列表。ControlPanel 不会挂接到这些游戏模式。

    默认值：`[]`

    示例：
    ```yaml
    disabled-gamemodes:
      - BSkyBlock
      - AcidIsland
    ```

### controlPanelTemplate.yml

此文件定义所有控制面板及其按钮。编辑后，运行 `/{admin} cp import` 来加载更改。

#### 面板结构

```yaml
panel-list:
  <panel-key>:
    defaultPanel: true|false
    panelName: '<title>'
    permission: '<suffix>'
    buttons:
      <slot>:
        name: '<display name>'
        material: MATERIAL_NAME
        icon: 'namespace:item_id'
        itemsadder: 'namespace:item_id'
        description: |-
          line one
          line two
        command: '<left-click command>'
        right_click_command: '<right-click command>'
        shift_click_command: '<shift+left-click command>'
```

#### 面板字段

| 字段 | 类型 | 描述 |
|---|---|---|
| `defaultPanel` | boolean | 设为 `true` 以向没有特定面板权限的玩家显示此面板。 |
| `panelName` | string | 物品栏 GUI 的标题。支持 `&` 颜色代码。 |
| `permission` | string | 附加到 `[gamemode].controlpanel.panel.<suffix>` 的后缀。具有该权限的玩家会看到此面板。 |

#### 按钮字段

| 字段 | 必需 | 描述 |
|---|---|---|
| `slot` | 是 | 物品栏槽号（0–53）。使用引用的范围如 `"0-8"` 来用相同按钮填充多个槽。 |
| `name` | 是 | 按钮的显示名称。支持 `&` 颜色代码。 |
| `material` | 否 | 原版 Minecraft 材料，例如 `GRASS_BLOCK`。作为后备图标使用。 |
| `icon` | 否 | BentoBox `ItemParser` 格式，例如 `minecraft:diamond_block`。优先于 `material`。 |
| `itemsadder` | 否 | [ItemsAdder](https://github.com/LoneDev6/ItemsAdder) 自定义物品 ID，例如 `iasurvival:ruby`。需要安装 ItemsAdder。否则退回到纸张。 |
| `description` | 否 | 显示在按钮名称下的 lore 行。支持 `&` 颜色代码、使用 `|-` 的多行、PlaceholderAPI `%placeholders%` 和 `[gamemode]` 替换。 |
| `command` | 否 | 左键点击时执行的命令（以及所有其他点击类型的后备）。 |
| `right_click_command` | 否 | 右键点击或 Shift+右键点击时执行的命令。如果省略，退回到 `command`。 |
| `shift_click_command` | 否 | Shift+左键点击时执行的命令。如果省略，退回到 `command`。 |

!!! info "图标优先级"
    如果指定了多个图标字段，优先级为：`itemsadder` > `icon` > `material`。如果都未设置，按钮默认为 `PAPER`。

#### 点击类型

每个按钮可以根据玩家点击它的方式做出不同的响应：

| 点击操作 | 使用的命令 |
|---|---|
| 左键点击 | `command` |
| 右键点击 | `right_click_command`（退回到 `command`） |
| Shift + 左键点击 | `shift_click_command`（退回到 `command`） |
| Shift + 右键点击 | `right_click_command`（退回到 `command`） |
| 其他任何点击 | `command` |

#### 命令占位符

这些占位符可以在 `command`、`right_click_command` 和 `shift_click_command` 字段中使用：

| 占位符 | 替换为 |
|---|---|
| `[label]` | 游戏模式的玩家命令标签，例如 `island`、`ob` |
| `[player]` | 点击玩家的用户名 |
| `[server]` | 使命令作为服务器控制台而不是玩家运行 |

#### 描述占位符

这些占位符可以在 `description` 字段中使用：

| 占位符 | 替换为 |
|---|---|
| `[gamemode]` | 小写游戏模式名称，例如 `bskyblock`、`aoneblock` |
| `%placeholder%` | 任何已注册的 PlaceholderAPI 占位符 |

#### 槽位布局

GUI 是一个箱子物品栏。每行有 9 个槽位（0–8），最大是 6 行的箱子，有 54 个槽位（0–53）：

```
第 1 行：  0  1  2  3  4  5  6  7  8
第 2 行：  9 10 11 12 13 14 15 16 17
第 3 行： 18 19 20 21 22 23 24 25 26
第 4 行： 27 28 29 30 31 32 33 34 35
第 5 行： 36 37 38 39 40 41 42 43 44
第 6 行： 45 46 47 48 49 50 51 52 53
```

使用引用的范围如 `"0-8"` 来在整行上放置相同的按钮。这对于装饰边框很有用。

## 示例：默认和 VIP 面板

下面是一个实际示例，展示两个面板——一个所有玩家都能看到的默认面板和一个捐献者的 VIP 面板。它演示了槽位范围、多个点击操作、控制台命令、PlaceholderAPI 占位符和 ItemsAdder 图标。

```yaml
panel-list:

  # 默认面板——显示给所有玩家
  default:
    defaultPanel: true
    panelName: '&0&l Control Panel'
    permission: 'default'
    buttons:

      # 使用槽位范围的装饰性顶部边框
      "0-8":
        name: ' '
        material: BLACK_STAINED_GLASS_PANE
        description: ''
        command: ''

      # 多个点击操作的前往岛屿
      9:
        name: '&a&l Go to Island'
        icon: minecraft:grass_block
        description: |-
          &7 左键点击：传送到你的岛屿
          &7 右键点击：前往下界
          &7 Shift 点击：设置家
          &7 岛屿等级：&e%Level_[gamemode]_island_level%
        command: '[label] go'
        right_click_command: '[label] go nether'
        shift_click_command: '[label] sethome'

      10:
        name: '&e&l Set Home'
        icon: minecraft:white_bed
        description: |-
          &7 设置你的岛屿家
          &7 到你的当前位置。
        command: '[label] sethome'

      11:
        name: '&b&l Team'
        icon: minecraft:player_head
        description: |-
          &7 查看和管理
          &7 你的岛屿团队。
        command: '[label] team'

      13:
        name: '&6&l Settings'
        icon: minecraft:anvil
        description: |-
          &7 配置你的岛屿
          &7 保护设置。
        command: '[label] settings'

      # 控制台命令——作为服务器运行，不是玩家
      17:
        name: '&c&l Report Bug'
        icon: minecraft:writable_book
        description: |-
          &7 打开支持工单。
        command: '[server] ticket create [player] bug-report'

  # VIP 面板——玩家需要 bskyblock.controlpanel.panel.vip
  vip:
    defaultPanel: false
    panelName: '&d&l VIP Control Panel'
    permission: 'vip'
    buttons:

      "0-8":
        name: ' '
        material: PURPLE_STAINED_GLASS_PANE
        description: ''
        command: ''

      9:
        name: '&a&l Go to Island'
        icon: minecraft:grass_block
        description: |-
          &7 传送到你的岛屿。
        command: '[label] go'

      # VIP 独占——通过控制台授予 kit
      13:
        name: '&d&l VIP Kit'
        icon: minecraft:chest
        description: |-
          &d VIP 独占！
          &7 领取你的周度 VIP kit。
        command: '[server] kit vipweekly [player]'

      # ItemsAdder 自定义图标示例
      14:
        name: '&6&l VIP Perks'
        itemsadder: 'iasurvival:vip_star'
        description: |-
          &7 浏览你的所有 VIP 特权。
        command: 'vipperks'
```

## 提示

??? tip "创建装饰性边框"
    使用带有玻璃窗格的槽位范围来在面板周围创建干净的边框。设置 `command: ''` 和 `name: ' '` 来使按钮不可交互：
    ```yaml
    "0-8":
      name: ' '
      material: BLACK_STAINED_GLASS_PANE
      description: ''
      command: ''
    ```

??? tip "以控制台身份运行命令"
    在命令前缀加上 `[server]` 来以服务器控制台身份执行它。这让你可以授予 kits、运行经济命令或执行玩家没有直接权限运行的管理操作：
    ```yaml
    command: '[server] give [player] diamond 64'
    ```

??? tip "为排名使用多个面板"
    为不同的玩家组（如默认、VIP 或工作人员）创建单独的面板。使用权限（如 `bskyblock.controlpanel.panel.vip` 或 `bskyblock.controlpanel.panel.staff`）来分配它们。每个组会看到带有适当按钮的定制面板。

??? tip "在描述中使用 PlaceholderAPI"
    按钮描述在面板打开时由 PlaceholderAPI 处理，因此它们总是显示实时数据。在占位符名称中使用 `[gamemode]` 来使相同的模板在游戏模式中工作：
    ```yaml
    description: |-
      &7 等级：&e%Level_[gamemode]_island_level%
      &7 排名：&6%Level_[gamemode]_island_rank%
      &7 余额：&a%vault_balance%
    ```

??? tip "重新加载更改后"
    编辑 `controlPanelTemplate.yml` 后，运行 `/{admin} cp import` 来重新加载。如果你进行了 `config.yml` 的更改，请使用 BentoBox 重新加载命令：`/{admin} bentobox reload`。

## 常见问题

??? question "我如何更改 ControlPanel？"
    ControlPanel 在数据库中存储面板，但你通过模板文件编辑它们。对 `controlPanelTemplate.yml` 进行更改后，通过运行 `/{admin} controlpanel import` 来导入它们。你也可以创建额外的模板文件并按名称导入它们：`/{admin} controlpanel import myPanels`。

??? question "我可以为不同的用户拥有不同的面板吗？"
    可以。在模板文件中定义多个面板，每个都有不同的 `permission` 后缀。然后向玩家分配相应的权限，例如 `bskyblock.controlpanel.panel.vip`。没有特定面板权限的玩家会看到标记为 `defaultPanel: true` 的面板。

??? question "支持什么图标类型？"
    ControlPanel 支持三种图标类型，按此优先级顺序检查：ItemsAdder 自定义物品（`itemsadder` 字段）、BentoBox ItemParser 格式（`icon` 字段）和原版 Minecraft 材料（`material` 字段）。如果都未指定，按钮默认为纸张。

??? question "我可以以服务器控制台身份运行命令吗？"
    可以。在命令前缀加上 `[server]`，它将由控制台而不是玩家执行。你也可以在命令字符串中使用 `[player]` 来插入点击玩家的名称。例如：`[server] give [player] diamond 64`。

??? question "单个按钮可以根据我如何点击它来做不同的事情吗？"
    可以。每个按钮支持多达三个不同的命令：`command` 用于左键点击、`right_click_command` 用于右键点击、`shift_click_command` 用于 shift+左键点击。如果未设置特定的点击命令，它会退回到常规的 `command`。

??? question "你能添加功能 X 吗？"
    请在[这里](https://github.com/BentoBoxWorld/ControlPanel/issues)添加。

## 翻译

{{ translations("ControlPanel") }}