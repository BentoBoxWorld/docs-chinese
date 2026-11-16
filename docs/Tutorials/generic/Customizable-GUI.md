# 自定义菜单 { #customizing-menus }

BentoBox 中大多数玩家看到的菜单（团队菜单、岛屿设置、创建岛屿菜单、家点、语言等）都是从**面板模板**构建的：你可以编辑的 YAML 文件。你可以改变菜单的标题、大小、背景、每个按钮使用的图标、其文本和位置。

你不能创建新的按钮类型。每个菜单只能理解其代码提供的按钮类型。如果你想要自己的菜单且按钮可以运行命令，请使用 [ControlPanel](../../addons/ControlPanel/index.md) 附属。

## 菜单文件的位置 { #where-the-menu-files-are }

| 菜单来自 | 文件夹 |
|---|---|
| BentoBox | `plugins/BentoBox/panels/` |
| 一个游戏模式（仅限该游戏模式） | `plugins/BentoBox/addons/<GameMode>/panels/` |
| 一个附属（Level、Challenges、Warps 等） | `plugins/BentoBox/addons/<Addon>/panels/` |

BentoBox 在第一次使用每个菜单时将其模板写入 `plugins/BentoBox/panels/`。附属将它们写入自己的文件夹。

### BentoBox 的菜单 { #bentoboxs-menus }

| 文件 | 菜单 | 游戏模式可以有自己的副本吗？ |
|---|---|---|
| `island_creation_panel.yml` | 创建或重置时选择岛屿 | 是 |
| `island_homes_panel.yml` | `/island homes` | 是 |
| `language_panel.yml` | `/island language` | 是 |
| `settings_panel.yml` | `/island settings` | 是 |
| `admin_settings_panel.yml` | `/bsbadmin settings` | 是 |
| `command_ranks_panel.yml` | 设置菜单中的命令等级页面 | 是 |
| `team_panel.yml` | `/island team` | 否 |
| `team_invite_panel.yml` | 团队菜单中的邀请屏幕 | 否 |
| `placeholder_panel.yml`、`placeholder_list_panel.yml` | 占位符浏览器 | 否 |

**不同游戏模式的不同菜单：**从 `plugins/BentoBox/panels/` 复制文件到游戏模式的 `panels` 文件夹（如果需要可创建）并编辑副本。例如，`plugins/BentoBox/addons/AOneBlock/panels/island_creation_panel.yml` 只改变 AOneBlock 的创建岛屿菜单。其他游戏模式继续使用 BentoBox 版本。

### 附属菜单 { #addon-menus }

使用模板的附属包括 Level（`top_panel`、`value_panel`、`detail_panel`、`donation_panel`）、Challenges、Biomes、Warps、Upgrades、Likes、Visit、TopBlock、CheckMeOut、MagicCobblestoneGenerator、AOneBlock（`phases_panel`）和 CauldronWitchery。查看每个附属的 `panels` 文件夹。它们使用与下面相同的格式。

## 进行更改 { #making-a-change }

1. 阻止玩家打开菜单，或在测试服务器上先进行此操作。
2. 编辑 `.yml` 文件。保留原始文件的副本。
3. 运行 `/bentobox reload`。这将关闭打开的菜单并重新加载模板。
4. 在游戏中打开菜单并检查它。

如果菜单停止打开或显示空白，YAML 可能无效。检查服务器控制台是否有错误，并将文件粘贴到 YAML 检查器中。**要恢复默认值**，删除该文件。BentoBox 会在下次菜单打开时复制其默认版本。对于附属的文件，重启服务器。

## 常见更改 { #common-changes }

### 更改标题或按钮文字 { #change-the-title-or-button-text }

文本可以是纯文本或**区域键**。默认模板使用区域键，以便菜单被翻译：

```yaml
team_panel:
  title: commands.island.team.gui.titles.team-panel
```

- **更改每种语言的文本：**在区域文件中编辑该键（`plugins/BentoBox/locales/` 或附属的 `locales` 文件夹）。参见[语言和消息](../../BentoBox/About/Multilingual.md)。
- **为所有人使用相同的文本：**将键替换为你自己的文本，例如 `title: "&6My Team"`。

