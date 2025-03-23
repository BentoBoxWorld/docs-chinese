# 传送点

**Warps** 允许玩家在他们的岛屿上添加个人传送标志。

由 [tastybento](https://github.com/tastybento) 创建和维护。

{{ addon_description("Warps") }}

## 安装

1. 将 Warps 插件 jar 文件放入 BentoBox 插件的 addons 文件夹
2. 重启服务器
3. 插件将创建一个数据文件夹,里面有一个 config.yml
4. 根据需要编辑 config.yml。
5. 如果进行了更改,请重启服务器

## 配置

### config.yml

插件成功安装后,它将创建 config.yml 文件。此文件中的每个选项都带有关于它们的注释。请查看文件以获取更多信息。
你可以找到最新的配置文件: [config.yml](https://github.com/BentoBoxWorld/Warps/blob/develop/src/main/resources/config.yml)

??? question "什么是传送限制?"
    这限制了对至少拥有一定岛屿等级的玩家创建传送标志。它需要 Level 插件,默认等级为 10。

??? question "什么是欢迎文本?"
    这是玩家必须放在标志上以使其成为传送标志的文本,例如 [Welcome]。它不区分大小写!

    此文本必须在顶行。

??? question "什么是禁用的游戏模式?"
    此列表存储 Warps 插件不应在其中工作的游戏模式。

    要禁用插件,必须在以 - 开头的新行中写入其名称。示例:
    ```
      disabled-gamemodes:
       - BSkyBlock
    ```

??? question "什么是 lore 格式?"
    Lore 格式允许更改标志中描述行的默认颜色。描述行用于 GUI 中。

    描述行包含在 [welcome] 文本下方的标志行。

??? question "什么是允许在其他世界中?"
    这允许在*任何*世界中放置传送标志,即使是非 BentoBox 世界。

    玩家必须拥有 `welcomewarpsigns.warp` 权限才能使用。

??? question "什么是 warp 和 warps?"
    命令 `warp` 需要 `<player>` 来指定应该传送到哪里,而 `warps` 打开一个菜单,允许选择玩家。

    如果你启用了 `allow in other worlds`,那么它将作为主命令 `/warp`

    而对于每个 BentoBox 游戏模式,它仍将是 `/[player_cmd] warp`

### 可自定义 GUI

BentoBox 1.17 API 引入了一个允许实现可自定义 GUI 的功能。此插件是最早使用此功能的插件之一。我们尽量让自定义变得简单,但有些功能需要解释。
你可以在这里找到更多关于 BentoBox 自定义 GUI 如何工作的信息: [Custom GUI's](/en/latest/Tutorials/generic/Customizable-GUI/)

??? question "我如何自定义 GUI?"
    要自定义插件 GUI,你需要 1.12 版本。这是第一个实现它们的版本。插件将在 `/plugins/BentoBox/addons/Warps` 下创建一个名为 `panels` 的新目录

??? question "`PREVIOUS`|`NEXT` 按钮类型是什么?"
    PREVIOUS 和 NEXT 按钮类型允许在岛屿多于 GUI 中的空间时创建自动分页。
    这些类型在 data 下有额外的参数:

    - `indexing` - 指示按钮是否显示页码。

    示例:
    ```yaml
        icon: tipped_arrow[potion_contents={custom_color:11546150}]
        title: warps.gui.buttons.previous.name
        description: warps.gui.buttons.previous.description
        data:
          type: PREVIOUS
          indexing: true
        action:
          left:
            action: PREVIOUS
            tooltip: warps.gui.tips.click-to-previous
    ```

??? question "`RANDOM` 按钮类型是什么?"
    此按钮允许玩家传送到随机传送点。
    仅当有多个传送点时才可用。

    示例:
    ```yaml
        icon: DROPPER
        title: warps.gui.buttons.random.name
        description: warps.gui.buttons.random.description
        data:
          type: RANDOM
        actions:
          warp:
            click-type: left
            tooltip: warps.gui.tips.click-to-warp
    ```

??? question "`WARP` 按钮类型是什么?"
    WARP 按钮为传送点对象创建一个动态条目。

    指定标题、描述和图标将覆盖基于标志和数据库数据的动态生成。默认情况下,这些值将从数据库条目生成。

    图标 PLAYER_HEAD 将被所有者玩家头替换。但是,目前没有指定不同玩家头的选项。

    示例:
    ```yaml
        warp_button:
          icon: PLAYER_HEAD
          title: warps.gui.buttons.warp.name
          description: warps.gui.buttons.warp.description
          data:
            type: WARP
          actions:
            warp:
              click-type: left
              tooltip: warps.gui.tips.click-to-warp
    ```

## 命令

!!! tip
    `[player_command]` 是根据你运行的游戏模式而不同的命令。
    游戏模式的 `config.yml` 文件包含允许你修改这些值的选项。
    例如,在 BSkyBlock 中,默认的 `[player_command]` 是 `island`。
    请注意,此插件允许在插件 `config.yml` 文件中更改玩家命令别名。

=== "玩家命令"
    - `/[player_command] warp <player>`: 将玩家传送到目标标志。
    - `/[player_command] warps`: 打开允许查看所有可用传送标志的 GUI。

## 权限

!!! tip
    `[gamemode]` 是一个根据你运行的游戏模式而不同的前缀。
    前缀是游戏模式的小写名称,即如果你使用 BSkyBlock,前缀就是 `bskyblock`。
    类似地,如果你使用 AcidIsland,前缀就是 `acidisland`。

=== "玩家权限"
    - `[gamemode].island.warp` - 玩家可以使用 `/[player_command] warp` 和 `/[player_command] warps` 命令。默认启用。
    - `[gamemode].island.addwarp` - 玩家可以创建传送标志。默认启用。
    - `welcomewarpsigns.warp` - 玩家可以使用 `/warp` 和 `/warps` 命令。默认禁用。需要 `allow-in-other-worlds`。
    - `welcomewarpsigns.addwarp` - 玩家可以创建传送标志。默认禁用。需要 `allow-in-other-worlds`。

??? question "有缺失的内容吗?"
    你可以在此插件的 [addon.yml](https://github.com/BentoBoxWorld/Warps/blob/develop/src/main/resources/addon.yml) 文件中找到完整的权限列表。
    如果下面的列表中确实缺少了什么,请告诉我们!

## 常见问题

??? question "你能添加 X 功能吗?"
    请将其添加到[这里](https://github.com/BentoBoxWorld/Warps/issues)的列表中。

??? question "我发现了一个错误,应该在哪里报告它?"
    请将其添加到[这里](https://github.com/BentoBoxWorld/Warps/issues)的列表中。

## 翻译

{{ translations(2973, ["cs", "de", "es", "fr", "hu", "ja", "lv", "pl", "tr", "zh-CN", "zh-TW", "id", "it", "ru", "vi", "uk"]) }}

## Api

### 事件

自 BentoBox 1.17 API 实现了解决类加载器问题的功能。现在想直接使用事件的插件可以这样做。

你只需要将 Visit 添加到你的项目作为依赖。你可以使用 Maven 来做到这一点:

```xml
<dependency>
    <groupId>world.bentobox</groupId>
    <artifactId>warps</artifactId>
    <version>1.11.2</version>
    <scope>provided</scope>
</dependency>
```

=== "WarpInitiateEvent"
    !!! summary "描述"
        玩家创建新的传送标志后触发的事件。

        链接到类: [WarpInitiateEvent](https://github.com/BentoBoxWorld/Warps/blob/develop/src/main/java/world/bentobox/warps/event/WarpInitiateEvent.java)

    !!! question "变量"
        - `UUID player` - 创建传送标志的玩家的 ID。
        - `Location warpLoc` - 传送标志的位置。

    !!! example "代码示例"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onWarpInitiate(WarpInitiateEvent event) {
            UUID player = event.getPlayer();
            Location warpLoc = event.getWarpLoc();
        }
        ```

=== "WarpRemoveEvent"
    !!! summary "描述"
        玩家创建新的传送标志后触发的事件。

        链接到类: [WarpRemoveEvent](https://github.com/BentoBoxWorld/Warps/blob/develop/src/main/java/world/bentobox/warps/event/WarpRemoveEvent.java)

    !!! question "变量"
        - `UUID owner` - 拥有传送标志的玩家的 ID。
        - `UUID remover` - 移除传送标志的玩家的 ID。
        - `Location warpLoc` - 传送标志的位置。

    !!! example "代码示例"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onWarpRemove(WarpRemoveEvent event) {
            UUID owner = event.getOwner();
            UUID remover = event.getRemover();
            Location warpLoc = event.getWarpLocation();
        }
        ```