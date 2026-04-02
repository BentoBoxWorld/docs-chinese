# 生态区

**生态区**允许您的玩家在他们的岛屿上**改变生态区**。

由[BONNe](https://github.com/BONNe)创建和维护。

{{ addon_description("Biomes", beta=True) }}

## 安装

1. 将插件 jar 文件放到 `plugins/BentoBox/addons` 文件夹中。
2. 启动并停止服务器，让生态区生成其配置文件。
3. 编辑[`config.yml`](#config.yml)和[`biomesTemplate.yml`](#Template)文件（你可以在`plugins/BentoBox/addons/Biomes`文件夹中找到它们）。
4. 重启服务器。
5. 将生态区导入到游戏模式中。

## 配置

### config.yml

插件安装成功后，它将创建config.yml文件。这个文件中的每个选项都附有注释。请查阅文件以获取更多信息。
你可以在这里找到最新的配置文件：[config.yml](https://github.com/BentoBoxWorld/Biomes/blob/develop/src/main/resources/config.yml)

### 模板

!!! 警告
    与通常的配置文件不同，你对`biomesTemplate.yml`文件所做的更改在启动服务器时不会自动被考虑。  
    你必须手动导入所做的更改，并最终覆盖之前已导入的配置。

此文件包含有关默认生态区的所有必要信息。
如果你在biomes.yml中更改了值，那么要应用它们，你必须运行 **/[admin_command] biomes**。

默认模板文件可以在这里找到：[biomesTemplate.yml](https://github.com/BentoBoxWorld/Biomes/blob/develop/src/main/resources/biomesTemplate.yml)

!!! 信息 "关于生态区的有用资源"
    - [Spigot上可用生态区的综合列表](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/block/Biome.html)
    - [官方Minecraft wiki上的“生态区”页面](https://minecraft.gamepedia.com/Biome)

??? 模板文件结构
    ```
    biomes:                                      # 内部数据结构。不要更改！
      <unique_name>:                             # 生态区的唯一名称。必需！
        biome: <BIOME>                           # Spigot生态区类型。有效值可以在下面的链接中找到。必需！
        environment: <ENVIRONMENT>               # Spigot世界环境类型。默认为Normal。
        name: <String>                           # 生态区的自定义名称。默认为<unique_name>。
        description: <String>                    # 图标描述中的一些额外描述。默认为空。
        icon: <Item>                             # BentoBox ItemParser类型。写入格式可以在：https://docs.bentobox.world/en/latest/BentoBox/ItemParser/ 中找到。默认为纸。
        order: <Integer>                         # 当前生态区的顺序。默认为-1。
        unlock:                                  # 配置生态区解锁/购买选项的部分。不是必需的。
          level: <Long>                          # 解锁生态区所需的最小岛屿等级。需要等级插件。默认为0。
          permissions: [<String>]                # 解锁生态区所需的权限集。默认为空。
          cost: <Double>                         # 购买生态区的费用（一次性）。需要Vault和经济插件。默认为0。
          items: [<Item>]                        # 购买生态区所需的物品集（一次性）。每个物品的写入格式可以在：https://docs.bentobox.world/en/latest/BentoBox/ItemParser/ 中找到。默认为空。
        change:                                  # 配置每次使用生态区的成本的部分。不是必需的。
          mode: <Mode>                           # 应用成本的模式。支持的值：STATIC - 价格永远不变，PER_BLOCK - 每个区域内的方

块都应用成本，PER_USAGE - 每次使用后成本增加[increment]。默认为STATIC。
          cost: <Double>                         # 更改生态区的成本。需要Vault和经济插件。默认为0。
          items: [<Item>]                        # 更改生态区所需的物品集。每个物品的写入格式可以在：https://docs.bentobox.world/en/latest/BentoBox/ItemParser/ 中找到。默认为空。
          increment: <Double>                    # 如果使用设置为PER_USAGE，则所有成本（金钱和物品）的增量。默认为0。（作为静态）
    # 这里开始捆绑包列表
    bundles:                                     # 内部数据结构。
      <unique_name>:                             # 捆绑包的唯一名称。必需！
        name: <String>                           # 捆绑包的自定义名称。默认为<unique_name>。
        description: <String>                    # 图标描述中的一些额外描述。默认为空。
        icon: <Item>                             # BentoBox ItemParser类型。写入格式可以在：https://docs.bentobox.world/en/latest/BentoBox/ItemParser/ 中找到。默认为纸。
        biomes: [<String>]                       # 在生态区部分中使用的<unique_names>集。默认为空。
    ```

### 可自定义的GUI

BentoBox 1.17 API引入了一个功能，允许实现可自定义的GUI。这个插件是第一个使用这个功能的插件之一。我们试图尽可能简单地进行自定义，然而，一些功能需要解释。
你可以在这里找到更多关于BentoBox自定义GUI如何工作的信息：[自定义GUI](/en/latest/Tutorials/generic/Customizable-GUI/)

??? 问题 "如何自定义GUI"
    要自定义插件GUI，你需要拥有2.0版本。这是第一个实现它们的版本。插件将在`/plugins/BentoBox/addons/Biomes`下创建一个名为`panels`的新目录

    目前你可以自定义3个GUI：

    - 主面板：`main_panel` - 包含所有用户可以购买或使用的生态区的面板。
    - 高级面板：`advanced_panel` - 包含不同方式的面板，生态区可以在岛屿上应用。
    - 购买面板：`buy_panel` - 包含玩家可以购买的生态区的面板。

    每个GUI包含只有它自己支持的函数。

??? 问题 "什么是`PREVIOUS`|`NEXT`按钮类型？"
    PREVIOUS和NEXT按钮类型允许创建自动分页，当你的生态区多于GUI中的空间时。
    这些类型在数据下有额外的参数：
 
    - `indexing` - 表示按钮是否会显示页码。

    示例： 
    ```yaml
        icon: tipped_arrow[potion_contents={custom_color:11546150}]
        title: biomes.gui.buttons.previous.name
        description: biomes.gui.buttons.previous.description
        data:
          type: PREVIOUS
          indexing: true
        action:
          left:
            tooltip: biomes.gui.tips.click-to-previous
    ```

??? 问题 "什么是`RETURN`按钮类型？"
    这个按钮在所有面板中都可用。
    它创建一个允许返回到上一个菜单或退出gui的按钮。描述由插件生成，但像所有按钮一样，你可以在面板中指定你自己的文本。

    示例： 
    ```yaml
        data:
          type: RETURN
    ```

??? 问题 "什么是`BIOME`按钮类型？"
    这个按钮在main_panel和buy_panel中可用。
    BIOME按钮为生态区对象创建一个动态条目。只有当存在生态区时，按钮才会被填充。例如，如果你只有3个生态区，但在GUI中为它们定义了7个位置，那么只有3个位置会被填充。其余位置将保持空白。

    默认情况下，生态区将根据它们的顺序编号进行排序，然而，你可以使用`id`参数在数据下指定特定生态区在特定插槽中。
    
    ```yaml
      data:
        type: BIOME
        id: example_biome
    ```

    指定标题、描述和图标将覆盖基于数据库数据的动态生成。默认情况下，这些值将从数据库条目中生成。
    这个按钮支持3种不同的操作类型：

    - CHANGE - 根据默认更新模式和默认范围值更改生态区。在main_panel中可用。
    - ADVANCED_PANEL - 打开允许选择不同生态区更新模式的高级面板。在main_panel中可用。
    - BUY - 购买选定的生态区。在buy_panel中可用。

    示例： 
    ```yaml
      data:
        type: BIOME
      actions:
        left:
          type: CHANGE
          # 支持ISLAND | CHUNK:NUMBER | RANGE:NUMBER
          content: ISLAND
          tooltip: biomes.gui.tips.left-click-to-apply
        right: 
          type: ADVANCED_PANEL
          tooltip: biomes.gui.tips.right-click-to-open
    ```

??? 问题 "什么是`PURCHASE`按钮类型？"
    这个按钮在main_panel中可用。
    它创建一个打开新面板的按钮，该面板包含玩家可以购买的生态区。

    示例： 
    ```yaml
        data:
          type: PURCHASE
        action:
          left:
            tooltip: biomes.gui.tips.click-to-view
    ```


??? 问题 "什么是`INCREASE|REDUCE`按钮类型？"
    这个按钮在advanced_panel中可用。
    它创建一个增加/减少更改生态区“范围”的按钮。增加/减少的数字可以与按钮类型一起定义。

    示例： 
    ```yaml
        data:
          type: INCREASE
          value: 5
        actions:
          left:
            tooltip: biomes.gui.tips.click-to-increase
    ```

??? 问题 "什么是`MODE`按钮类型？"
    这个按钮在advanced_panel中可用。
    它创建一个允许在ISLAND、CHUNK和RANGE模式之间更改生态区更新模式的按钮。模式与按钮类型一起定义。

    示例： 
    ```yaml
        data:
          type: MODE
          value: CHUNK
        actions:
          left:
            tooltip: biomes.gui.tips.click-to-choose
    ```

??? 问题 "什么是`ACCEPT`按钮类型？"
    这个按钮在advanced_panel中可用。
    它创建一个允许使用选定设置开始生态区更新的按钮。它有两个动作： 
      
       - ACCEPT: 开始生态区更新
       - INPUT: 允许通过聊天手动输入数字。

    示例： 
    ```yaml
        data:
          type: ACCEPT
        actions:
          left:
            type: ACCEPT
            tooltip: biomes.gui.tips.left-click-to-accept
          right:
            type: INPUT
            tooltip: biomes.gui.tips.right-click-to-write
    ```

## 命令

!!! 小贴士
    `[player_command]`和`[admin_command]`是根据你运行的游戏模式而变化的命令。
    游戏模式的`config.yml`文件包含允许你修改这些值的选项。
    例如，在BSkyBlock上，默认的`[player_command]`是`island`，默认的`[admin_command]`是`bsbadmin`。

!!! 信息
    生态区插件玩家命令是完全可配置的。你可以在生态区插件配置文件中更改它们。下面仅是这些命令的默认名称。

=== "玩家命令"
    - `/[player_command] biomes`: 此方法打开GUI，允许在用户岛屿上更改生态区。
    - `/[player_command] biomes help`: 显示所有命令的帮助
    - `/[player_command] biomes set <biome> [<type>] [<size>]`: 此命令允许在不打开GUI的情况下更改岛屿上的生态区。如果参数<type>和<size>未提供，命令将使用插件配置中的默认值。
    - `/[player_command] biomes buy <biome>`: 此命令允许在不打开GUI的情况下购买生态区。

    !!! 信息
        - `<biome>`可能不是实际Minecraft生态区名称。它是由管理员定义的。
        - `<type>`是三种生态区更改类型之一。它提供在整个岛屿(`ISLAND`)、当前区块(`CHUNK`)或围绕玩家的距离(`RANGE`)上更改生态区。


=== "管理员命令"
    - `/[admin_command] biomes`: 打开管理员生态区GUI。
    - `/[admin_command] biomes help`: 显示所有与生态区相关的管理员命令的帮助。
    - `/[admin_command] biomes import [<file>]`: 从`biomesTemplate.yml`配置文件或提供的文件中导入生态区。
    - `/[admin_command] biomes set <player> <biome> [<type>] [<size>]`: 与用户生态区设置命令相同，但需要提供玩家，其岛屿生态区将被更新。
    - `/[admin_command] biomes migrate`: 迁移生态区插件数据。通常用于从旧版本升级到新版本时使用。
    - `/[admin_command] biomes unlock <player> <biome_id> [true]`: 解锁（如果在最后添加`true`则购买）传递的生态区给玩家岛屿。

## 权限

!!! 小贴士
    `[gamemode]`是一个前缀，根据你运行的游戏模式而变化。
    前缀是游戏模式的小写名称，即如果你使用BSkyBlock，前缀是`bskyblock`。
    类似地，如果你使用AcidIsland，前缀是`acidisland`。

??? 问题 "缺少什么？"
    你可以在这个插件的[addon.yml](https://github.com/BentoBoxWorld/Biomes/blob/develop/src/main/resources/addon.yml)文件中找到权限的综合列表。  
    如果下面的列表确实缺少了什么，请告诉我们！

=== "玩家权限"
    - `[gamemode].biomes`（默认：`true`）：玩家可以使用打开GUI的生态区命令。
    - `[gamemode].biomes.info`（默认：`true`）：玩家可以使用生态区信息命令。
    - `[gamemode].biomes.set`（默认：`true`）：玩家可以使用生态区设置命令。
    - `[gamemode].biomes.buy`（默认：`true`）：玩家可以使用生态区购买命令。

=== "管理员权限"
    - `[gamemode].admin.biomes`（默认：`op`）：玩家可以使用打开GUI的管理员生态区命令。

## 翻译

{{ translations(2894, ["lv", "zh-CN", "fr", "pl", "es", "uk"]) }}

## API

自从生态区2.0和BentoBox 1.17以来，其他插件可以直接访问生态区插件数据。然而，插件请求仍然是对于不想使用太多依赖的插件来说是一个好的解决方案。

### Maven依赖

生态区提供了一个用于其他插件的API。这涵盖了2.1.0及之后的版本。

!!! 注意
添加生态区依赖到你的Maven POM.xml中：

    ```xml
        <repositories>
            <repository>
                <id>codemc-repo</id>
                <url>https://repo.codemc.io/repository/bentoboxworld/</url>
            </repository>
        </repositories>
        
        <dependencies>
            <dependency>
                <groupId>world.bentobox</groupId>
                <artifactId>biomes</artifactId>
                <version>2.1.0</version>
                <scope>provided</scope>
            </dependency>
        </dependencies>
    ```

使用最新的生态区版本。

生态区的JavaDocs可以在[这里](https://ci.codemc.io/job/BentoBoxWorld/job/Biomes/ws/target/apidocs/index.html)找到。

### 事件

=== "BiomeUnlockedEvent"
    !!! 摘要 "描述"
        当玩家解锁新生态区时触发的事件。

        事件是可取消的。取消事件将阻止用户解锁生态区对象。

        类链接：[BiomeUnlockedEvent](https://github.com/BentoBoxWorld/Biomes/blob/develop/src/main/java/world/bentobox/biomes/events/BiomeUnlockedEvent.java)

    !!! 摘要 "自"
        事件在生态区2.0版本中添加。

    !!! 问题 "变量"
        - `@NotNull BiomesObject biomesObject` - 被解锁的生态区对象。
        - `@Nullable User user` - 解锁生态区对象的用户。
        - `@NotNull Island island` - 生态区对象被解锁的岛屿。
        
    !!! 示例 "代码示例"
        ```java
        @EventHandler(priority = EventPriority.LOW)
        public void onBiomesUnlock(BiomeUnlockedEvent event) {
            User user = event.getUser();
            BiomesObject biomesOjbect = event.getBiomesObject();
            Island island = event.getIsland();
            
            // 还有转换方法，不使用生态区插件对象。
            UUID userUUID = event.getUserUUID();
            String islandUUID = event.getIslandUUID();
            String biomeId = event.getBiomeId();
            Biome biome = event.getBiome();

            event.setCancelled(false);
        }
        ```

=== "BiomePurchasedEvent"
    !!! 摘要 "描述"
        当玩家购买新生态区时触发的事件。

        事件仅为信息性质。不能被取消。

        类链接：[BiomePurchasedEvent](https://github.com/BentoBoxWorld/Biomes/blob/develop/src/main/java/world/bentobox/biomes/events/BiomePurchasedEvent.java)

    !!! 摘要 "自"
        事件在生态区2.0版本中添加。

    !!! 问题 "变量"
        - `@NotNull BiomesObject biomesObject` - 被购买的生态区对象。
        - `@NotNull User user` - 购买生态区对象的用户。
        - `@NotNull Island island` - 生态区对象被购买的岛屿。
        
    !!! 示例 "代码示例"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onBiomesPurchase(BiomePurchasedEvent event) {
            User user = event.getUser();
            BiomesObject biomesOjbect = event.getBiomesObject();
            Island island = event.getIsland();
            
            // 还有转换方法，不使用生态区插件对象。
            UUID userUUID = event.getUserUUID();
            String islandUUID = event.getIslandUUID();
            String biomeId = event.getBiomeId();
            Biome biome = event.getBiome();
        }
        ```

=== "BiomePreChangeEvent"
    !!! 摘要 "描述"
        在从项目中提取物品并更改区域生态区之前触发的事件。

        事件仅为信息性质。不能被取消。

        类链接：[BiomePreChangeEvent](https://github.com/BentoBoxWorld/Biomes/blob/develop/src/main/java/world/bentobox/biomes/events/BiomePreChangeEvent.java)

    !!! 摘要 "自"
        事件在生态区2.0版本中添加。

    !!! 问题 "变量"
        - `@NotNull BiomesObject biomesObject` - 被使用的生态区对象。
        - `@Nullable User user` - 触发生态区更改的用户。
        - `@NotNull Island island` - 生态区发生变化的岛屿。
        - `@NotNull BlockVector min

Coordinate` - 生态区更改的最小坐标。
        - `@NotNull BlockVector maxCoordinate` - 生态区更改的最大坐标。
        
    !!! 示例 "代码示例"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onBiomesPreChange(BiomePreChangeEvent event) {
            User user = event.getUser();
            BiomesObject biomesOjbect = event.getBiomesObject();
            Island island = event.getIsland();
            
            BlockVector minCoordinate = event.getMinCoordinate();
            BlockVector maxCoordinate = event.getMaxCoordinate();
            
            // 还有转换方法，不使用生态区插件对象。
            UUID userUUID = event.getUserUUID();
            String islandUUID = event.getIslandUUID();
            String biomeId = event.getBiomeId();
            Biome biome = event.getBiome();

            int minX = event.getMinX();
            int minY = event.getMinY();
            int minZ = event.getMinZ();

            int maxX = event.getMaxX();
            int maxY = event.getMaxY();
            int maxZ = event.getMaxZ();
        }
        ```


=== "BiomeChangedEvent"
    !!! 摘要 "描述"
        在整个区域的生态区改变后触发的事件。即使生态区更改失败，也会触发事件。

        事件仅为信息性质。不能被取消。

        类链接：[BiomeChangedEvent](https://github.com/BentoBoxWorld/Biomes/blob/develop/src/main/java/world/bentobox/biomes/events/BiomeChangedEvent.java)

    !!! 摘要 "自"
        事件在生态区2.0版本中添加。

    !!! 问题 "变量"
        - `@NotNull BiomesObject biomesObject` - 被使用的生态区对象。
        - `@Nullable User user` - 触发生态区更改的用户。
        - `@NotNull Island island` - 生态区发生变化的岛屿。
        - `@NotNull BlockVector minCoordinate` - 生态区更改的最小坐标。
        - `@NotNull BlockVector maxCoordinate` - 生态区更改的最大坐标。
        - `@Nullable Result result` - 生态区更改后的结果值。结果值可能为：
                                        - FINISHED: 生态区更改成功。
                                        - TIMEOUT: 生态区更改超过超时值，失败。
                                        - FAILED: 生态区更改由于其他原因失败。

    !!! 示例 "代码示例"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onBiomeChanged(BiomeChangedEvent event) {
            User user = event.getUser();
            BiomesObject biomesOjbect = event.getBiomesObject();
            Island island = event.getIsland();
            
            BlockVector minCoordinate = event.getMinCoordinate();
            BlockVector maxCoordinate = event.getMaxCoordinate();
            
            Result result = event.getResult();            

            // 还有转换方法，不使用生态区插件对象。
            UUID userUUID = event.getUserUUID();
            String islandUUID = event.getIslandUUID();
            String biomeId = event.getBiomeId();
            Biome biome = event.getBiome();

            int minX = event.getMinX();
            int minY = event.getMinY();
            int minZ = event.getMinZ();

            int maxX = event.getMaxX();
            int maxY = event.getMaxY();
            int maxZ = event.getMaxZ();

            String resultName = event.getResultName();
        }
        ```