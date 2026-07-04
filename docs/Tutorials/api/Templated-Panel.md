# BentoBox TemplatedPanel 文档

BentoBox TemplatedPanel 是一个强大的工具，为 Minecraft 开发者提供便利，让他们可以轻松创建可自定义的基于物品栏的用户界面（UI）。通过在 YAML 中定义面板布局，开发者可以快速调整 UI 元素，而无需进行大量代码修改。以下是如何使用 YAML 配置 TemplatedPanel 的详细说明。

## 面板定义

### 面板识别
- `detail_panel`：为面板定义唯一的名称，以便在代码中引用。

### 面板标题
- `title`：设置面板的显示标题。此标题可以通过本地化文件中的引用进行本地化。

### 面板类型
- `type`：选择要显示的物品栏类型。选项包括 `INVENTORY`、`HOPPER` 和 `DROPPER`。

### 背景和边框
- `background`：使用 Minecraft 物品自定义面板的背景。例如，`BLACK_STAINED_GLASS_PANE` 可用于美观效果。
- `border`：定义面板边框的外观，同样使用 Minecraft 物品。这有助于突出面板物品。

### 显示配置
- `force-shown`：指定面板中要显示的行，影响面板的垂直大小。

## 内容配置

### 按钮布局和功能
- `content`：在此部分中，详细说明面板中的每个物品或按钮。使用行号和列号来定位每个元素。
  - `icon`：设置用作按钮图标的 Minecraft 物品。
  - `title`：为按钮提供标题，可以本地化。
  - `description`：为按钮添加描述，也可本地化。
  - `data`：包含与按钮功能相关的数据，例如它触发的操作类型。
  - `actions`：定义与按钮交互时发生的操作，指定点击类型和任何工具提示。

### 可复用按钮
- `reusable`：为在面板中多次使用的按钮定义模板。
  - 在此部分中，指定按钮的图标、标题、描述和关联数据等详细信息。

## 按钮配置示例
- 对于第 1 行第 2 列的按钮：
  ```yaml
  1:
    2:
      icon: STONE
      title: level.gui.buttons.all_blocks.name
      description: level.gui.buttons.all_blocks.description
      data:
        type: TAB
        tab: ALL_BLOCKS
      actions:
        view:
          click-type: unknown
          tooltip: level.gui.tips.click-to-view
  ```

- 对于名为 `material_button` 的可复用按钮：
  ```yaml
  reusable:
    material_button:
      title: level.gui.buttons.material.name
      description: level.gui.buttons.material.description
      data:
        type: BLOCK
  ```

TemplatedPanel 系统为 BentoBox 开发者提供了一种流畅而灵活的方式来设计和实现游戏中的交互式 UI 元素，增强用户体验和功能。

# TemplatedPanelBuilder 文档

`TemplatedPanelBuilder` 类是 BentoBox API 的一部分，旨在便于创建 `TemplatedPanel` 对象。它提供了一个流畅的接口来构建具有各种自定义选项的面板，例如模板、用户上下文、世界上下文和监听器。以下是其功能和用法的概览。

## 类概览

`TemplatedPanelBuilder` 用于构建 `TemplatedPanel` 的实例。它允许设置各种参数和配置，这些参数和配置对于面板在 Minecraft 世界中的运行是必需的，特别是在 BentoBox 框架内。

## 方法

### 模板方法

- `template(String guiName, File dataFolder)`：基于 GUI 名称和数据文件夹为面板设置模板。返回 `TemplatedPanelBuilder` 实例以进行链式调用。
- `template(String panelName, String templateName, File dataFolder)`：基于面板名称、模板名称和数据文件夹为面板设置模板。在 1.20.0 版本中引入。返回 `TemplatedPanelBuilder` 实例以进行链式调用。

### 用户方法

- `user(User user)`：为正在构建的面板设置用户。返回 `TemplatedPanelBuilder` 实例以进行链式调用。

### 世界方法

- `world(World world)`：为面板设置世界上下文。返回 `TemplatedPanelBuilder` 实例以进行链式调用。

### 参数方法

- `parameters(@NonNull String... parameters)`：为面板标题设置参数。返回 `TemplatedPanelBuilder` 实例以进行链式调用。自 1.20.0 版本可用。
- 示例：`panelBuilder.parameters("[name]", this.user.getName());` 将用户名称放入面板标题中。

### 监听器方法

- `listener(PanelListener listener)`：为面板添加 `PanelListener` 以处理用户交互。返回 `TemplatedPanelBuilder` 实例以进行链式调用。
- 监听器不是必需的，因为切换到另一个标签页或对点击做出反应的功能已在 API 中处理。
- 只有在需要自定义功能时才可能需要监听器。

### 类型构建器注册

- `registerTypeBuilder(String type, BiFunction<ItemTemplateRecord, TemplatedPanel.ItemSlot, PanelItem> buttonCreator)`：为面板注册一个新的按钮类型构建器。返回 `TemplatedPanelBuilder` 实例以进行链式调用。
- 示例：
```
        panelBuilder.registerTypeBuilder("NEXT", this::createNextButton);
        panelBuilder.registerTypeBuilder("PREVIOUS", this::createPreviousButton);
        panelBuilder.registerTypeBuilder("BLOCK", this::createMaterialButton);
```
- 当单击具有关联名称的按钮时，将调用相应的方法。它被传入 ItemTemplateRecord、ItemSlot 和 PanelItem。

### 构建方法

- `build()`：根据提供的配置构建并返回一个 `TemplatedPanel` 实例。

## 获取器

- `getPanelTemplate()`：检索当前的 `PanelTemplateRecord`。
- `getUser()`：获取与面板关联的 `User` 对象。
- `getWorld()`：返回面板的 `World` 上下文。
- `getParameters()`：检索为面板标题设置的参数列表。
- `getListener()`：返回附加到面板的 `PanelListener`。
- `getObjectCreatorMap()`：提供对将对象与其面板物品创建者链接的映射的访问。

## 变量

- `panelTemplate`：存储 GUI 模板记录。
- `user`：保存打开 GUI 的用户的引用。
- `world`：代表 GUI 运行的世界。
- `listener`：存储用于处理 GUI 交互的 `PanelListener`。
- `parameters`：用于存储标题对象参数的列表。
- `objectCreatorMap`：将对象类型链接到其各自的面板物品创建者的映射。

## 用法

要使用 `TemplatedPanelBuilder`，请实例化它并链式调用其方法来根据需要配置面板。设置所有配置后，调用 `build()` 方法来创建 `TemplatedPanel` 实例。

示例：

```
        // 开始构建面板。
        TemplatedPanelBuilder panelBuilder = new TemplatedPanelBuilder();
        panelBuilder.user(this.user);
        panelBuilder.world(this.user.getWorld());

        panelBuilder.template("detail_panel", new File(this.addon.getDataFolder(), "panels"));

        panelBuilder.parameters("[name]", this.user.getName());

        panelBuilder.registerTypeBuilder("NEXT", this::createNextButton);
        panelBuilder.registerTypeBuilder("PREVIOUS", this::createPreviousButton);
        panelBuilder.registerTypeBuilder("BLOCK", this::createMaterialButton);

        panelBuilder.registerTypeBuilder("FILTER", this::createFilterButton);

        // 注册标签页
        panelBuilder.registerTypeBuilder("TAB", this::createTabButton);

        // 注册未知类型构建器。
        panelBuilder.build();
```

