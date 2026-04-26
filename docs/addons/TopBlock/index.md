# TopBlock

为 BentoBox 专门计算 AOneBlock 岛屿等级的插件。排名由挖掘了多少魔法方块决定 - 计数。

由 [tastybento](https://github.com/tastybento) 创建和维护。

{{ addon_description("TopBlock") }}

## 安装

1. 将 top block 插件 jar 文件放入 BentoBox 插件的 addons 文件夹
2. 重启服务器
3. 插件将创建一个数据文件夹,里面有一个 config.yml
4. 根据需要编辑 config.yml。
5. 如果进行了更改,请重启服务器

## 配置

TopBlock 插件有 2 个通用配置项:

- config.yml 文件包含插件的默认配置。
- /panels/ 包含管理玩家 GUI 的文件。

### config.yml

配置文件包含插件的主要功能。

最新的 config.yml 可以在[这里](https://github.com/BentoBoxWorld/TopBlock/blob/develop/src/main/resources/config.yml)找到。

本节定义了插件的许多整体设置。

??? note "refresh-time"
    前十名应该以分钟为单位刷新的频率。最小值为 1 分钟,默认值为 5 分钟。
    每次刷新都需要从数据库读取每个岛屿,因此不应过于频繁。

    默认值: `5`

??? note "shorthand"
    允许显示较短的岛屿等级数字。

    显示向下取整的大等级值,例如 10,345 -> 10k

    默认值: `false`

### 可自定义 GUI

BentoBox 1.17 API 引入了一个允许实现可自定义 GUI 的功能。我们尽量让自定义变得简单,但有些功能需要解释。
你可以在这里找到更多关于 BentoBox 自定义 GUI 如何工作的信息: [自定义 GUI](/en/latest/Tutorials/generic/Customizable-GUI/)

??? question "我如何自定义 GUI?"
     插件将在 `/plugins/bentobox/addons/topblock` 下创建一个名为 `panels` 的新目录

    目前你可以自定义 GUI:

    - 排行榜面板: `top_panel` - 允许查看前 10 名岛屿。

??? question "`TOP` 按钮类型是什么?"
    此按钮在 top_panel 中可用。它按岛屿排名前 X 显示岛屿。
    
    `icon` 默认为 `PLAYER_HEAD`,带有正确的玩家皮肤。启用它将使用指定的材料替换它。

    data 字段中的 `index` 允许指定当前位置应显示前 10 名中的哪个位置。

    排行榜面板有 2 个实现的操作,功能需要额外的插件:
    
    - `warp` - 需要 Warps 插件。仅当玩家岛屿上存在传送标志时才会显示。
    - `visit` - 需要 Visit 插件。仅当玩家岛屿上允许访问时才会显示。

    Fallback 允许在排行榜位置上没有玩家时更改背景图标。

    示例:
    ```yaml
        #icon: PLAYER_HEAD
        title: topblock.gui.buttons.island.name
        description: topblock.gui.buttons.island.description
        data:
          type: TOP
          index: 1
        actions:
          warp:
            click-type: LEFT
            tooltip: topblock.gui.tips.click-to-warp
          visit:
            click-type: RIGHT
            tooltip: topblock.gui.tips.right-click-to-visit
        fallback:
          icon: LIME_STAINED_GLASS_PANE
          title: topblock.gui.buttons.island.empty
    ```

??? question "`VIEW` 按钮类型是什么?"
    此按钮在 top_panel 中可用。它显示查看者的岛屿 topblock 值。

    `icon` 默认为 `PLAYER_HEAD`,带有正确的玩家皮肤。启用它将使用指定的材料替换它。
    
    `view` 操作允许查看玩家岛屿的详细菜单。

    示例:
    ```yaml
        #icon: PLAYER_HEAD
        title: topblock.gui.buttons.island.name
        description: topblock.gui.buttons.island.description
        data:
          type: VIEW
        actions:
          view:
            click-type: unknown
            tooltip: topblock.gui.tips.click-to-view
    ```

## 命令

!!! tip
    `[player_command]` 和 `[admin_command]` 是根据你运行的游戏模式而不同的命令。
    游戏模式的 `config.yml` 文件包含允许你修改这些值的选项。
    例如,在 BSkyBlock 中,默认的 `[player_command]` 是 `island`,默认的 `[admin_command]` 是 `bsbadmin`。

=== "玩家命令"
    - `/[player_command] topblock`: 访问排行榜面板。需要 `aoneblock.island.topblock` 权限。

## 权限

=== "玩家权限"
    - `aoneblock.island.topblock` - (默认: `true`) - 允许玩家使用 `/[player_command] top` 命令。
    - `aoneblock.intopten` - (默认: `true`) - 控制该玩家的岛屿是否出现在前十名中。从管理员或测试人员处移除此权限可将其排除在排行榜之外。

??? question "有缺失的内容吗?"
    你可以在此插件的 [addon.yml](https://github.com/BentoBoxWorld/TopBlock/blob/develop/src/main/resources/addon.yml) 文件中找到完整的权限列表。
    如果下面的列表中确实缺少了什么,请告诉我们!

## 占位符

{{ placeholders_source(source="TopBlock") }}

## 常见问题

??? question "你能添加 X 功能吗?"
    请将其添加到[这里](https://github.com/BentoBoxWorld/TopBlock/issues)的列表中。

## 更新日志

??? warning "v2.0.0 新内容 — 需要平台升级"
    **发布于：** 2026-04-26

    - 🐛 **前十名面板已修复。** 长期存在的 bug 导致前十名面板只显示空的绿色占位符。事件处理器被设为 `private`，导致 Bukkit 静默跳过注册。现已修复——面板可正确显示玩家头颅和统计数据。
    - ✨ **`aoneblock.intopten` 权限。** 通过移除此权限（默认授予所有玩家），可将管理员和测试人员排除在前十名之外。
    - 🔡 **22 种新语言** — cs, de, es, fr, hr, hu, id, it, ja, ko, lv, nl, pl, pt, pt-BR, ro, ru, tr, uk, vi, zh-CN, zh-HK。
    - 🔺 现在需要 **Paper 1.21.x**、**Java 21**、**BentoBox 3.14.0+** 和 **AOneBlock 1.18.0+**。不再支持 Spigot。

    🔺 重启前**删除 `addons/TopBlock/panels/top_panel.yml`**，以便提取更新后的面板模板。之后重新应用自定义布局更改。

    🔡 更新后运行 `/bentobox reload`，以便 BentoBox 将新的语言键合并到现有语言文件中。

    [Release v2.0.0](https://github.com/BentoBoxWorld/TopBlock/releases/tag/2.0.0)

## 翻译

{{ translations("TopBlock") }}

## API

### Maven 依赖
TopBlock 为其他插件提供了 API。

!!! note
    将 TopBlock 依赖项添加到你的 Maven POM.xml 中:

    ```xml
        <repositories>
            <repository>
                <id>codemc-repo</id>
                <url>https://repo.codemc.io/repository/maven-public/</url>
            </repository>
        </repositories>
        
        <dependencies>
            <dependency>
                <groupId>world.bentobox</groupId>
                <artifactId>topblock</artifactId>
                <version>1.0.1</version>
                <scope>provided</scope>
            </dependency>
        </dependencies>
    ```

TopBlock 的 JavaDoc 可以在[这里](https://ci.codemc.io/job/BentoBoxWorld/job/TopBlock/ws/target/apidocs/index.html)找到。