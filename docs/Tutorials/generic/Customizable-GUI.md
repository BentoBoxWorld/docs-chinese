## 可自定义的 GUI

BentoBox 1.17 引入了 GUI 自定义 API。不过由于需要做的更改很多，目前还不是所有的功能都可以自定义，只有少数插件已经实现了这个功能。

可自定义 GUI 的例子：
```yaml
# 面板的名称。必须与文件名相同。
panel_name:
  # 面板的标题
  title: "The Panel Title"
  # 面板类型：
  # INVENTORY - 箱子 GUI 类型
  # HOPPER - 漏斗 GUI 类型
  # DROPPER - 投掷器 GUI 类型
  type: INVENTORY
  # 空位的背景物品
  background:
    # 元素的图标。
    # 写法格式见：https://docs.bentobox.world/zh-cn/latest/BentoBox/ItemParser/
    icon: BLACK_STAINED_GLASS_PANE
    # 元素的标题
    title: "&b&r" # 空文本
    # 元素的描述
    description: "I am background"
  # 边框位置的物品
  border:
    # 元素的图标。
    # 写法格式见：https://docs.bentobox.world/zh-cn/latest/BentoBox/ItemParser/
    icon: BLACK_STAINED_GLASS_PANE
    # 元素的标题
    title: "&b&r" # 空文本
    # 元素的描述
    description: "I am border"
  # 必须始终显示的行
  force-shown: [2,4]
  # GUI 的内容。
  content:
    # 行号，从 1 到 6
    2:
      # 列号
      2: reusable_button_one
      3: reusable_button_one
      4: reusable_button_one
      5: reusable_button_one
      6: reusable_button_one
      7: reusable_button_one
      8: reusable_button_one
    3:
      1:
        # 元素的图标。
        # 写法格式见：https://docs.bentobox.world/zh-cn/latest/BentoBox/ItemParser/
        icon: tipped_arrow[potion_contents={custom_color:11546150}]
        # 元素的标题。
        title: "Button One"
        # 元素的描述
        description: "Button description"
        # 数据用于定义一些由插件使用的函数。
        # 其内容取决于插件/GUI 的实现。
        data:
          type: ADDON_THING
        # 动作用于指定按钮应执行什么操作。插件可以指定额外的参数。
        action:
          # 可用选项可在此处找到：[ClickType](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/inventory/ClickType.html)
          left:
            # 插件可以定义一种点击类型。
            type: ADDON_THING
            # 工具提示是将被添加到按钮描述末尾的文本。
            tooltip: "Tooltip for a button"
      9:
        # 元素的图标。
        # 写法格式见：https://docs.bentobox.world/zh-cn/latest/BentoBox/ItemParser/
        icon: STONE
        # 元素的标题。
        title: "Button Twi"
        # 元素的描述
        description: "Button description"
        # 数据用于定义一些由插件使用的函数。
        # 其内容取决于插件/GUI 的实现。
        data:
          type: ADDON_THING
        # 动作用于指定按钮应执行什么操作。插件可以指定额外的参数。
        action:
          # 可用选项可在此处找到：[ClickType](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/inventory/ClickType.html)
          left:
            # 插件可以定义一种点击类型。
            type: ADDON_THING
            # 工具提示是将被添加到按钮描述末尾的文本。
            tooltip: "Tooltip for a button"
    5:
      2: reusable_button_two
      3: reusable_button_two
      4: reusable_button_two
      5: reusable_button_two
      6: reusable_button_one
      7: reusable_button_two
      8: reusable_button_two
  # 在内容部分多次使用的可复用按钮。
  reusable:
    # 可复用项的 ID
    reusable_button_one:
      # 元素的图标。
      # 写法格式见：https://docs.bentobox.world/zh-cn/latest/BentoBox/ItemParser/
      icon: GLASS
      # 元素的标题。
      title: "Reusable Button One"
      # 元素的描述
      description: "Button description"
      # 数据用于定义一些由插件使用的函数。
      # 其内容取决于插件/GUI 的实现。
      data:
        type: ADDON_THING
      # 动作用于指定按钮应执行什么操作。插件可以指定额外的参数。
      action:
        # 可用选项可在此处找到：[ClickType](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/inventory/ClickType.html)
        left:
          # 插件可以定义一种点击类型。
          type: ADDON_THING
          # 工具提示是将被添加到按钮描述末尾的文本。
          tooltip: "Tooltip for a button"
    reusable_button_two:
      # 元素的图标。
      # 写法格式见：https://docs.bentobox.world/zh-cn/latest/BentoBox/ItemParser/
      icon: DIRT
      # 元素的标题。
      title: "Reusable Button Two"
      # 元素的描述
      description: "Button description"
      # 数据用于定义一些由插件使用的函数。
      # 其内容取决于插件/GUI 的实现。
      data:
        type: ADDON_THING
      # 动作用于指定按钮应执行什么操作。插件可以指定额外的参数。
      action:
        # 可用选项可在此处找到：[ClickType](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/inventory/ClickType.html)
        left:
          # 插件可以定义一种点击类型。
          type: ADDON_THING
          # 工具提示是将被添加到按钮描述末尾的文本。
          tooltip: "Tooltip for a button"
```

