# 魔法圆石发生器

**魔法圆石发生器**将平凡无聊的圆石发生器变成了一个棒极了的、可配置的方块来源！

由[BONNe](https://github.com/BONNe)创建和维护。

{{ addon_description("MagicCobblestoneGenerator") }}

## 安装

1. 将插件jar文件放入BentoBox插件的addons文件夹中
2. 重启服务器
3. 运行`/[admincmd] generator`指令来配置插件

## 配置

默认情况下，插件试图从模板文件中导入所有数据，以简化首次设置。许多插件设置在Admin GUI中公开，然而，有些设置不是。
最新的配置选项及其详细解释可以在[这里](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/blob/develop/src/main/resources/config.yml)找到。

模板文件主要是为那些不喜欢使用游戏内编辑GUI的用户准备的。然而，模板文件在每次更改时不会自动导入。需要通过指令或Admin GUI导入。

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
        # 生成器类型: which vanilla lava mechanic this tier replaces.
        # COBBLESTONE, STONE, BASALT, COBBLESTONE_OR_STONE, BASALT_OR_COBBLESTONE,
        # BASALT_OR_STONE or ANY. See the "Generator types" section below.
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

### 生成器类型（方块流产生的熔岩机制）

Minecraft 通过四种不同的方式从熔岩中创建方块，生成器层级只针对其**类型**覆盖的那些触发。这是控制*生成器可以使用的位置*的主要设置：

| 原版机制 | 原版生成的方块 | 生成器类型 |
|---|---|---|
| 一个熔岩**源**接触水 | 黑曜石 | *插件不处理* |
| **流动的熔岩**在同一水平面接触水 | 圆石 | `COBBLESTONE` |
| **流动的熔岩**流入水中 | 石头 | `STONE` |
| **流动的熔岩**流入灵魂土壤旁的蓝冰 | 玄武岩 | `BASALT` |

类型是按生成器层级设置的，可以在管理员 GUI — `/[admin] generator` → 选择一个层级 → **类型**按钮，打开列出每个类型及其后面机制提示的选择器 — 或使用模板文件中的 `type:` 键。组合类型 `COBBLESTONE_OR_STONE`、`BASALT_OR_COBBLESTONE`、`BASALT_OR_STONE` 和 `ANY` 使层级针对多个机制触发。

!!! warning "`STONE` 生成器在任何水体上工作"
    一个 `STONE` 生成器在玩家可以倒岩浆到水中的地方触发 — 包括岛屿保护范围内的开放海洋。在水量丰富的游戏模式上，如**酸岛**，一个熔岩桶因此可以将大量海洋转换为生成器方块，并随之提升岛屿等级。两种方法来防止这种情况：

    - **不给玩家 `STONE` 层级。** 仅使用 `COBBLESTONE` 和/或 `BASALT` 类型，所以生成方块需要一个适当构建的生成器。
    - **限制高度范围。** 给 `STONE` 层级一个最小和最大 Y，排除海平面，所以它们在洞穴或高于水面的地方工作但不在海洋表面。参见[每方块高度范围](#按方块高度范围)。

### 生成器耗尽（速率限制）

自 **2.8.0** 起，生成器可以被设上限制，以便在一段时间内只产生一定数量的方块，然后进入冷却状态 — 适用于阻止完全自动化的 AFK 农场。该功能是**可选的，默认禁用**（限制为 `0`），所以现有设置不受影响，直到你启用它。当生成器暂时处于冷却状态时，玩家会收到 `generator-exhausted` 消息。

=== "exhaustion.limit"
    !!! summary "说明"
        生成器在单个耗尽期间可能产生的默认方块数。`0` 或更少禁用限制（默认值）。每个生成器层级可以通过每层级的 `exhaustion-limit` 密钥覆盖此设置（见下文）。

        默认值：`0`

=== "exhaustion.period"
    !!! summary "说明"
        耗尽期的长度，以**分钟**为单位。方块计数在每个周期结束时重置。

        默认值：`60`

=== "exhaustion.cooldown"
    !!! summary "说明"
        生成器达到其耗尽限制后保持冷却的时间，以**分钟**为单位。

        默认值：`1440`（24 小时）

=== "exhaustion.notification-cooldown"
    !!! summary "说明"
        向同一玩家显示两个耗尽警告消息之间的最少时间，以**秒**为单位。

        默认值：`60`

!!! tip "按层级限制"
    每个生成器层级可以通过生成器模板（以及管理员 GUI）中的 `exhaustion-limit` 密钥覆盖全局限制，所以不同层级可以独立节流。

### 按方块高度范围

同样自 **2.8.0** 起，生成器 — 以及生成器内的单个方块 — 可以限制为最小和最大 Y 级别，所以不同的材料在不同的高度产生。新的 GUI 按钮让管理员设置和清除范围，生成器说明向玩家显示每个生成器的运行位置。没有高度范围的遗留模板保持完全兼容。

### 解锁进程与要求

自 **2.9.0** 起，生成器可以设置更丰富的要求门槛，让你能够设计真正的解锁树，而不是一份扁平的等级列表。以下所有内容都在管理员 GUI 的生成器编辑面板中配置：

- **前置生成器** —— 要求先解锁一个或多个其他生成器，从而构建多步进程。
- **AOneBlock 阶段要求** —— 在 AOneBlock 游戏模式上，将生成器门槛设为特定的岛屿阶段，使各等级随岛屿的推进而解锁。
- **OneBlock 破坏方块数要求** —— 将生成器门槛设为在 OneBlock 岛屿上破坏的方块数量。
- **解锁即激活** —— 一个针对每个生成器的选项，在生成器解锁的那一刻自动激活它，为玩家省去一趟 GUI。
- **购买确认** —— 可选择在购买生成器扣款前要求明确确认，防止误购。

=== "lose-tiers-on-level-loss"
    !!! summary "描述"
        *在 2.9.0 中新增。* 恢复 2.0.0 之前的行为：如果岛屿等级之后跌破要求，通过岛屿等级解锁的生成器会被重新锁定。已购买的等级始终保留 —— 只有免费的、按等级解锁的等级会被重新锁定。升级后首次加载时会自动写入 `config.yml`。

        默认值：`false`

!!! warning "受权限门槛限制的生成器现在会被撤销"
    自 **2.9.0** 起，当岛屿当前（在线）拥有者不再持有所需权限时 —— 例如在所有权转移之后 —— 通过权限解锁的生成器会被重新检查并从该岛屿的已解锁和已激活列表中**撤销**。已购买的等级会被保留，因此如果重新获得权限，访问权限会恢复；离线拥有者不受影响。以前这样的授予是永久性的。

### 自定义方块产出（ItemsAdder、CraftEngine、Oraxen、Nexo）

自 **2.10.0** 起，生成器等级可以产出来自 ItemsAdder、CraftEngine、Oraxen 和 Nexo 的**自定义方块**，而不仅限于原版材料 —— 例如一个镶嵌钻石的 ItemsAdder 矿石可以和其他所有方块一起进入加权随机的产出组合中。对这些插件的所有访问都通过 BentoBox 核心钩子进行路由，因此该附属从不直接依赖它们。

- 方块以字符串 ID 存储：原版名称如 `COBBLESTONE`，或带提供者前缀的 ID `itemsadder:namespace:id`、`craftengine:namespace:id`、`oraxen:id`、`nexo:id`。**现有数据库和模板可原样加载。**
- 管理员编辑面板新增了一个**添加自定义方块**按钮 —— 在聊天中输入 ID，它会根据钩子注册表进行验证。面板会以提供者自身的纹理和显示名称渲染自定义方块。
- 如果所选的自定义方块在生成时不可用（提供者或方块缺失），生成器会回退到原版方块，并通过 `/[admin_command] generator why` 报告原因，而不是无声地失败。模板中未注册的自定义方块会在导入时给出警告，从而使模板在各服务器间保持可移植。

!!! note "提供者可用性"
    ItemsAdder 和 CraftEngine 目前即可生成方块。Oraxen 和 Nexo 已接线就绪，将在对应的 BentoBox 核心钩子发布后生成（BentoBox 3.20.0 添加了 Nexo 钩子和 `OraxenHook.placeBlock`）。

!!! warning "需要 BentoBox 3.19.1 或更新版本"
    2.10.0 依赖 BentoBox 3.19.1 中新增的自定义方块钩子 API，**无法在更旧的核心上加载**。放入此 jar 前请先更新 BentoBox。

## 指令

!!! 小贴士
    `[player_command]` 和 `[admin_command]` 是根据你运行的游戏模式而不同的指令。
    游戏模式的`config.yml`文件包含允许你修改这些值的选项。
    例如，在BSkyBlock上，默认的`[player_command]`是`island`，默认的`[admin_command]`是`bsbadmin`。
    注意，这个插件允许在插件`config.yml`文件中更改玩家指令别名。

=== "玩家指令"
    - `/[player_command] generator`：访问生成器选择GUI。
    - `/[player_command] generator view <generator>`：访问特定生成器的详细视图。
    - `/[player_command] generator activate <generator> [false]`：允许激活（或停用）特定生成器。
    - `/[player_command] generator buy <generator>`：允许购买特定生成器。

=== "管理员指令"
    - `/[admin_command] generator`：访问插件的管理员GUI
    - `/[admin_command] generator import`：导入默认模板文件 - `/plugins/BentoBox/addons/MagicCobblestoneGenerator/generatorTemplate.yml`。
    - `/[admin_command] generator database import <file>`：能够导入导出的数据库<file>。
    - `/[admin_command] generator database export <file>`：能够将数据库导出到保存在`/plugins/BentoBox/addons/MagicCobblestoneGenerator/`文件夹中的<file>。
    - `/[admin_command] generator why <player>`：一个调试指令，允许为每个玩家找到生成器问题。
    - `/[admin_command] generator reset <player>`：在确认提示后重置某个玩家的岛屿生成器数据 —— 已解锁、已购买和已激活的生成器。*（在 2.9.0 中新增。）*

## 权限

!!! 小贴士
    `[gamemode]` 是一个根据你运行的游戏模式而不同的前缀。
    前缀是游戏模式的小写名称，即如果你使用BSkyBlock，前缀是`bskyblock`。
    类似地，如果你使用AcidIsland，前缀是`acidisland`。

=== "玩家权限"
    - `[gamemode].stone-generator` - 让玩家使用`/[player_command] generator`指令及其子指令。
    - `[gamemode].stone-generator.active-generators.3` - 设置岛屿所有者可以拥有的最大活跃生成器数量。3可以被任何正整数替换。这只是一个例子。
    - `[gamemode].stone-generator.max-range.30` - 设置生成器继续

工作的最大距离。30可以被任何正整数替换。这只是一个例子。
    - `[gamemode].stone-generator.bundle.[bundle_id]` - 指定将用于用户拥有的岛屿的套餐。

=== "管理员权限"
    - `[gamemode].admin.stone-generator` - 让玩家使用`/[admin_command] generator`指令及其子指令。
    - `[gamemode].admin.stone-generator.why` - 让玩家使用调试指令`/[admin_command] why generator <player>`。
    - `[gamemode].admin.stone-generator.database` - 让玩家使用`/[admin_command] generator database`指令及其子指令。
    
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
    
    - 通过使用游戏内GUI，可通过`/[admin] generator`指令访问。
    - 通过向模板文件添加生成器。
    - 通过向导出的数据库文件添加生成器。

??? question “我在模板/数据库文件中添加了生成器，但它在游戏中不显示。”
    为了更容易地配置多个游戏模式，生成器存储在内部数据库中。编辑模板或数据库文件后，您需要将它们导入到内存中。您可以通过点击Admin GUI中的`导入模板`或`导入数据库`按钮来完成。
    
    ![template](resources/import_template.png){: loading=lazy }
    ![database](resources/import_database.png){: loading=lazy }

??? question “我有一个生成器显示在Admin GUI中，但玩家看不到它。”
    最有可能是由于”部署”状态。为了避免在管理员添加它们时玩家开始激活生成器的问题，生成器是未部署的，没有人可以使用它们。您可以通过编辑Admin GUI中的生成器并点击编辑生成器GUI中的开关来激活它们。
    ![deployed](resources/deployed.png){: loading=lazy }

??? question “玩家在海洋上使用熔岩桶来生成方块。我怎样才能阻止这种情况？”
    这是一个 `STONE` 生成器按设计工作：原版把水变成石头，无论何时熔岩流入到它，所以一个 `STONE` 层级在玩家可以到达的任何水处触发，开放海洋也包括在内。要么停止发放 `STONE` 层级，改用 `COBBLESTONE` 和/或 `BASALT` 类型，要么给你的 `STONE` 层级一个排除海平面的高度范围。参见[生成器类型](#生成器类型方块流产生的熔岩机制)。

??? question “什么是宝藏？”
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

## 更新日志

??? warning "v2.10.0 新内容 — 自定义方块，需要 BentoBox 3.19.1"
    **发布于：** 2026-07-11

    生成器现在可以产出来自其他插件的自定义方块，通过 BentoBox 核心钩子进行路由。

    - 🔺 **自定义方块支持。** 生成器等级除了原版材料外，还可以产出来自 **ItemsAdder、CraftEngine、Oraxen 和 Nexo** 的方块。方块以字符串 ID 存储（`COBBLESTONE`，或 `itemsadder:namespace:id`、`craftengine:namespace:id`、`oraxen:id`、`nexo:id`）；现有数据库可原样加载。修复 [#103](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/issues/103)。详见上面的"配置"部分。
    - ✨ **添加自定义方块面板按钮**，通过聊天输入并根据钩子注册表进行验证；面板会以提供者自身的纹理和名称渲染自定义方块。不可用的自定义方块会回退到原版方块并给出 `/why` 报告，而不是无声地失败。ItemsAdder 和 CraftEngine 目前即可生成；Oraxen 和 Nexo 在 BentoBox 3.20.0 的钩子就位后即可生成。
    - 🐛 **宝藏几率的编辑现在会保存。** 在管理员面板中编辑宝藏几率时写入的是已弃用的 `treasureChanceMap` 而非 `treasureItemChanceMap`，导致编辑丢失 —— 现已修复。
    - ⚙️ **模板接受自定义方块。** `generatorTemplate.yml` 现在接受带引号、带提供者前缀的方块键。现有配置无需任何操作；未注册的自定义方块导入时会给出警告。
    - 🔡 **本地化说明：** 为自定义方块 UI 新增了 `en-US.yml` 键。请重新生成或更新你的本地化文件以获取新字符串。
    - 🔺 **需要 BentoBox 3.19.1 或更新版本。** 此版本调用的自定义方块钩子 API 仅在 3.19.1 及以后可用；该附属无法在更旧的核心上加载。请先更新 BentoBox。

    [发布 v2.10.0](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/releases/tag/2.10.0)

??? warning "v2.9.0 新内容 — 受权限门槛限制的生成器现在会被撤销"
    **发布于：** 2026-07-08

    新增更丰富的解锁进程以及若干管理员/API 改进。

    - 🔒 **前置生成器。** 将生成器门槛设为一个或多个其他生成器，让各等级按设计好的进程解锁。通过新的管理员 GUI 选择器配置。修复 [#88](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/issues/88)。
    - 🧱 **OneBlock / AOneBlock 门槛。** 要求特定的 AOneBlock 阶段，或在 OneBlock 岛屿上破坏一定数量的方块，生成器才会可用。修复 [#121](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/issues/121)、[#117](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/issues/117)。
    - ⚙️ **等级下降时重新锁定等级层。** 新的 `lose-tiers-on-level-loss` 设置（默认 `false`）会在岛屿等级下降时重新锁定按等级解锁的生成器。已购买的等级始终保留。修复 [#118](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/issues/118)。
    - ✨ **解锁即激活。** 生成器现在可以在解锁的那一刻自动激活。修复 [#106](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/issues/106)。
    - 💰 **购买确认。** 可选择在为生成器扣款前要求玩家确认。修复 [#109](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/issues/109)。
    - 🛠️ **管理员数据重置。** 新的 `/[admin_command] generator reset <player>` 指令会在确认提示后重置某个玩家的已解锁、已购买和已激活的生成器。修复 [#149](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/issues/149)。
    - 🔌 **新的可取消 API 事件** `GeneratorPreBuyEvent` 和 `GeneratorTreasureDropEvent`，供其他插件挂接（见下面的 API 部分）。
    - 🔺 **行为变更：** 当岛屿的在线拥有者不再持有所需权限时 —— 例如在所有权转移之后 —— 受权限门槛限制的生成器现在会被**撤销**。已购买的等级会被保留，因此如果重新获得权限，访问权限会恢复。
    - 🔡 **本地化说明：** 为前置选择器、解锁即激活、购买确认、管理员重置指令以及 OneBlock/AOneBlock 要求消息新增了 `en-US.yml` 键。请重新生成或更新你的语言文件以获取新字符串。

    [发布 v2.9.0](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/releases/tag/2.9.0)

??? warning "v2.8.0 新内容 — 需要 BentoBox 3.14.0 / Java 21"
    **发布于：** 2026-07-03

    - ⚙️ **生成器耗尽。** 可选地限制生成器每个周期产生多少方块，达到限制后进入冷却。全局配置（`config.yml` 中的 `exhaustion.*`）和按生成器层级配置（模板中的 `exhaustion-limit`）。可选的，默认禁用。详见上面的"配置"部分。
    - **按方块高度范围。** 将生成器和单个方块限制到最小/最大 Y 级别，配合新的 GUI 控制和面向玩家的说明。
    - 🔡 **新占位符** `[gamemode]_magiccobblestonegenerator_generator_exhaustion_status` 和 `[gamemode]_magiccobblestonegenerator_exhausted_generator_names` 公开耗尽状态。
    - 🔡 🔺 **MiniMessage 本地化 + 13 种新语言。** 每个语言文件都从旧版 `&`/`§` 颜色代码转换为 MiniMessage（BentoBox 3.14 原生渲染），并添加了 cs、hr、hu、id、it、ja、ko、lv、nl、pt、pt-BR、ro 和 zh-HK 的翻译 — 共 24 种本地化，与 BentoBox 核心匹配。如果你保留了对任何 `locales/*.yml` 的自定义编辑，请以 MiniMessage 格式重新应用它们（或删除文件以重新生成新的）。
    - 🔺 **针对 BentoBox 3.14 / Java 21 现代化。** 更新到当前 BentoBox API 和 Paper，测试套件迁移到 MockBukkit。此版本不会在较旧的 BentoBox 或 Java 版本上加载 — 请先更新 BentoBox。

    [发布 v2.8.0](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/releases/tag/2.8.0)

## 翻译

{{ translations("MagicCobblestoneGenerator") }}

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

=== "GeneratorPreBuyEvent"
    !!! summary "描述"
        在生成器被购买**之前**触发的事件，允许取消或检查此次购买。继承共享的 `GeneratorEvent` 基类。
        此事件可取消。

        自 2.9.0 版本起。

        类链接：[GeneratorPreBuyEvent](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/blob/develop/src/main/java/world/bentobox/magiccobblestonegenerator/events/GeneratorPreBuyEvent.java)

    !!! question "变量"
        - `String islandUUID` - 目标岛屿 ID。
        - `UUID targetPlayer` - 购买生成器的玩家的 ID。
        - `String generator` - 被购买生成器的名称。
        - `String generatorID` - 被购买生成器的 ID。


    !!! example "代码示例"
        ```java
        @EventHandler(priority = EventPriority.LOW)
        public void onGeneratorPreBuy(GeneratorPreBuyEvent event) {
            UUID user = event.getTargetPlayer();
            String island = event.getIslandUUID();
            String generatorID = event.getGeneratorID();

            // 如有需要，否决此次购买
            if (someCondition) {
                event.setCancelled(true);
            }
        }
        ```

=== "GeneratorTreasureDropEvent"
    !!! summary "描述"
        在生成器即将掉落宝藏时触发的事件，允许取消或修改该掉落。继承共享的 `GeneratorEvent` 基类。
        此事件可取消。

        自 2.9.0 版本起。

        类链接：[GeneratorTreasureDropEvent](https://github.com/BentoBoxWorld/MagicCobblestoneGenerator/blob/develop/src/main/java/world/bentobox/magiccobblestonegenerator/events/GeneratorTreasureDropEvent.java)

    !!! question "变量"
        - `String islandUUID` - 目标岛屿 ID。
        - `UUID targetPlayer` - 宝藏为其掉落的玩家的 ID。
        - `String generator` - 掉落宝藏的生成器的名称。
        - `String generatorID` - 掉落宝藏的生成器的 ID。
        - `Location location` - 宝藏即将掉落的位置。
        - `ItemStack itemStack` - 即将掉落的宝藏物品（可被修改）。


    !!! example "代码示例"
        ```java
        @EventHandler(priority = EventPriority.LOW)
        public void onTreasureDrop(GeneratorTreasureDropEvent event) {
            Location location = event.getLocation();
            ItemStack treasure = event.getItemStack();

            // 取消掉落或替换物品
            event.setCancelled(true);
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