### 更改背景或边框 { #change-the-background-or-border }

```yaml
  background:
    icon: GRAY_STAINED_GLASS_PANE
    title: "&b&r"     # 不显示名称
  border:
    icon: LIGHT_BLUE_STAINED_GLASS_PANE
    title: "&b&r"
```

删除 `background` 或 `border` 部分以留下这些位置空白。`"&b&r"` 是显示没有名称的物品的通常方式；Minecraft 总是显示工具提示，所以不能完全隐藏。

### 更改按钮的图标 { #change-a-buttons-icon }

在按钮上设置 `icon`。任何物品都可以工作，包括带有数据、药水颜色和玩家头颅的物品。请参见[物品格式](../../BentoBox/ItemParser.md)。

```yaml
      icon: DIAMOND
      icon: tipped_arrow[potion_contents={custom_color:11546150}]
```

如果你省略 `icon`，某些按钮会选择自己的图标。例如，团队菜单显示玩家的头颅，创建岛屿菜单显示岛屿的图标。

### 移动按钮 { #move-a-button }

按钮由 `content` 下的**行**（1–6）和**列**（1–9）放置。要移动一个，改变其行或列号：

```yaml
  content:
    1:        # 第 1 行
      1:      # 第 1 列
        data:
          type: STATUS
```

### 使菜单更高 { #make-a-menu-taller }

菜单缩小以适应有按钮的行。要在它们为空时保留行，请使用 `force-shown`：

```yaml
  force-shown: 6        # 总是显示第 1 到 6 行
  force-shown: [2, 4]   # 总是显示第 2 和 4 行
```

这只添加空行。要显示**每页更多物品**（更多岛屿、更多家点），还要添加更多重复按钮。[更大的创建岛屿菜单](Bigger-Create-Island-Menu.md) 页面提供了完整的工作示例。

### 移除按钮 { #remove-a-button }

从 `content` 删除按钮。该槽位然后显示背景。某些按钮是菜单工作所必需的：在可能有多页的菜单中保留 `NEXT`/`PREVIOUS` 按钮。

## 模板如何布局 { #how-a-template-is-laid-out }

每个模板都有相同的部分。这个简化的示例基于创建岛屿菜单：

```yaml
island_creation_panel:          # 必须与文件名相同
  title: panels.island_creation.title
  type: INVENTORY               # INVENTORY（箱子）、HOPPER（5 个槽位）或 DROPPER（9 个槽位）
  background:
    icon: BLACK_STAINED_GLASS_PANE
    title: "&b&r"
  border:
    icon: BLACK_STAINED_GLASS_PANE
    title: "&b&r"
  force-shown: []
  content:
    2:
      2: blueprint_bundle_button    # 一个名称指向 `reusable` 中的按钮
      3: blueprint_bundle_button
    3:
      9:                            # 或直接在此定义按钮
        icon: ARROW
        title: panels.buttons.next.name
        description: panels.buttons.next.description
        data:
          type: NEXT
        actions:
          next:
            click-type: UNKNOWN
            tooltip: panels.tips.click-to-next
  reusable:
    blueprint_bundle_button:
      title: panels.island_creation.buttons.bundle.name
      description: panels.island_creation.buttons.bundle.description
      data:
        type: BUNDLE
      actions:
        select:
          click-type: UNKNOWN
          tooltip: panels.tips.click-to-choose
```

### 按钮设置 { #button-settings }

| 设置 | 作用 |
|---|---|
| `icon` | 显示的物品。参见[物品格式](../../BentoBox/ItemParser.md) |
| `title` | 物品的名称：文本或区域键 |
| `description` | 名称下的行：文本或区域键 |
| `data` | **按钮是什么。** `type` 选择按钮类型（见下文）。某些类型需要额外的设置，例如设置标签按钮上的 `tab` |
| `actions` | 每次点击做什么，以及为其添加的工具提示行 |
| `fallback` | 当此按钮无法显示时要显示的另一个按钮，例如当最后一页没有剩余空间时。它可以是完整按钮或 `reusable` 按钮的名称。需要 BentoBox 3.23.0 或更高版本 |