### 常见问题

??? question "我可以设置多语言标题和描述吗？"
    可以。GUI 中的每段文本都会尝试使用 BentoBox 本地化。这意味着如果您指定的文本链接到翻译字符串，它将使用该翻译。
    例如：
    ```yaml
    tooltip: panels.tooltips.left
    ```
    将尝试从 BentoBox 的任何本地化中获取翻译字符串：
    ```yaml
    panels:
      tooltips:
        left: "Left Click Tooltip"
    ```

??? question "type 是什么？"
    在 Spigot 插件中，您可以指定 3 种玩家可以交互的物品栏类型：
    - `INVENTORY` - 简单物品栏，如箱子，有 27 至 54 个格子。
    - `HOPPER` - 漏斗物品栏，有 5 个格子。
    - `DROPPER` - 投掷器物品栏，有 9 个格子。
    
    其他物品栏，如附魔台和砧，不被 Spigot 支持，需要额外的插件。这就是为什么 BentoBox 目前不支持它们。

??? question "background 是什么？"
    背景物品允许为 GUI 中所有将留空的位置设置统一的物品。
    它需要有图标和标题。如果您不想使用它，只需删除 `background` 行。
    `background` 下唯一必需的东西是图标。`title` 和 `description` 可以删除。
    ```yaml
        icon: BLACK_STAINED_GLASS_PANE
        title: "背景物品的标题"
        description: "背景物品的描述"
    ```

??? question "border 是什么？"
    边框物品允许为 GUI 四周设置统一的物品。它只会替换空位。
    它需要有图标和标题。如果您不想使用它，只需删除 `border` 行。
    `background` 下唯一必需的东西是图标。`title` 和 `description` 可以删除。
    ```yaml
        icon: BLACK_STAINED_GLASS_PANE
        title: "边框物品的标题"
        description: "边框物品的描述"
    ```

??? question "我可以设置空文本并隐藏工具提示吗？"
    不幸的是，Minecraft 服务器无法为客户端禁用文本和工具提示渲染。只有对于模组客户端（如 Fabric 或 Forge），才能做到。
    最接近的方法是使用空文本：`&b&r`


??? question "`force-shown` 是什么？"
    在物品栏 GUI 中，我们尝试删除所有完全空的行。这允许根据其中可用元素的数量动态设置 GUI 的大小。但是，有时您可能想始终看到特定的行。`force-shown` 选项允许您这样做，您可以列出行号（从 0 到 6）。

??? question "reusable 是什么？"
    在某些 GUI 中，您可能会有许多需要指定的重复项，如挑战或生物群系。`reusable` 允许您创建一个元素，该元素将在内容部分需要该对象的所有地方被替换。

??? question "如何正确填充 `content`？"
    内容需要首先指定行号（从 1 到 6），然后为每个按钮指定列号（从 1 到 9）。不需要指定每个格子，只需指定您想填充的那些。其他的将是空的、背景或边框。
    
    请注意，某些 GUI 类型没有多行或列数较少。

??? question "按钮的 `data` 是什么？"
    数据是我们为插件实现自定义函数功能的方式。例如，挑战插件有两种数据类型：CHALLENGE 和 LEVEL。每个插件都有自己的数据，可能包含多个类型。

??? question "按钮的 `actions` 是什么？"
    `actions` 允许实现不同的操作，这些操作会在玩家对按钮进行不同点击时发生。
    所有点击选项可在此处找到：[ClickType](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/event/inventory/ClickType.html)
    请注意，并非所有选项都可由玩家使用。

    `action` 支持工具提示生成。工具提示将始终添加到按钮描述的末尾，并按操作的顺序排列。
