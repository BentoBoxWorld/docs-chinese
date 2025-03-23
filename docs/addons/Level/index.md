# Level

**Level** 可让你的玩家通过放置方块来提升岛屿等级,竞争最高的岛屿等级!

由 [tastybento](https://github.com/tastybento) 创建和维护。

{{ addon_description("Level") }}

## 安装

1. 将 level 插件 jar 文件放入 BentoBox 插件的 addons 文件夹
2. 重启服务器 
3. 插件将创建一个数据文件夹,里面有一个 config.yml 文件
4. 根据需要编辑 config.yml。该配置文件指定方块的价值(见下文)
5. 如果进行了更改,请重启服务器

## 配置

Level 插件有 3 个通用配置项:

- config.yml 文件包含插件的默认配置。
- blockconfig.yml 文件包含每个方块的价值。
- /panels/ 包含管理玩家 GUI 的文件。

### config.yml

配置文件包含插件的主要功能。

最新的 config.yml 可以在[这里](https://github.com/BentoBoxWorld/Level/blob/develop/src/main/resources/config.yml)找到。

本节定义了插件的许多整体设置。

??? note "disabled-game-modes"
    允许指定 Level 插件不应在哪些游戏模式插件中运行。
    
    Level 将不会与这些游戏模式插件挂钩。

    默认值: `[]`

??? note "log-report-to-console"
    如果从控制台执行命令,则允许查看等级报告。

    默认值: `true`

??? note "concurrent-island-calcs" 
    允许指定一次可以进行多少个岛屿等级计算。

    如果队列中有多个,且你的 CPU 可以处理,你可以并行运行岛屿计算。

    默认值: `1`

??? note "calculation-timeout"
    允许指定等级计算应在多少分钟后停止。

    一般来说,计算只需要几秒钟,所以如果这个值被触发,说明有些不对劲。

    默认值: `5`

??? note "zero-new-island-levels"
    允许指定起始方块是否应包含在岛屿等级中。

    如果为 true,Level 将计算初始岛屿的等级,并将其从任何未来的等级计算中移除。
    如果移除所有起始方块,玩家等级可能会变成负值。
    
    如果为 false,玩家的初始岛屿方块将计入他们的等级。

    默认值: `true`

??? note "login"
    允许设置在玩家登录时计算岛屿等级。

    这会在玩家登录时静默计算他们的岛屿等级。

    默认值: `false`

??? note "nether"
    允许在等级计算中包含下界岛屿。

    警告:在游戏中途启用此选项会让拥有岛屿的玩家的岛屿等级突然提高。新岛屿将被正确归零。

    默认值: `false`

??? note "end"
    允许在等级计算中包含末地岛屿。

    警告:在游戏中途启用此选项会让拥有岛屿的玩家的岛屿等级突然提高。新岛屿将被正确归零。

    默认值: `false`

??? note "include-chests"
    允许在等级计算中包含箱子内容。

    警告:等级计算时间会更长,服务器性能可能受到影响。

    默认值: `false`

??? note "underwater"
    允许指定水下方块倍数。

    如果方块低于海平面,它们可以有更高的价值。例如 2 倍。
    如果有海洋,则可以促进水下开发。该值可以是小数。

    默认值: `1.0`

??? note "levelcost"
    允许指定一个岛屿等级的价值。

    默认值: `100`

    最小值: `1`

??? note "level-calc"
    允许指定等级计算公式。

    * blocks - 所有方块价值的总和,减去任何死亡惩罚
    * level_cost - 在线性方程中,一个等级的价值

    此公式可以包括 +、=、*、/、sqrt、^、sin、cos、tan、log(自然对数)。
    结果将始终四舍五入为长整数。

    例如,另一个非线性选项可以是: `3 * sqrt(blocks / level_cost)`

    默认值: `blocks / level_cost`

??? note "levelwait" 
    允许指定等级请求之间的冷却时间(秒)。

    默认值: `60`

??? note "deathpenalty"
    允许指定死亡惩罚。

    玩家每死一次将损失多少方块价值。
    默认值 100 意味着每死一次,玩家将损失 1 级(如果 levelcost 为 100)。

    设置为零可不使用此功能。

    默认值: `100`

??? note "sumteamdeaths"
    允许对死亡惩罚中的所有队员求和。

    如果为 false,则只计算队长的死亡次数。

    默认值: `false`

??? note "shorthand"
    允许显示较短的岛屿等级数字。

    显示向下取整的大等级值,例如 10,345 -> 10k

    默认值: `false`

### blockconfig.yml

方块配置文件包含方块的价值。

最新的 blockconfig.yml 可以在[这里](https://github.com/BentoBoxWorld/Level/blob/develop/src/main/resources/blockconfig.yml)找到。

本节定义了方块的价值和限制。

!!! tip
    此文件中的值仅支持整数 -> 完整数字。

!!! tip
    正确的材料名称可以在 Spigot 材料页面找到。

    注意:这是最新的 spigot 材料列表: [材料](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)

??? note "limits"
    本节列出了任何特定方块的限制。
    超过此数量的方块不会被计算。
    此限制适用于所有游戏模式,不是特定于世界的。

    格式: `MATERIAL: NUMBER`

??? note "blocks"
    本节列出了所有游戏模式(世界)中方块的价值。
    要指定特定世界的价值,请使用下一节。
    任何未列出的方块将具有 0 的价值。空气始终为零。

    格式: `MATERIAL: NUMBER`

??? note "worlds" 
    列出在特定世界中具有不同价值的任何方块。
    如果未列出某个方块,将使用 blocks 部分的默认值。
    以世界名称为前缀。如果存在,这些值将应用于相关的下界和末地。

    示例:

    ```
        worlds:
          AcidIsland_world:
            SAND: 0
            SANDSTONE: 0
            ICE: 0
    ```

    在此示例中,AcidIsland 将对所有方块使用与 BSkyBlock 相同的值,除了沙子、沙石和冰。

### 可自定义 GUI

BentoBox 1.17 API 引入了一个允许实现可自定义 GUI 的功能。我们尽量让自定义变得简单,但有些功能需要解释。
你可以在这里找到更多关于 BentoBox 自定义 GUI 如何工作的信息: [自定义 GUI](/en/latest/Tutorials/generic/Customizable-GUI/)

??? question "我如何自定义 GUI?"
    要自定义 Level 插件的 GUI,你需要 2.10.0 版本。这是第一个实现它们的版本。插件将在 `/plugins/bentobox/addons/level` 下创建一个名为 `panels` 的新目录。

    目前你可以自定义 3 个 GUI:

    - 排行榜面板: `top_panel` - 允许查看前 10 名岛屿。
    - 详细方块面板: `detail_panel` - 允许在游戏中查看详细的方块价值列表。 
    - 方块价值面板: `value_panel` - 允许在游戏中查看每个方块的价值。

    每个 GUI 都包含仅由其自身支持的功能。

??? question "`PREVIOUS`|`NEXT` 按钮类型是什么?"
    此按钮在 detail_panel 和 value_panel 中可用。
    PREVIOUS 和 NEXT 按钮类型允许在方块多于 GUI 中的空间时创建自动分页。
    这些类型在 data 下有额外的参数:

    - `indexing` - 指示按钮是否显示页码。

      示例:
      ```yaml
          icon: tipped_arrow[potion_contents={custom_color:11546150}]
          title: level.gui.buttons.previous.name
          description: level.gui.buttons.previous.description
          data:
            type: PREVIOUS
            indexing: true
          action:
            left:
              tooltip: level.gui.tips.click-to-previous
      ```

??? question "`TOP` 按钮类型是什么?"
    此按钮在 top_panel 中可用。它按岛屿等级显示排名前 X 的岛屿。

    `icon` 默认为 `PLAYER_HEAD`,带有正确的玩家皮肤。启用它将使用指定的材料替换它。

    data 字段中的 `index` 允许指定当前位置应显示前 10 名中的哪个位置。

    排行榜面板有 2 个实现的操作,功能需要额外的插件:

    - `warp` - 需要 Warps 插件。仅当玩家岛屿上存在传送标志时才会显示。
    - `visit` - 需要 Visit 插件。仅当玩家岛屿上允许访问时才会显示。

    Fallback 允许在排行榜位置上没有玩家时更改背景图标。

    示例:
    ```yaml
        #icon: PLAYER_HEAD
        title: level.gui.buttons.island.name
        description: level.gui.buttons.island.description
        data:
          type: TOP
          index: 1
        actions:
          warp:
            click-type: LEFT
            tooltip: level.gui.tips.click-to-warp
          visit:
            click-type: RIGHT
            tooltip: level.gui.tips.right-click-to-visit
        fallback:
          icon: LIME_STAINED_GLASS_PANE
          title: level.gui.buttons.island.empty
    ```

??? question "`VIEW` 按钮类型是什么?"
    此按钮在 top_panel 中可用。它显示查看者的岛屿等级。

    `icon` 默认为 `PLAYER_HEAD`,带有正确的玩家皮肤。启用它将使用指定的材料替换它。

    `view` 操作允许查看玩家岛屿的详细菜单。

    示例:
    ```yaml
        #icon: PLAYER_HEAD
        title: level.gui.buttons.island.name
        description: level.gui.buttons.island.description
        data:
          type: VIEW
        actions:
          view:
            click-type: unknown
            tooltip: level.gui.tips.click-to-view
    ```

??? question "`BLOCK` 按钮类型是什么?"
    此按钮在 detail_panel 和 value_panel 中可用。此按钮将给定材料显示为图标。

    示例:
    ```yaml
      #icon: STONE
      title: level.gui.buttons.value.name
      description: level.gui.buttons.value.description
      data:
        type: BLOCK
    ```

## 命令

!!! tip
    `[player_command]` 和 `[admin_command]` 是根据你运行的游戏模式而不同的命令。
    游戏模式的 `config.yml` 文件包含允许你修改这些值的选项。
    例如,在 BSkyBlock 中,默认的 `[player_command]` 是 `island`,默认的 `[admin_command]` 是 `bsbadmin`。

=== "玩家命令"
    - `/[player_command] top`: 访问排行榜面板。需要 `[gamemode].island.top` 权限。
    - `/[player_command] level`: 触发玩家的等级计算。需要 `[gamemode].island.level` 权限。
    - `/[player_command] value [material]`: 允许检查方块价值。需要 `[gamemode].island.value` 权限。

=== "管理员命令"
    - `/[admin_command] level <player>`: 触发玩家的等级计算。需要 `[gamemode].admin.level` 权限。
    - `/[admin_command] levelstatus`: 显示有多少岛屿在队列中。需要 `[gamemode].admin.levelstatus` 权限。
    - `/[admin_command] sethandicap <player> <number>`: 允许设置岛屿等级的初始数值。需要 `[gamemode].admin.level.sethandicap` 权限。
    - `/[admin_command] top`: 在聊天中显示前 10 名岛屿。需要 `[gamemode].admin.top` 权限。
    - `/[admin_command] top remove <player>`: 允许从排行榜中移除玩家。需要 `[gamemode].admin.top.remove` 权限。

## 权限

!!! tip
    `[gamemode]` 是一个根据你运行的游戏模式而不同的前缀。
    前缀是游戏模式的小写名称,即如果你使用 BSkyBlock,前缀就是 `bskyblock`。
    类似地,如果你使用 AcidIsland,前缀就是 `acidisland`。

=== "玩家权限"
    - `[gamemode].intopten` - (默认: `true`) - 让玩家出现在前 10 名面板中。
    - `[gamemode].island.level` - (默认: `true`) - 允许玩家使用 `/[player_command] level` 命令。
    - `[gamemode].island.top` - (默认: `true`) - 允许玩家使用 `/[player_command] top` 命令。
    - `[gamemode].island.value` - (默认: `true`) - 允许玩家使用 `/[player_command] value` 命令。
    - `[gamemode].island.level.details.blocks` - (默认: `true`) - 允许玩家查看岛屿的详细方块列表。
    - `[gamemode].island.level.details.spawners` - (默认: `false`) - 允许玩家查看岛屿的详细刷怪笼列表。
    - `[gamemode].island.level.details.underwater` - (默认: `false`) - 允许玩家查看岛屿的详细水下方块列表。
    - `[gamemode].island.level.details.above-sea-level` - (默认: `false`) - 允许玩家查看岛屿海平面以上的详细方块列表。

=== "管理员权限"
    - `[gamemode].admin.level` - (默认: `op`) - 允许玩家使用 `/[admin_command] level <player>` 命令。
    - `[gamemode].admin.levelstatus` - (默认: `op`) - 允许玩家使用 `/[admin_command] levelstatus` 命令。
    - `[gamemode].admin.level.sethandicap` - (默认: `op`) - 允许玩家使用 `/[admin_command] sethandicap <player> <number>` 命令。
    - `[gamemode].admin.top` - (默认: `op`) - 允许访问 `/[admin_command] top` 命令。
    - `[gamemode].admin.top.remove` - (默认: `op`) - 允许访问 `/[admin_command] top remove <player>` 命令。

??? question "有缺失的内容吗?"
    你可以在此插件的 [addon.yml](https://github.com/BentoBoxWorld/Level/blob/develop/src/main/resources/addon.yml) 文件中找到完整的权限列表。
    如果下面的列表中确实缺少了什么,请告诉我们!

## 占位符

{{ placeholders_source(source="Level") }}

## 常见问题

??? question "你能添加 X 功能吗?"
    请将其添加到[这里](https://github.com/BentoBoxWorld/Level/issues)的列表中。

??? question "如何让 `level-cost` 在每个等级后增加?"
    你不能直接这样做,因为 BentoBox 等级计算是一次性完成的,而不是每个等级迭代的。

    但是,如果你知道所需的公式,这可以使用 `level-calc` 公式完成。如果我们使用你的示例,让每个等级比前一个等级难 50%,那么近似公式为:

    `level-calc: 2.4661 * log(blocks) - (2.4661 * log(level_cost) - 1)`

    其中 `level_cost` 是达到 1 级所需的方块数。例如,如果 1 级需要 100 个方块,2 级需要 150 个方块,3 级需要 225 个,以此类推。

    这是图表:

    ![template](https://user-images.githubusercontent.com/4407265/212771452-edc943fe-c861-4ba1-b581-8ec987e52f94.png){: loading=lazy }

    请注意,该特定公式在 25 级左右开始渐近,即达到 26 或 27 级变得非常困难,因为需要太多方块,所以这种特定规则可能不是一个好方法,因为最终几乎每个人都会以相同的等级结束。

    无论如何,虽然我理解你的问题,但 `level-calc` 公式实际上应该能够提供你想要的东西,只要它支持正确的公式。拥有 `next-levelcost` 从编程的角度来看是有问题的,因为等级计算必须迭代完成,而不是仅应用单一公式计算所计数的方块。我现在还不能完全弄清楚如何做到这一点,但我确实知道,目前拥有一个公式来确定你想要如何增加等级的方法肯定是有效的。

    我如何计算等级的公式?

    最好的方法是从一个公式开始,绘制图表看它是否有意义,例如使用 Excel 之类的工具。如果你想根据一个值表计算出需要什么公式,那么 Excel(或其他电子表格)也可以做到:制作一个等级图和每个等级需要多少方块,然后绘制表格的图形(X Y 图)。右键单击图表以添加趋势线,选择最适合的近似值,例如线性、对数、指数等。然后选择"在图表上显示方程",显示公式并用 `blocks` 替换 `x`。以下是我为了找出每次增加 50% 且起始成本为 100 个方块的等式所做的一些截图。

    ![template](https://user-images.githubusercontent.com/4407265/212773894-6f635ed4-f337-4936-b50f-3b616b6bf041.png){: loading=lazy }
    ![template](https://user-images.githubusercontent.com/4407265/212773929-b51ae6b3-5df3-43ae-b35f-bc6fcb42d78f.png){: loading=lazy }

    所以,对于这种情况,它应该是:

    `level-calc: 2.4661 * log(blocks) - 10.357`

    希望这有帮助。

## 翻译

{{ translations(3013, ["cs", "de", "es", "fr", "hu", "id", "lv", "pl", "ro", "tr", "zh-CN", "ko", "pt", "vi", "ru"]) }}

## API

从 Level 2.7.2 和 BentoBox 1.17 开始,其他插件可以直接访问 Level 插件数据。但是,对于不想使用太多依赖项的插件来说,插件请求仍然是一个很好的解决方案。

### Maven 依赖
Level 为其他插件提供了 API。这涵盖了 Level 2.8.1 及更高版本。

!!! note
    将 Level 依赖项添加到你的 Maven POM.xml 中:

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
                <artifactId>level</artifactId>
                <version>2.8.1</version>
                <scope>provided</scope>
            </dependency>
        </dependencies>
    ```
使用最新的 Level 版本。

然后,一旦你拥有岛屿所在的世界,并确认玩家是该世界中岛屿的所有者,你就可以通过询问 Level 来获得玩家的等级。

Level 的 JavaDoc 可以在[这里](https://ci.codemc.io/job/BentoBoxWorld/job/Level/ws/target/apidocs/index.html)找到。

### 事件

=== "IslandLevelCalculatedEvent"
    !!! summary "描述"
        当玩家等级被计算时触发的事件。

        链接到类: [IslandLevelCalculatedEvent](https://github.com/BentoBoxWorld/Level/blob/develop/src/main/java/world/bentobox/level/events/IslandLevelCalculatedEvent.java)

    !!! question "变量"
        - `Island island` - 岛屿对象。
        - `UUID targetPlayer` - 计算等级的玩家的 ID。
        - `Results results` - 计算出的岛屿结果。
        
    !!! example "代码示例"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onLevelCalculated(IslandLevelCalculatedEvent event) {
            UUID user = event.getTargetPlayer();
            Island island = event.getIsland();
            Results results = event.getResults();
            
            // 来自结果的死亡惩罚。
            int deathHandicap = event.getDeathHandicap();

            // 来自结果的岛屿初始等级。
            long initialLevel = event.getInitialLevel();
            
            // 来自结果的岛屿等级。
            long level = event.getLevel();

            // 这将覆盖岛屿等级为 100。
            event.setLevel(100);
            
            // 达到下一级所需的点数
            long pointsToNextLevel = event.getPointsToNextLevel();

            // 来自结果的报告文本。
            List<String> report = event.getReport();
        }
        ``` 

=== "IslandPreLevelEvent "
    !!! summary "描述"
        在计算玩家等级之前触发的事件。

        链接到类: [IslandPreLevelEvent](https://github.com/BentoBoxWorld/Level/blob/develop/src/main/java/world/bentobox/level/events/IslandPreLevelEvent.java)

    !!! question "变量"
        - `Island island` - 岛屿对象。
        - `UUID targetPlayer` - 计算等级的玩家的 ID。
        
    !!! example "代码示例"
        ```java
        @EventHandler(priority = EventPriority.LOW)
        public void beforeLevelCalculated(IslandPreLevelEvent event) {
            UUID user = event.getTargetPlayer();
            Island island = event.getIsland();
        }
        ```

### 插件请求处理程序

直到 BentoBox 1.17,由于我们用于加载插件的类加载器,我们在访问 BentoBox 环境之外的数据时遇到了问题。
这意味着数据只能从其他插件访问。但是 BentoBox 实现了 PlAddon 功能,这意味着请求处理程序不再是必需的。

有关插件请求处理程序的更多信息可以在[这里](/en/latest/BentoBox/Request-Handler-API---How-plugins-can-get-data-from-addons/)找到。

=== "island-level"
    !!! summary "描述"
        返回给定世界中玩家的岛屿等级。

    !!! question "输入"
        - `world-name`: String - 世界名称。
        - `player`: UUID - 玩家的 UUID。

    !!! success "输出"
        玩家的岛屿等级,如果输入无效或该玩家在此世界中没有岛屿,则为 `0L`。

    !!! failure
        如果未提供 `world-name` 或 `world-name` 不存在或不是游戏模式世界,此处理程序将返回 `0L`。

    !!! example "代码示例"
        ```java
            /**
             * 返回给定世界中玩家的岛屿等级。
             * @param playerUUID 玩家的 UUID,不为 null。
             * @param worldName 岛屿所在的世界(主世界)名称,不为 null。
             * @return 玩家的岛屿等级,如果输入无效或该玩家在此世界中没有岛屿,则为 {@code 0L}。
             */
            public long getIslandLevel(UUID playerUUID, String worldName) {
                return (Long) new AddonRequestBuilder()
                    .addon("Level")
                    .label("island-level")
                    .addMetaData("world-name", worldName)
                    .addMetaData("player", playerUUID)
                    .request();
            }
        ```

=== "top-ten-level"
    !!! summary "描述"
        返回拥有的岛屿位于前 10 名的玩家,映射到他们岛屿的等级。

    !!! question "输入"
        - `world-name`: String - 世界名称。

    !!! success "输出"
        `Map<UUID, Long>`,包含拥有的岛屿位于前 10 名的岛主的 UUID,映射到他们岛屿的等级。

    !!! failure 
        如果未提供 `world-name` 或 `world-name` 不存在或不是游戏模式世界,此处理程序将返回空 map。

    !!! example "代码示例"
        ```java
            /**
             * 返回拥有的岛屿位于前 10 名的玩家,映射到他们岛屿的等级。
             * @param worldName 岛屿所在的世界(主世界)名称,不为 null。
             * @return 一个 Map,包含拥有的岛屿位于前 10 名的岛主的 UUID,映射到他们岛屿的等级,
             *         如果指定的世界不存在或不包含岛屿,则返回一个空 map。
             */
            public Map<UUID, Long> getTopTen(String worldName) {
                return (Map<UUID, Long>) new AddonRequestBuilder()
                    .addon("Level")
                    .label("top-ten-level")
                    .addMetaData("world-name", worldName)
                    .request();
            }
        ```