### 重复按钮（`reusable`） { #repeating-buttons-reusable }

列出内容的菜单（岛屿、家点、团队成员、语言、标志）对每个条目使用一个按钮设计。在 `reusable` 下定义一次，并将其名称放在每个可能出现条目的槽位中。菜单按顺序填充这些槽位并翻页其余的。

### 点击动作 { #click-actions }

每个动作都有一个名称、点击类型和工具提示：

```yaml
        actions:              # 团队菜单的成员按钮
          kick:
            click-type: SHIFT_RIGHT
            tooltip: commands.island.team.gui.tips.SHIFT_RIGHT.kick
          setowner:
            click-type: SHIFT_LEFT
            tooltip: commands.island.team.gui.tips.SHIFT_LEFT.setowner
```

- `click-type` 是 Minecraft 点击：`LEFT`、`RIGHT`、`SHIFT_LEFT`、`SHIFT_RIGHT`、`MIDDLE`、`DROP` 等。`UNKNOWN` 表示任何点击。
- 动作名称（`kick`、`setowner`）是菜单做什么。使用已经在默认文件中的名称。你可以改变哪个点击触发动作，或从菜单中删除你不想让玩家使用的动作。
- 工具提示被添加在描述下方，按动作列出的顺序。

### BentoBox 菜单中的按钮类型 { #button-types-in-bentoboxs-menus }

| 菜单 | 按钮类型（`data: type:`） |
|---|---|
| 创建岛屿 | `BUNDLE`、`NEXT`、`PREVIOUS` |
| 家点 | `ISLAND`、`NEXT`、`PREVIOUS` |
| 语言 | `LOCALE`、`NEXT`、`PREVIOUS` |
| 团队 | `STATUS`、`MEMBER`、`RANK`、`INVITE`、`INVITED` |
| 团队邀请 | `PROSPECT`、`SEARCH`、`BACK`、`NEXT`、`PREVIOUS` |
| 设置/管理员设置 | `FLAG`、`TAB`、`MODE`、`RESET`、`NEXT`、`PREVIOUS` |
| 命令等级 | `COMMAND`、`NEXT`、`PREVIOUS` |
| 占位符 | `BENTOBOX`、`ADDON`、`PLACEHOLDER`、`BACK`、`NEXT`、`PREVIOUS` |

默认文件包含解释每个的注释。设置菜单在[保护、标志和等级](../../BentoBox/Island-Protection,-Flags-&-Ranks.md#customizing-the-settings-panel)中有详细介绍。

## 故障排除 { #troubleshooting }

**我的更改没有显示。**
运行 `/bentobox reload`，然后重新打开菜单。如果游戏模式在 `addons/<GameMode>/panels/` 中有自己的副本，该副本被使用而不是 `plugins/BentoBox/panels/` 中的。

**菜单为空或编辑后无法打开。**
YAML 无效或顶级名称不再与文件名匹配。检查控制台，修复文件，或删除它以恢复默认值。

**我添加了行但其中什么都没有出现。**
`force-shown` 只添加空间。将重复按钮（例如 `blueprint_bundle_button`）添加到新槽位。

**文本显示为 `commands.island.…` 而不是文字。**
该键在玩家语言的区域文件中缺失。添加它，或使用纯文本。

**我想要一个运行命令的按钮。**
模板不能做这个。使用 [ControlPanel](../../addons/ControlPanel/index.md) 附属。

## 另请参见 { #see-also }

- [更大的创建岛屿菜单](Bigger-Create-Island-Menu.md)：完整的工作示例
- [物品格式](../../BentoBox/ItemParser.md)：编写图标
- [语言和消息](../../BentoBox/About/Multilingual.md)：改变菜单文本
- [模板化面板 API](../api/Templated-Panel.md)：针对在他们自己的附属中添加模板的开发者
