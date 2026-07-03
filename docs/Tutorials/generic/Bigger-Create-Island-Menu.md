# 扩大创建岛屿菜单（增加行数）

**问题：** "是否可以让创建岛屿菜单变大——最多 5 或 6 行而不是默认的 3 行？"

**回答：** 可以。创建岛屿菜单是一个完全[可自定义的 GUI](Customizable-GUI.md)。你可以通过编辑 `island_creation_panel.yml` 模板来控制菜单有多少行，以及每页显示多少个蓝图捆绑包。本页向你展示具体方法。

首先决定你真正想要的是哪一种，因为它们需要不同的改动：

- **只想让菜单看起来更高** （更多行的空间，例如用于框架式/宽敞的外观）→ 使用下面的一行代码 [`force-shown` 快捷方式](#just-want-a-taller-menu-force-shown)。额外的行将被空的背景填充。
- **想要一次看到更多岛屿 / 更少的页面** → 你需要[添加更多捆绑包按钮](#example-a-6-row-menu)。仅使用 `force-shown` 不会做到这一点。

## 只想要更高的菜单？（`force-shown`）

如果你只想要一个更高的菜单——更多可见的行，而不一定要在屏幕上放下更多岛屿——这是一个一行的改动。在 `island_creation_panel.yml` 中添加（或编辑）`force-shown` 行：

```yaml
force-shown: 6
```

`force-shown: 6` 强制第 1 到 6 行始终渲染，给你一个完整的 **6 行（54 个槽位）** 的面板。使用 `5` 可得到 5 行，依此类推。

**重要：** `force-shown` 仅控制面板的**高度**。它打开的额外行被你的 `background`/`border` 物品填充——它们**不** 包含更多岛屿捆绑包。捆绑包只出现在 `content` 部分中存在 `blueprint_bundle_button` 条目的地方。所以如果你的目标是显示*更多岛屿*（而不仅仅是让框变大），请跳到[6 行示例](#example-a-6-row-menu)，其中也添加了额外的捆绑包按钮。

## 背景：菜单是如何构建的

创建岛屿菜单（以及玩家重置岛屿时显示的相同菜单）由称为 `island_creation_panel.yml` 的面板模板生成。BentoBox 附带一个默认版本，带有 **3 行** 和最多 **7 个捆绑包按钮每页** （当有比适配的更多捆绑包时，带有"上一页"/"下一页"箭头对用于分页）。

两个规则决定玩家实际看到多少行：

1. **面板会增长以适应其内容。** 如果一行包含至少一个按钮，该行就会显示。在内部网格始终是 6 行，但空行会被修剪，所以默认模板看起来只有 3 行，因为第 1、5 和 6 行是空的。
2. **`force-shown` 可以固定行打开** 即使它们是空的（对于在你的捆绑包列表增长时保持固定布局很有用）。

所以要获得一个更大的菜单，你只需在更多行上添加更多 `blueprint_bundle_button` 条目。有一个硬性最大值 **6 行** （54 个槽位），因为那是 Minecraft 箱子库存能达到的最大值。

## 文件放在哪里

该菜单可以在两个级别被覆盖。BentoBox 按此顺序查找该文件：

1. **按游戏模式** （推荐）— `plugins/<GameMode>/panels/island_creation_panel.yml`
   例如 `plugins/AcidIsland/panels/island_creation_panel.yml`、`plugins/BSkyBlock/panels/island_creation_panel.yml`。
   这仅影响那一个游戏模式。
2. **全局后备** — `plugins/BentoBox/panels/island_creation_panel.yml`
   用于任何没有自己副本的游戏模式。

如果两个文件都不存在，将使用内置默认值（在 BentoBox jar 内部）。

> **提示：** 复制默认文件而不是从头开始编写。启动服务器一次以让 BentoBox 写出其默认值，然后将 `plugins/BentoBox/panels/island_creation_panel.yml` 复制到你的游戏模式的 `panels/` 文件夹中并在那里编辑它。保存后使用 `/bentobox reload` （或重启）重新加载。

## 示例：6 行菜单

此模板显示一个带有边框布局的完整 6 行菜单。第 2-5 行保存蓝图捆绑包按钮（每页最多 **28** 个捆绑包），第 6 行保存分页箭头。

```yaml
island_creation_panel:
  title: panels.island_creation.title
  type: INVENTORY
  background:
    icon: BLACK_STAINED_GLASS_PANE
    title: "&b&r"
  border:
    icon: BLACK_STAINED_GLASS_PANE
    title: "&b&r"
  # 固定所有 6 行打开，即使某些是空的。使用 [] 让面板
  # 改为自动调整大小以适应其内容。
  force-shown: 6
  content:
    2:
      2: blueprint_bundle_button
      3: blueprint_bundle_button
      4: blueprint_bundle_button
      5: blueprint_bundle_button
      6: blueprint_bundle_button
      7: blueprint_bundle_button
      8: blueprint_bundle_button
    3:
      2: blueprint_bundle_button
      3: blueprint_bundle_button
      4: blueprint_bundle_button
      5: blueprint_bundle_button
      6: blueprint_bundle_button
      7: blueprint_bundle_button
      8: blueprint_bundle_button
    4:
      2: blueprint_bundle_button
      3: blueprint_bundle_button
      4: blueprint_bundle_button
      5: blueprint_bundle_button
      6: blueprint_bundle_button
      7: blueprint_bundle_button
      8: blueprint_bundle_button
    5:
      2: blueprint_bundle_button
      3: blueprint_bundle_button
      4: blueprint_bundle_button
      5: blueprint_bundle_button
      6: blueprint_bundle_button
      7: blueprint_bundle_button
      8: blueprint_bundle_button
    6:
      1:
        icon: tipped_arrow[potion_contents={custom_color:11546150}]
        title: panels.buttons.previous.name
        description: panels.buttons.previous.description
        data:
          type: PREVIOUS
          indexing: true
        actions:
          previous:
            click-type: UNKNOWN
            tooltip: panels.tips.click-to-previous
      9:
        icon: tipped_arrow[potion_contents={custom_color:8439583}]
        title: panels.buttons.next.name
        description: panels.buttons.next.description
        data:
          type: NEXT
          indexing: true
        actions:
          next:
            click-type: UNKNOWN
            tooltip: panels.tips.click-to-next
  reusable:
    blueprint_bundle_button:
      # icon: GRASS_BLOCK   # 取消注释以强制每个捆绑包使用一个图标；
                            # 否则每个捆绑包使用其自己的配置图标。
      title: panels.island_creation.buttons.bundle.name
      description: panels.island_creation.buttons.bundle.description
      data:
        type: BUNDLE
      actions:
        select:
          click-type: UNKNOWN
          tooltip: panels.tips.click-to-choose
```

### 想要 5 行菜单呢？

从 `content` 中删除第 5 行，并将 `force-shown: 6` 更改为 `force-shown: 5`。如果需要，可将分页箭头向上移到第 5 行。从 1 到 6 的任何行数都以相同的方式工作——只需添加或删除行数的 `blueprint_bundle_button` 条目。

## 各部分如何工作

| 设置 | 作用 |
|---|---|
| `content` 行 `1`–`6` | 每个键 `1`–`6` 是一行；每个嵌套键 `1`–`9` 是一列。仅当一行有内容或被强制时才显示。 |
| `blueprint_bundle_button` | 一个类型为 `type: BUNDLE` 的可重用按钮。**模板中这个按钮的数量 = 每页显示的捆绑包数。** 添加更多以一次适配更多捆绑包。 |
| `force-shown` | `force-shown: 6` 强制第 1 到 6 行始终渲染（固定高度）。`force-shown: [2,4]` 仅强制第 2 和 4 行。`force-shown: []` （或省略它）让面板自动调整大小以适应其内容。 |
| `type: PREVIOUS` / `type: NEXT` | 分页箭头。它们仅在有比一页能容纳的更多的捆绑包时才出现，所以始终包含它们是安全的。 |
| `unique_id` （可选） | 在按钮的 `data:` 下添加 `unique_id: <bundleId>` 将一个特定捆绑包固定到那个确切的槽位，而不是按顺序填充槽位。 |

## 常见问题

**"我添加了行但菜单仍然很小。"**
一行仅在它有按钮 *或* 它被列在 `force-shown` 中时才显示。确保每个新行实际上包含 `blueprint_bundle_button` 条目，并检查 YAML 缩进（行和列是嵌套在 `content` 下的数字键）。

**"我能做得比 6 行更大吗？"**
不能。6 行 / 54 个槽位是 Minecraft 箱子 GUI 的最大大小，所以它是 `INVENTORY` 类型面板的硬限制。

**"我的改动没有起作用。"**
确认该文件在你正在测试的游戏模式的正确文件夹中（按模式文件夹优先于全局 BentoBox 文件夹），文件名完全是 `island_creation_panel.yml`，编辑后你运行了 `/bentobox reload` 或重启服务器。YAML 语法错误会让 BentoBox 回退到内置默认值——在启动时检查服务器控制台的警告。

**"这也改变了玩家*重置*岛屿时的菜单吗？"**
是的。重置岛屿菜单使用相同的 `island_creation_panel.yml` 模板。

## 另请参阅

- [可自定义的 GUI](Customizable-GUI.md) — 这些菜单建立在其上的通用系统，包括物品/图标选项的完整列表。
- [ItemParser](https://docs.bentobox.world/en/latest/BentoBox/ItemParser/) — `icon:` 字段的语法。
