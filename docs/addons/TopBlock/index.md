# TopBlock

为 BentoBox 生成魔法方块游戏模式前十排名的插件。排名由挖掘了多少魔法方块决定 - 计数。

TopBlock 支持 [**AOneBlock**](../../gamemodes/AOneBlock/index.md) 和 [**ChunkBlock**](../../gamemodes/ChunkBlock/index.md)。你可以安装其中任何一个或两个 —— 当两个都存在时，每个游戏模式都获得自己完全独立的前十、自己的 `topblock` 指令和自己的占位符集。玩家在 AOneBlock 中的排名对其在 ChunkBlock 中的排名没有影响。

由 [tastybento](https://github.com/tastybento) 创建和维护。

{{ addon_description("TopBlock") }}

## 安装

1. 将 top block 插件 jar 文件放入 BentoBox 插件的 addons 文件夹
2. 重启服务器
3. 插件将创建一个数据文件夹,里面有一个 config.yml
4. 根据需要编辑 config.yml。
5. 如果进行了更改,请重启服务器

!!! note "TopBlock 不是独立的"
    TopBlock 需要在其旁边安装至少一个 [AOneBlock](../../gamemodes/AOneBlock/index.md) 或 [ChunkBlock](../../gamemodes/ChunkBlock/index.md)。如果未找到任何一个，TopBlock 会记录错误并禁用自己。它在启动时挂接找到的任何一个，所以在稍后安装或删除游戏模式只有在重启后才会生效。

## 配置

TopBlock 插件有 2 个通用配置项:

- config.yml 文件包含插件的默认配置。
- /panels/ 包含管理玩家 GUI 的文件。

### config.yml

配置文件包含插件的主要功能。

最新的 config.yml 可以在[这里](https://github.com/BentoBoxWorld/TopBlock/blob/develop/src/main/resources/config.yml)找到。

本节定义了插件的许多整体设置。这些设置是全局的 —— 它们适用于 TopBlock 已挂接的每个游戏模式。没有每个游戏模式的配置。

??? note "refresh-time"
    前十名应该以分钟为单位刷新的频率。最小值为 1 分钟,默认值为 5 分钟。
    每次刷新都需要从数据库读取每个已挂接游戏模式的岛屿，因此不应过于频繁（自 2.1.1 起该读取在非主线程上运行，因此不再造成卡顿尖峰）。如果你同时运行 AOneBlock 和 ChunkBlock，每次刷新会读取两套岛屿，所以考虑保留为默认值或提高它。

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

## 指令

!!! tip
    `[player_command]` 和 `[admin_command]` 是根据你运行的游戏模式而不同的指令。
    游戏模式的 `config.yml` 文件包含允许你修改这些值的选项。
    例如,在 BSkyBlock 中,默认的 `[player_command]` 是 `island`,默认的 `[admin_command]` 是 `bsbadmin`。

=== "玩家指令"
    - `/[player_command] topblock`: 访问排行榜面板。需要该游戏模式的 `island.topblock` 权限（`aoneblock.island.topblock` 或 `chunkblock.island.topblock`）。

TopBlock 在它挂接的**每个**游戏模式上注册 `topblock` 子指令，所以在安装了两个的情况下，你会得到 AOneBlock 的 `/ob topblock` 和 ChunkBlock 的等效指令。每个都打开运行它的世界所属游戏模式的面板 —— 两个排行榜完全独立。

## 权限

=== "玩家权限"
    - `aoneblock.island.topblock` - (默认: `true`) - 允许玩家在 AOneBlock 中使用 `/[player_command] topblock` 指令。
    - `aoneblock.intopten` - (默认: `true`) - 控制该玩家的岛屿是否出现在 AOneBlock 前十名中。从管理员或测试人员处移除此权限可将其排除在排行榜之外。
    - `chunkblock.island.topblock` - (默认: `true`) - 允许玩家在 ChunkBlock 中使用 `/[player_command] topblock` 指令。
    - `chunkblock.intopten` - (默认: `true`) - 控制该玩家的岛屿是否出现在 ChunkBlock 前十名中。

??? question "我如何从排行榜中隐藏一个玩家？"
    移除（或否定）该玩家想隐藏的游戏模式的 `intopten` 权限 —— `aoneblock.intopten` 或 `chunkblock.intopten`。由于前缀是按游戏模式的，你可以将某人从一个排行榜中隐藏，同时在另一个中保持可见。

    需要注意两点：

    - 权限仅在岛屿**所有者在线**时检查。离线所有者始终包含，因为 Bukkit 无法为未登录的玩家可靠地评估权限。所以从实际登录的账户移除权限，而不是从小号。
    - 仅检查**岛屿所有者的**权限。队伍成员的权限没有影响。

    更改在下一次刷新时生效，所以允许最多 `refresh-time` 分钟让岛屿从列表中掉下来。

??? question "有缺失的内容吗？"
    你可以在此插件的 [addon.yml](https://github.com/BentoBoxWorld/TopBlock/blob/develop/src/main/resources/addon.yml) 文件中找到完整的权限列表。
    如果下面的列表中确实缺少了什么,请告诉我们!

## 占位符

占位符是为 TopBlock 已挂接的每个游戏模式分别注册的，使用该游戏模式自己的前缀。`chunkblock_` 集仅在 ChunkBlock 已安装时存在，并报告 ChunkBlock 自己的排名 —— 两者从不混合。

{{ placeholders_source(source="TopBlock") }}

## 常见问题

??? question "你能添加 X 功能吗?"
    请将其添加到[这里](https://github.com/BentoBoxWorld/TopBlock/issues)的列表中。

## 更新日志

??? note "v2.1.1 新内容"
    **发布于：** 2026-08-27

    补丁版本 —— 无配置、地区或数据格式更改；即插即用替换 2.1.0。

    - 🐛 **前十刷新不再拖累主线程。** 刷新任务（每 `refresh-time` 分钟，默认 5）在主线程上同步读取游戏模式的整个岛屿数据库 —— 在有许多岛屿的服务器上每个周期最多 ~1 秒，在挂接了 AOneBlock 和 ChunkBlock 时两倍 —— 造成周期性卡顿尖峰。数据库读取现在异步运行；只有便宜的岛屿和权限查找保持在主线程上。

    [发布 v2.1.1](https://github.com/BentoBoxWorld/TopBlock/releases/tag/2.1.1)

??? note "v2.1.0 新内容 — ChunkBlock 支持"
    **发布于：** 2026-08-21

    TopBlock 不再仅限 AOneBlock。它现在支持 **ChunkBlock**，并且可以安装任何一个游戏模式 —— 或同时两个。兼容性：BentoBox API 3.14.0+ · AOneBlock 1.18.0+ 和/或 ChunkBlock 1.0.1+ · Paper Minecraft 1.21.x · Java 21。

    - ✨ **ChunkBlock 支持。** TopBlock 在启动时挂接找到的 AOneBlock 和 ChunkBlock。在安装了两个时，每个保持完全独立的前十、`topblock` 指令和占位符集。
    - ✨ **新占位符** —— 完整的 `%chunkblock_island_*_top_<number>%` 集，镜像现有的 `aoneblock_` 并报告 ChunkBlock 自己的排名。
    - ✨ **新权限** —— `chunkblock.island.topblock` 和 `chunkblock.intopten`，两者默认 `true`，镜像 AOneBlock 等效项。由于前缀是按游戏模式的，你可以将一个玩家从一个排行榜中隐藏，同时在另一个中保持可见。
    - 🔺 **AOneBlock 现在是软依赖。** TopBlock 之前拒绝在没有 AOneBlock 的情况下加载；它现在仅在*没有*受支持的游戏模式存在时禁用自己。现有仅 AOneBlock 的设置不受影响，无需任何更改。
    - 🐛 **每个前十仅显示其自己的游戏模式的岛屿。** AOneBlock 和 ChunkBlock 都在 `database/OneBlockIslands/` 下存储岛屿，所以 ChunkBlock 刷新加载了 AOneBlock 的记录，错误的玩家出现。岛屿现在按游戏模式的世界过滤。
    - 🐛 **前十面板中的 Steve 头部已修复。** 如果 `top_panel.yml` 有 `icon: PLAYER_HEAD` 取消注释，皮肤解析从未被触发，每个头部都渲染为 Steve。面板现在落回到基于名称的头部路径。

    ℹ️ 这是 AOneBlock 服务器的即插即用更新 —— 无需配置、面板或地区更改。

    [发布 v2.1.0](https://github.com/BentoBoxWorld/TopBlock/releases/tag/2.1.0)

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