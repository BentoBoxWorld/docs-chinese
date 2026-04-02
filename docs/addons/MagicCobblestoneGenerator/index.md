# 魔法圆石发生器

**魔法圆石发生器**将平凡无聊的圆石发生器变成了一个棒极了的、可配置的方块来源！

由[BONNe](https://github.com/BONNe)创建和维护。

{{ addon_description("MagicCobblestoneGenerator") }}

## 安装

1. 将插件jar文件放入BentoBox插件的addons文件夹中
2. 重启服务器
3. 运行`/[admincmd] generator`命令来配置插件

## 配置

默认情况下，插件试图从模板文件中导入所有数据，以简化首次设置。许多插件设置在Admin GUI中公开，然而，有些设置不是。
最新的配置选项及其详细解释可以在[这里](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/blob/develop/src/main/resources/config.yml)找到。

模板文件主要是为那些不喜欢使用游戏内编辑GUI的用户准备的。然而，模板文件在每次更改时不会自动导入。需要通过命令或Admin GUI导入。

??? question "模板文件结构"
    ```
    # 开始所有生成器等级的列表。
    tiers:
      # 生成器的唯一ID。用于内部存储和访问每个生成器数据。
      generator_unique_id: 
        # 用户的显示名称。支持颜色代码。
        # 默认值: 生成器唯一ID去掉下划线
        name: "Something fancy"
        # 说明文字信息。支持颜色代码。
        # 可以通过用[]替换一切来定义为空。
        # 默认值: []
        description: -|
          第一行说明信息
          &2第二行说明信息
        # GUI中使用的图标。数字在末尾允许指定项目的堆叠大小。
        # 默认值: Paper.
        icon: "PAPER:1"
        # 生成器类型: COBBLESTONE, STONE 或 BASALT。自解释。
        # 默认值: COBBLESTONE
        type: COBBLESTONE
        # 指示生成器是否为默认生成器。默认生成器忽略要求部分。
        # 对每种生成器类型只能有一个默认生成器。
        # 默认值: false
        default: false
        # 用户选择激活的生成器。
        # 优先级指示如果多个生成器满足要求，
        # 将使用哪个生成器。
        # 默认值: 1
        priority: 1
        # 这里可以定义几个要求。
        requirements:
          # 可以定义生成器工作所需的最小岛屿等级。需要等级插件。
          # 默认值: 0
          island-level: 10
          # 列出用户选择此生成器所需的权限列表。
          # 默认值: []
          required-permissions: []
          # 列出生成器工作所需的生物群系列表。
          # 空意味着没有限制生物群系生成器工作。
          # 默认值: []。
          required-biomes: []
          # 购买此生成器的费用。需要Vault和任何经济插件。
          # 通过在生成器视图GUI中点击购买图标来实现。
          # 默认值: 0
          purchase-cost: 5.0
        # 激活当前生成器等级的费用。需要Vault和任何经济插件。
        # 只有在生成器之间主动切换时才会支付。
        # 默认值: 0。
        activation-cost: 0.0
        # 材料及其几率。请使用实际的方块。
        # 几率支持任何正数，包括双精度值。
        # 最终所有内容将被规范化。
        # 默认值: []
        blocks:
          FIRST_BLOCK_NAME_ID: NUMBER
          SECOND_BLOCK_NAME_ID: NUMBER
        # 在

方块生成时有机会掉落的宝藏。
        # 仅在生成时，而非方块破坏时。
        # 默认值: []
        treasure:
          # 从0到1的几率。0 - 不可能获得宝藏。
          # 默认值: 0
          chance: 0.001
          # 可以掉落的材料。适用于与方块部分相同的规则。
          # 默认值: []
          material:
            FIRST_BLOCK_NAME_ID: NUMBER
            SECOND_BLOCK_NAME_ID: NUMBER
          # 掉落项目的最大数量。
          # 将从1到定义的数量之间。
          # 默认值: 1
          amount: 1
    
    # 开始所有套餐的列表
    bundles:
      # 套餐id
      bundle_unique_id:
        # 用户的显示名称
        name: "Something fancy"
        # 说明文字信息。支持颜色代码。
        # 可以通过用[]替换一切来定义为空。
        # 默认值: []
        description: -|
          第一行说明信息
          &2第二行说明信息
        # GUI中使用的图标。数字在末尾允许指定项目的堆叠大小。
        # 默认值: Paper.
        icon: "PAPER:1"
        # 套餐将工作有访问权限的生成器列表。
        generators:
          - generator_id_1
          - generator_id_2
    ```

## 命令

!!! 小贴士
    `[player_command]` 和 `[admin_command]` 是根据你运行的游戏模式而不同的命令。
    游戏模式的`config.yml`文件包含允许你修改这些值的选项。
    例如，在BSkyBlock上，默认的`[player_command]`是`island`，默认的`[admin_command]`是`bsbadmin`。
    注意，这个插件允许在插件`config.yml`文件中更改玩家命令别名。

=== "玩家命令"
    - `/[player_command] generator`：访问生成器选择GUI。
    - `/[player_command] generator view <generator>`：访问特定生成器的详细视图。
    - `/[player_command] generator activate <generator> [false]`：允许激活（或停用）特定生成器。
    - `/[player_command] generator buy <generator>`：允许购买特定生成器。

=== "管理员命令"
    - `/[admin_command] generator`：访问插件的管理员GUI
    - `/[admin_command] generator import`：导入默认模板文件 - `/plugins/BentoBox/addons/MagicCobblestoneGenerator/generatorTemplate.yml`。
    - `/[admin_command] generator database import <file>`：能够导入导出的数据库<file>。
    - `/[admin_command] generator database export <file>`：能够将数据库导出到保存在`/plugins/BentoBox/addons/MagicCobblestoneGenerator/`文件夹中的<file>。
    - `/[admin_command] generator why <player>`：一个调试命令，允许为每个玩家找到生成器问题。

## 权限

!!! 小贴士
    `[gamemode]` 是一个根据你运行的游戏模式而不同的前缀。
    前缀是游戏模式的小写名称，即如果你使用BSkyBlock，前缀是`bskyblock`。
    类似地，如果你使用AcidIsland，前缀是`acidisland`。

=== "玩家权限"
    - `[gamemode].stone-generator` - 让玩家使用`/[player_command] generator`命令及其子命令。
    - `[gamemode].stone-generator.active-generators.3` - 设置岛屿所有者可以拥有的最大活跃生成器数量。3可以被任何正整数替换。这只是一个例子。
    - `[gamemode].stone-generator.max-range.30` - 设置生成器继续

工作的最大距离。30可以被任何正整数替换。这只是一个例子。
    - `[gamemode].stone-generator.bundle.[bundle_id]` - 指定将用于用户拥有的岛屿的套餐。

=== "管理员权限"
    - `[gamemode].admin.stone-generator` - 让玩家使用`/[admin_command] generator`命令及其子命令。
    - `[gamemode].admin.stone-generator.why` - 让玩家使用调试命令`/[admin_command] why generator <player>`。
    - `[gamemode].admin.stone-generator.database` - 让玩家使用`/[admin_command] generator database`命令及其子命令。
    
??? question "缺少什么？"
    你可以在这个插件的[addon.yml](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/blob/develop/src/main/resources/addon.yml)文件中找到权限的综合列表。  
    如果下面的列表确实缺少了什么，请告诉我们！


## 占位符

{{ placeholders_source(source="MagicCobblestoneGenerator") }}


## 常见问题解答

??? question "你能添加功能X吗？"
    请在[这里](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/issues)添加。

??? question "如何添加新的生成器等级？"
    目前，插件支持3种添加新生成器的方式：
    
    - 通过使用游戏内GUI，可通过`/[admin] generator`命令访问。
    - 通过向模板文件添加生成器。
    - 通过向导出的数据库文件添加生成器。

??? question "我在模板/数据库文件中添加了生成器，但它在游戏中不显示。"
    为了更容易地配置多个游戏模式，生成器存储在内部数据库中。编辑模板或数据库文件后，您需要将它们导入到内存中。您可以通过点击Admin GUI中的`导入模板`或`导入数据库`按钮来完成。

??? question "我有一个生成器显示在Admin GUI中，但玩家看不到它。"
    最有可能是由于“部署”状态。为了避免在管理员添加它们时玩家开始激活生成器的问题，生成器是未部署的，没有人可以使用它们。您可以通过编辑Admin GUI中的生成器并点击编辑生成器GUI中的开关来激活它们。

??? question "什么是宝藏？"
    宝藏是在生成方块时掉落的东西。它允许为每个生成器提供额外的自定义。

??? question "什么是套餐？"
    套餐是一项功能，允许为每个岛屿提供更多的自定义体验。如果岛屿分配了套餐，那么该岛屿上的玩家将只能使用该套餐中的生成器。

??? question "我可以禁用在生成器描述中显示所需权限吗？"
    是的，插件为显示每个生成器提供了许多自定义选项。它位于 locales 文件中：
    ```
          # 生成器说明消息生成器。生成器说明中的所有元素都是基于
          # 下面的部分生成的。
          generator:
            # 主说明元素内容。如果你不想显示宝藏，
            # 只需从 [treasures] 部分删除它们。
            # [description] 来自每个生成器等级。
            # 说明不支持颜色代码。每个对象都单独支持。
            lore: |-
              [description]
              [blocks]
              [treasures]
              [type]
              [requirements]
              [status]
            # 生成 [blocks] 部分
            blocks:
              # blocks 部分中的第一行。空行将不显示。
              title: "&7&l Blocks:"
              # 标题下的每个方块及其值。不能为空。
              # 支持 [number], [#.#], [#.##], [#.###], [#.####], [#.#####]
              value: "&8 [material] - [#.##]%"
            # 生成 [treasures] 部分
            treasures:
              # blocks 部分中的第一行。空行将不显示。
              title: "&7&l Treasures:"
              # 标题下的每个宝藏及其值。不能为空。
              # 支持 [number], [#.#], [#.##], [#.###], [#.####], [#.#####]
              value: "&8 [material] - [#.####]%"
            # 生成 [requirements] 部分
            requirements:
              # 允许更改要求消息的顺序和内容。
              description: |-
                [biomes]
                [level]
                [missing-permissions]
              # 生成 [level] 消息。
              level: "&c&l Required Level: &r&c [number]"
              # 生成 [missing-permission] 消息标题。
              permission-title: "&c&l Missing Permissions:"
              # 生成 [missing-permission] 消息值。
              permission: "&c  -[permission]"
              # 生成 [biomes] 消息标题。
              biome-title: "&7&l Operates in:"
              # 生成 [biomes] 消息值。
              biome: "&8 [biome]"
              # 生成所有生物群系的 [biomes] 消息。
              any: "&7&l Operates in &e&o all &r&7&l biomes"
            # 生成 [status] 部分
            status:
              # 针对锁定生成器显示的消息。
              locked: "&c Locked!"
              # 针对未部署生成器显示的消息。
              undeployed: "&c Not Deployed!"
              # 针对活跃生成器显示的消息。
              active: "&2 Active"
              # 针对需要购买的生成器显示的消息。
              purchase-cost: "&e Purchase Cost: $[number]"
              # 针对有激活费用的生成器显示的消息。
              activation-cost: "&e Activation Cost: $[number]"
            # 生成 [type] 部分
            type:
              title: "&7&l Supports:"
              cobblestone: "&8 Cobblestone Generators"
              stone: "&8 Stone Generators"
              basalt: "&8 Basalt Generators"
              any: "&7&l Supports &e&o all &r&7&l generators"
    ```

## 翻译

{{ translations(2972, ["de", "es", "lv", "zh-CN", "zh-TW", "fr", "ru", "pl", "tr", "vi"]) }}

## API

自 MagicCobblestoneGenerator 2.4.0 和 BentoBox 1.17 以来，其他插件可以直接访问 MagicCobblestoneData 插件的数据。但是，对于不想使用太多依赖的插件来说，插件请求仍然是一个很好的解决方案。

### Maven 依赖

MagicCobblestoneGenerator 为其他插件提供了 API。这涵盖了 2.5.0 及以后的版本。

!!! note
    将 MagicCobblestoneGenerator 依赖添加到你的 Maven POM.xml 中：

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
                <artifactId>magiccobblestonegenerator</artifactId>
                <version>2.5.0</version>
                <scope>provided</scope>
            </dependency>
        </dependencies>
    ```

使用最新的 MagicCobblestoneGenerator 版本。

MagicCobblestoneGenerator 的 JavaDocs 可以在[这里](https://ci.codemc.io/job/BentoBoxWorld/job/MagicCobblestoneGenerator/ws/target/apidocs/index.html)找到。

### 事件

=== "GeneratorActivationEvent"
    !!! summary "描述"
        玩家在其岛屿上激活/停用生成器时触发的事件。
        此事件可以取消。

        类链接：[GeneratorActivationEvent](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/blob/develop/src/main/java/world/bentobox/magiccobblestonegenerator/events/GeneratorActivationEvent.java)

    !!! question "变量"
        - `String islandUUID` - 目标岛屿 ID。
        - `UUID targetPlayer` - 触发生成器激活的玩家的 ID。
        - `String generator` - 被激活生成器的名称。
        - `String generatorID` - 被激活生成器的 ID。
        - `boolean activate` - 指示生成器是激活还是停用的布尔值。


    !!! example "代码示例"
        ```java
        @EventHandler(priority = EventPriority.LOW)
        public void onGeneratorActivationChange(GeneratorActivationEvent event) {
            UUID user = event.getTargetPlayer();
            String island = event.getIslandUUID();

            String generator = event.getGenerator();
            String generatorID = event.getGeneratorID();
            boolean activate = event.isActivate();
        }
        ```

=== "GeneratorUnlockEvent"
    !!! summary "描述"
        玩家在其岛屿上解锁新生成器时触发的事件。
        此事件可以取消。

        类链接：[GeneratorUnlockEvent](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/blob/develop/src/main/java/world/bentobox/magiccobblestonegenerator/events/GeneratorUnlockEvent.java)

    !!! question "变量"
        - `String islandUUID` - 目标岛屿 ID。
        - `UUID targetPlayer` - 触发生成器解锁的玩家的 ID。
        - `String generator` - 被解锁生成器的名称。
        - `String generatorID` - 被解锁生成器的 ID。


    !!! example "代码示例"
        ```java
        @EventHandler(priority = EventPriority.LOW)
        public void onGeneratorUnlock(GeneratorUnlockEvent event) {
            UUID user = event.getTargetPlayer();
            String island = event.getIslandUUID();

            String generator = event.getGenerator();
            String generatorID = event.getGeneratorID();
        }
        ```

=== "GeneratorBuyEvent"
    !!! summary "描述"
        玩家在其岛屿上购买新生成器时触发的事件。
        此事件不可取消。

        类链接：[GeneratorBuyEvent](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/blob/develop/src/main/java/world/bentobox/magiccobblestonegenerator/events/GeneratorBuyEvent.java)

    !!! question "变量"
        - `String islandUUID` - 目标岛屿 ID。
        - `UUID targetPlayer` - 购买生成器的玩家的 ID。
        - `String generator` - 被购买生成器的名称。
        - `String generatorID` - 被购买生成器的 ID。


    !!! example "代码示例"
        ```java
        @EventHandler(priority = EventPriority.LOW)
        public void onGeneratorBuy(GeneratorBuyEvent event) {
            UUID user = event.getTargetPlayer();
            String island = event.getIslandUUID();

            String generator = event.getGenerator();
            String generatorID = event.getGeneratorID();
        }
        ```

### 插件请求处理程序

到 BentoBox 1.17 为止，我们在访问 BentoBox 环境外的数据时遇到了类加载器的问题。
这意味着数据只能从其他插件访问。但 BentoBox 实现了 PlAddon 功能，这意味着请求
处理程序不再是必需的。

有关插件请求处理程序的更多信息可以在[这里](/en/latest/BentoBox/Request-Handler-API---How-plugins-can-get-data-from-addons/)找到。

=== "active-generator-names"
    !!! summary "描述"
        返回玩家的活跃生成器的名称。

        自 2.4.0 版本开始。

    !!! question "输入"
        - `world-name`: String - 世界的名称。
        - `player`: String - 玩家的 UUID。

    !!! success "输出"
        输出是一个 `List<String>`，包含活跃生成器的名称。

    !!! failure "失败"
        如果未提供 `world-name` 或 `world-name` 不存在或未提供 `player`，此处理程序将返回 null。

    !!! example "代码示例"
        ```java
        public List<String> getActiveGeneratorNames(String worldName, UUID playerUUID) {
            return (List<String>) new AddonRequestBuilder()
                .addon("MagicCobblestoneGenerator")
                .label("active-generator-names")
                .addMetaData("world-name", worldName)
                .addMetaData("player", playerUUID)
                .request();
        }
        ```


=== "generator-data"
    !!! summary "描述"
        返回为请求的生成器对象存储的原始数据。

        自 2.4.0 版本开始。

    !!! question "输入"
        - `generator`: String - 生成器的 UUID。

    !!! success "输出"
        输出是一个 `Map<String, Object>`，包含原始生成器数据。

        输出映射包含：

        - `uniqueId`: String - 生成器的唯一 ID。应与输入相同。
        - `friendlyName`: String - 生成器的显示名称（未格式化）。
        - `description`: List<String> - 说明消息的字符串列表（未格式化）。
        - `generatorType`: String - 生成器的类型。可用的类型：

            - COBBLESTONE
            - STONE
            - BASALT
            - COBBLESTONE_OR_STONE
            - BASALT_OR_COBBLESTONE
            - BASALT_OR_STONE
            - ANY

        - `generatorIcon`: ItemStack - 生成器图标的物品堆。
        - `lockedIcon`: ItemStack - 锁定的生成器图标的物品堆。
        - `defaultGenerator`: boolean - 指示生成器是否为默认的布尔值。
        - `priority`: int - 生成器的优先级值。
        - `requiredMinIslandLevel`: int - 生成器工作所需的最小岛屿等级。
        - `requiredBiomes`: Set<Biome> - 生成器工作所需的生物群系集合。
        - `requiredPermissions`: Set<String> - 生成器可购买所需的权限集合。
        - `generatorTierCost`: double - 生成器的价格。
        - `activationCost`: double - 生成器的激活价格。
        - `deployed`: boolean - 指示生成器对玩家是否可用的布尔值。
        - `blockChanceMap`: TreeMap<Double, Material> - 包含方块几率原始数据的映射。
        - `treasureItemChanceMap`: TreeMap<Double, ItemStack> - 包含宝藏几率原始数据的映射。
        - `treasureChance`: double - 从生成的方块中掉落宝藏的值。
        - `maxTreasureAmount`: int - 一次掉落的最大宝藏数量。

    !!! failure "失败"
        如果未提供 `generator`，此处理程序将返回 null；如果 `generator` 不存在，将返回空映射。

    !!! example "代码示例"
        ```java
        public Map<String, Object> getGeneratorData(String generatorId) {
            return (List<String>) new AddonRequestBuilder()
                .addon("MagicCobblestoneGenerator")
                .label("generator-data")
                .addMetaData("generator", generatorId)
                .request();
        }
        ```