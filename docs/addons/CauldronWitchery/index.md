# CauldronWitchery

**CauldronWitchery** 允许你的玩家 **使用装满水、岩浆或雪的炼药锅和一根魔法棒来召唤任何种类的生物或物品**。

由 [BONNe](https://github.com/BONNe) 创建和维护。

{{ addon_description("CauldronWitchery", beta=True) }}

## 安装

1. 将插件 jar 文件放入 BentoBox 插件的 addons 文件夹
2. 启动服务器 
3. 运行管理员命令,例如 `/[admin_cmd] witchery` 来配置插件

## 配置

与挑战、生物群系和生成器类似,Cauldron Witchery 将所有数据存储在数据库中。配置文件包含有关插件及其运行方式的通用选项,而其他所有内容,如魔法棒和玩家数据都存储在数据库中。

### config.yml

最新的 config.yml 可以在[这里](https://github.com/BentoBoxWorld/CauldronWitchery/blob/develop/src/main/resources/config.yml)找到。

### 模板

CauldronWitchery 插件包含一个模板文件,可用于将魔法棒导入数据库。这个文件对于不喜欢使用游戏内 GUI 的人来说,批量添加数据非常有用。但是请注意,模板文件并非支持所有功能,有些物品/选项只能通过 GUI 添加。
你可以拥有任意数量的模板文件。管理员 GUI 将允许选择要导入的文件。
示例模板文件: [template.yml](https://github.com/BentoBoxWorld/CauldronWitchery/blob/develop/src/main/resources/template.yml)

!!! tip
    模板文件必须包含 `magic-sticks`。

??? question "我可以为魔法棒指定附魔吗?"
    不幸的是,Spigot 没有通用的物品解析机制。所以插件作者需要自己创建。CauldronWitchery 插件使用 BentoBox 的[物品解析器](/en/latest/BentoBox/ItemParser/)。如果它不支持某个功能,那么你就不能使用。

    但是,你始终可以使用游戏内管理员 GUI 来设置你想要的任何物品。没有任何限制。

??? question "我添加的配方没有被识别。可能是什么原因?"
    可能有几个原因。如果有明显的错误,日志文件应该包含相应的错误消息。

    但是,你可以先检查所有配方是否以 `- ` 开头,以及每个物品(原料、炼药锅、等级等)是否与左侧对齐。

    另一个原因可能是实体、物品或书籍不存在。你应该检查它们的输入是否正确。

### 书籍 

书籍是玩家如何找到配方的方式。书籍是非常可定制的,但请注意,标题、作者和页面有字符限制。我建议先在游戏中用成书尝试创建书籍,然后再将其放入翻译文件中。

??? question "我可以为书籍添加自己的翻译吗?"
    是的,你当然可以。你可以通过 [book_id]-[locale_code].yml 添加,或者更改现有的文件。

??? question "我可以禁用自动生成配方吗?"
    可以,只需从书籍中删除 `recipe` 部分即可。

??? question "我可以添加更多书籍吗?"
    可以,只需在 `books` 目录下创建一个新文件。文件必须命名为 `[book_id]-[locale_code].yml`,并且必须以 `[book_id]:` 开头。

## 可自定义的 GUI

BentoBox 1.17 API 引入了一个允许实现可自定义 GUI 的功能。这个插件是最早使用此功能的插件之一。我们尽量让自定义变得简单,但有些功能需要解释。
你可以在这里找到更多关于 BentoBox 自定义 GUI 如何工作的信息: [自定义 GUI](/en/latest/Tutorials/generic/Customizable-GUI/)

??? question "我如何自定义 GUI?"
    要自定义插件的 GUI,你需要 2.0 版本。这是第一个实现它们的版本。插件会在 `/plugins/BentoBox/addons/CauldronWitchery` 下创建一个名为 `panels` 的新目录。

    目前你可以自定义 2 个 GUI:

    - 魔法棒面板: `stick_panel` - 包含所有魔法棒的面板,用户可以购买或获得它们。
    - 配方面板: `recipe_panel` - 包含魔法棒可用的所有配方的面板。 

    每个 GUI 都包含仅由其自身支持的功能。

??? question "`PREVIOUS`|`NEXT` 按钮类型是什么?"
    PREVIOUS 和 NEXT 按钮类型允许在魔法棒或配方多于 GUI 中的空间时创建自动分页。
    这些类型在 data 下有额外的参数:

    - `indexing` - 指示按钮是否显示页码。

    示例:
    ```yaml
        icon: tipped_arrow[potion_contents={custom_color:11546150}]
        title: cauldron-witchery.gui.buttons.previous.name  
        description: cauldron-witchery.gui.buttons.previous.description
        data:
          type: PREVIOUS
          indexing: true
        action:
          left:
            tooltip: cauldron-witchery.gui.tips.click-to-previous
    ```

??? question "`RETURN` 按钮类型是什么?"
    RETURN 按钮类型在 recipe_panel 中可用。它允许返回到魔法棒面板。

    示例:
    ```yaml
        icon: OAK_DOOR
        title: cauldron-witchery.gui.buttons.return.name
        description: cauldron-witchery.gui.buttons.return.description
        data:
          type: RETURN
        action:
          left:
            tooltip: cauldron-witchery.gui.tips.click-to-return
    ```

??? question "`STICK` 按钮类型是什么?"
    此按钮在 stick_panel 中可用。
    STICK 按钮为魔法棒创建一个动态条目。只有存在魔法棒时,按钮才会被填充。例如,如果你只有 3 根魔法棒,但在 GUI 中为它们定义了 7 个位置,那么只有 3 个位置会被填充。其他位置将保持为空。

    默认情况下,魔法棒将按照它们的顺序号排序,但是,你可以使用 data 下的 `id` 参数指定特定的魔法棒放在特定的位置。

    ```yaml
      data:
        type: STICK
        id: example_stick
    ```

    指定标题、描述和图标将覆盖基于数据库数据的动态生成。默认情况下,这些值将从数据库条目生成。
    此按钮支持 2 种不同的操作类型:

    - RECIPES - 打开配方视图面板
    - PURCHASE - 为玩家购买或给予魔法棒。

    示例:
    ```yaml
      data:
        type: STICK
      actions:
        left:
          type: RECIPES
          tooltip: cauldron-witchery.gui.tips.left-click-to-view
        right:
          type: PURCHASE  
          tooltip: cauldron-witchery.gui.tips.right-click-to-buy
    ```

??? question "`RECIPE` 按钮类型是什么?"
    此按钮在 recipe_panel 中可用。
    RECIPE 按钮为配方创建一个动态条目。只有存在配方时,按钮才会被填充。例如,如果你只有 3 个配方,但在 GUI 中为等级定义了 7 个位置,那么只有 3 个位置会被填充。其他位置将保持为空。

    默认情况下,配方将按照它们的顺序号排序,然后按照奖励物品名称排序。
    指定标题、描述和图标将覆盖基于数据库数据的动态生成。默认情况下,这些值将从数据库条目生成。

    示例:
    ```yaml
      data:
        type: RECIPE
    ```

## 常见问题

??? question "配方如何工作?"
    所有配方都需要 3 样东西:

    - 玩家主手中的魔法棒
    - 玩家副手中的主要原料
    - 额外原料

    额外原料必须丢入炼药锅或保存在物品栏中。这取决于插件的配置选项: `mix-in-cauldron`。如果禁用该选项,则物品必须在玩家的物品栏中。

    如果没有任何缺失,配方就会生效。

??? question "我可以添加自定义魔法棒物品吗?"
    可以,只要 Spigot 支持它们。但是,你无法通过模板文件来实现。只有管理员 GUI 支持添加自定义物品。

??? question "玩家如何获得魔法棒?"
    玩家可以使用 `/[player_cmd] witchery` 命令购买魔法棒。

    管理员也可以创建自己的分发魔法棒的方式。有一个管理员命令可以生成它们:

    `/[admin_cmd] witchery get stick <stick_id>`

??? question "主要原料和额外原料有什么区别?"
    主要原料始终是玩家需要的"最后"一个物品。它始终是玩家副手中的物品。

    额外原料是必须在玩家物品栏中或丢入炼药锅中的物品(取决于配置)。

??? question "物品在岩浆炼药锅中不会燃烧,也不会消失?"
    如果在插件设置中启用了 `mix-in-cauldron` 选项,那么岩浆炼药锅中的物品不会燃烧,也不会消失。
    这对插件的运行是必要的,因为可能有需要岩浆炼药锅的配方。如果物品会燃烧掉,这些配方就无法完成。
    仅作为保护措施禁用了炼药锅内物品消失。

??? question "我岛上的任何人都可以使用魔法棒。我可以阻止吗?"
    可以,你可以使用岛屿保护标志限制哪些用户组可以使用魔法棒。
    CauldronWitchery 添加了 `CAULDRON_WITCHERY_ISLAND_PROTECTION`,可以从岛屿访客切换到所有者。

    不属于成员组的用户将无法在岛上使用魔法棒。

??? question "你能添加 X 功能吗?"
    请将其添加到[这里](https://github.com/BentoBoxWorld/CauldronWitchery/issues)的列表中。


## 翻译

{{ translations(2976, ["lv", "zh-CN"]) }}