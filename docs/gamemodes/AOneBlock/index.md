# AOneBlock

**AOneBlock** 是我们对 **IJAminecraft** 流行的生存地图：OneBlock 的独特改编。
玩家需要在一个似乎具有魔法的单个方块上生存...

由 [tastybento](https://github.com/tastybento) 创建和维护。

{{ addon_description("AOneBlock") }}

OneBlock 将你放置在太空中的一个方块上。只有一个方块。你接下来会做什么？

## 安装

0. 安装 BentoBox 并至少运行一次在服务器上，以创建其数据文件夹。
1. 将此 jar 放置在 BentoBox 插件的 addons 文件夹中。
2. 重启服务器。
3. 插件将创建世界和一个数据文件夹，在文件夹内将有一个 config.yml 和 phases 文件夹中的配置文件。
4. 停止服务器。
5. 按照您希望的方式编辑 config.yml 和 .yml 配置文件。
6. 如果您进行的更改会影响它们，则删除默认创建的任何世界。
7. 重启服务器。

## 配置

主要的 `config.yml` 文件包含关于游戏模式插件设置的基本信息。

`phases` 包含将在您的 AOneBlock 世界中出现的所有阶段的信息。

`panels` 允许自定义一些用户可访问的面板。

### config.yml

插件成功安装后，它将创建 config.yml 文件。这个文件中的每个选项都附带了关于它们的注释。请检查文件以获取更多信息。
您可以在此处找到最新的配置文件：[config.yml](https://github.com/BentoBoxWorld/AOneBlock/blob/develop/src/main/resources/config.yml)

### 阶段索引 —— `phases_index.yml`

!!! new "AOneBlock 1.26.0 新增"
    `phases_index.yml` 与 `phases` 文件夹并列存放，是决定哪些阶段会被加载、以什么顺序加载、每个阶段有多长、以及各自需要哪个 Minecraft 版本的唯一依据。它会在解析任何阶段文件**之前**被读取，因此对于需要更高 Minecraft 版本的阶段，其 YAML——以及其中的任何物品——完全不会被触碰就直接跳过。

`phases:` 列表中的每一项可以包含以下字段：

| 字段 | 含义 |
|---|---|
| `file` | `phases` 文件夹中阶段文件的基础名称，不含 `.yml`。对应的宝箱文件为 `<file>_chests.yml`。 |
| `section` | 阶段文件内部的顶层键（历史上是起始方块数）。 |
| `name` | 显示名称，用于日志和 `/[admin_command] phases` 面板。 |
| `length` | 该阶段包含的方块数量。 |
| `enabled` | 可选，默认为 `true`。设为 `false` 可以排除某个阶段。 |
| `requiredMinecraftVersion` | 可选。在低于此版本的服务端上，该阶段会被跳过——完全不占用任何方块数。 |

起始方块数是**计算得出的**：它等于其上方所有已启用阶段长度的累加和，从 0 开始。这意味着阶段可以随意重新排序，被跳过的阶段也会从进度中自动收起。最后一个阶段结束后，方块计数会跳到 `gotoAtEnd`。

当你第一次在 `/[admin_command] phases` 中编辑长度时，顶层的 `adminLengths: true` 会被自动写入。从此以后，协调过程再也不会重新计算长度，因此你设置的值可以在后续的文件新增、重命名和升级中保留下来。

#### 协调（Reconciliation）

!!! note "自 1.26.1 起，phases 文件夹是唯一依据"
    每次加载时，以及每次从管理面板保存时，索引都会与磁盘上实际存在的文件进行协调，因此 `/[admin_command] phases` 显示的就是服务器真正运行的内容。请留意启动日志中以 `Phase index:` 开头的行——它们会准确说明改动了什么。

- 文件在插件版本之间被**重命名**的条目，会按阶段名称重新指向你的文件，因此该阶段可以重新加载。
- 文件**缺失但 jar 中自带**的条目会被自动恢复。这正是升级后的服务器能出现新阶段的原因，因为 `phases/` 中的文件从不会被覆盖。
- 放进该文件夹的**自定义阶段文件**会被自动添加。数字键会按其历史起始方块数插入到相应位置；其他文件则会追加到末尾，供你在面板中排列。
- 文件确实已经消失的条目会被移除并给出警告，因此面板永远不会列出不存在的阶段。
- 在需要修复时，长度会依据你的文件中历史遗留的起始方块键重新计算，从而保留服务器在索引出现之前实际运行的布局——除非已设置 `adminLengths`。

!!! warning "删除阶段"
    要永久移除一个阶段，请删除它的文件，或在 `/[admin_command] phases` 中把它关闭。只删除索引条目是没用的——协调过程会重新加入它在文件夹中找到的任何阶段文件。

    格式错误的索引会回退到旧的直接加载文件方式，因此一次错误的编辑不会让插件卡死。

### 阶段配置文件

阶段的配置文件位于 `phases` 文件夹中。

每个阶段有两个文件 - 一个包含方块和怪物的文件，以及一个包含宝箱的文件。

任何文件的第一个数字是需要开采多少个方块才能达到该阶段。这是阶段的关键数字。

!!! tip "自 1.26.1 起，阶段文件名中的数字是可选的"
    自定义阶段文件不再需要在文件名或 YAML 小节键中带上起始方块数——带有 `desert:` 小节的 `desert.yml` 即可正常工作。宝箱文件仍然按文件名配对（`<file>_chests.yml`）。内置文件中的数字属于历史遗留：既然索引说了算，面板中的起始值和长度才是准的。数字键仍然有用，因为它们告诉协调过程某个文件应该放在哪里、原本有多长。

=== "name"
    !!! summary "描述"
        阶段的显示名称。这个名称将在玩家尝试查看阶段的所有地方显示。

=== "icon"
    !!! summary "描述"
        阶段图标仅在 `phases` 面板中使用。

        图标是使用 [BentoBox ItemParser](https://docs.bentobox.world/en/latest/BentoBox/ItemParser/) 创建的。

=== "fixedBlocks"
    !!! summary "描述"
        fixedBlocks 部分允许在玩家破坏时强制某些方块。首先是阶段中的方块数量，然后是 Bukkit 材料。阶段中的第一个方块索引为 0，而添加的数字大于阶段运行时间，则意味着它将不会被达到。
        
        您可以在这里找到可用的值：[Materials](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)    
    
        我们建议使用不需要支持方块的方块（如火把、铁轨、植物）。

    !!! example "示例"
        ```yaml
            0: GRASS_BLOCK
            1: GRASS_BLOCK
            2: GRASS_BLOCK
            50: SPONGE
        ```

    !!! tip "CHEST_WITH_X 写法"
        fixedBlocks 条目可以使用 `CHEST_WITH_X` 简写来放置预先填充特定物品的箱子，例如 `CHEST_WITH_WATER_BUCKET`。物品必须是有效的 Bukkit 材料名称。

=== "holograms"
    !!! summary "描述"
        AOneBlock 使用 [Holographic Displays](https://dev.bukkit.org/projects/holographic-displays) 插件显示这些行。显示在任何阶段开始之前的第一行位于 aoneblock locales 文件中。
        
        类似于 `fixedBlocks`，`holograms` 也从显示它应该显示的数字开始，后跟显示的文本。

    !!! example "示例"
        ```yaml
            0: "&a第一个方块是

草！"
            1: "&a第二个方块是草！"
            2: "&c如果没有下一个方块怎么办？"
            3: "&a祝你好运！"
        ```

=== "biome"
    !!! summary "描述"
        `biome` 是一个实验性选项。然而，它只改变“魔法”方块位置的生物群系。
        因此，我们建议使用具有更改整个岛屿生物群系选项的 Biomes 插件。
        您可以在阶段开始命令中使用它，这将触发生物群系变化。

=== "requiredMinecraftVersion"
    !!! summary "描述"
        自 1.26.0 起，一个阶段、单个方块或单个怪物都可以声明自己所需的最低 Minecraft 版本。凡是服务器版本过低而无法支持的内容，都会被跳过并只输出一行 info 日志，而不再抛出 `Tried to load invalid item` 或 `ConfigurationSerialization` 错误。

        在阶段这一层，该值同样应写在 `phases_index.yml` 中，这样阶段在其文件被解析之前就可以被跳过。设置在阶段层级时，该阶段在较旧的服务端上完全不占用方块数，其后的阶段会自动向前收起。

        单个 `blocks` 和 `mobs` 条目可以使用对象写法，包含 `weight` 以及各自的 `requiredMinecraftVersion`。宝箱文件现在逐个物品读取，因此你的服务器版本不认识的物品会被单独跳过，宝箱中其余内容照常加载。

    !!! example "示例"
        ```yaml
            blocks:
              NETHERRACK: 300
              DRIED_GHAST:
                weight: 25
                requiredMinecraftVersion: '1.21.6'
        ```

=== "start-commands"
    !!! summary "描述"
        `start-commands` 部分允许定义在玩家开始此阶段时将触发的命令。
    
        命令作为控制台运行，除非命令前缀为 `[SUDO]`，那么命令将作为触发命令的玩家运行。
    
        这些占位符将在命令字符串中被替换为相应的值：
    
        - `[island]` - 岛屿名称
        - `[owner]` - 岛屿所有者的名称
        - `[player]` - 破坏方块触发命令的玩家名称
        - `[phase]` - 此阶段的名称
        - `[blocks]` - 破坏的方块数量
        - `[level]` - 你的岛屿等级（需要 Levels 插件）
        - `[bank-balance]` - 你的岛屿银行余额（需要 Bank 插件）
        - `[eco-balance]` - 玩家的经济余额（需要 Vault 和经济插件）

    !!! example "示例"
        ```yaml
            start-commands:
            - 'give [player] WOODEN_AXE 1'
            - 'broadcast [player] 刚刚开始了 OneBlock！'
            - 'obadmin biomes set [player] aoneblock_fields ISLAND!'
        ```

=== "end-commands"
    !!! summary "描述"
        `end-commands` 部分允许定义在玩家完成此阶段时将触发的命令。
    
        命令作为控制台运行，除非命令前缀为 `[SUDO]`，那么命令将作为触发命令的玩家运行。
    
        这些占位符将在命令字符串中被替换为相应的值：
    
        - `[island]` - 岛屿名称
        - `[owner]` - 岛屿所有者的名称
        - `[player]` - 破坏方块触发命令的玩家名称
        - `[phase]` - 此阶段的名称
        - `[blocks]` - 破坏的方块数量
        - `[level]` - 你的岛屿等级（需要 Levels 插件）
        - `[bank-balance]` - 你的岛屿银行余额（需要 Bank 插件）
        - `[eco-balance]` - 玩家的经济余额（需要 Vault 和经济插件）

    !!! example "示例"
        ```yaml
            end-commands:
            - '[SUDO]say 刚刚完成了 [phase]'
        ```

=== "requirements"
    !!! summary "描述"
        `requirements` 部分允许限制访问下一阶段，直到满足特定要求。
        目前，有 5 个要求字段：
    
        - `economy-balance` - 最低玩家经济余额（需要 Vault 和经济插件）
        - `bank-balance` - 最低岛屿银行余额（需要 Bank 插件）
        - `level` - 岛屿等级（需要 Levels 插件）
        - `permission` - 权限字符串
        - `cooldown` - 阶段上次启动后必须经过的最少秒数（防止快速切换阶段）

    !!! example "示例"
        ```yaml
            requirements:
              bank-balance: 10000
              level: 10
              permission: ready.for.battle
              cooldown: 60
        ```

=== "blocks"
    !!! summary "描述"
        blocks 部分列出 Bukkit 材料及其相对概率。
    
        您可以在这里找到可用的值：[Materials](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)
    
        整个阶段的所有概率值都会加起来，方块放置的机会是相对概率除以所有概率的总和。

    !!! example "示例"
        ```yaml
            blocks:
              GRASS_BLOCK: 2
              STONE: 3
        ```
        
        此示例显示草方块生成的机会为 40%，而生成石头的机会为 60%。 (2 / (2+3)) 和 (3 / (2+3))

=== "mobs"
    !!! summary "描述"
        mobs 部分列出可以生成的怪物及其相对概率以及方块。
        您只能在此列表中列出可以存活并且可以生成的实体。[EntityTypes](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/entity/EntityType.html)

    !!! example "示例"
        ```yaml
            mobs:
              COW: 150
              SPIDER: 75
        ```

=== "Custom Blocks"
    !!! summary "描述"
        从版本 1.11 开始，您现在可以指定自定义方块（感谢 [@HSGamer](https://github.com/HSGamer)）。
        您可以在 blocks 和 fixed-blocks 两个地方定义自定义方块。
        
        要在 `blocks` 部分定义自定义方块，您需要在每个元素前添加 `-`。
        此外，必须使用类型、数据和概率值定义方块。
        支持的类型有：
        
          - `block-data` - 使用 `/setblock` 命令将方块放置在世界中。需要 `data` 字段
          - `mob` - 使用生成实体 API 创建请求的实体。需要 `mob` 字段，以及可选的 `underlying-block` 字段（默认值：STONE）
          - `itemsadder` - 使用 [ItemsAdder](https://itemsadder.devs.beer/) API 创建方块。需要 `id` 字段。必须安装 ItemsAdder 插件。
          - `nexo` - 使用 [Nexo](https://polymart.org/resource/nexo.6901) API 创建方块。需要 `id` 字段。必须安装 Nexo 插件。
          - `craftengine` - 使用 [CraftEngine](https://github.com/Xiao-MoMi/craft-core) API 创建方块。需要 `id` 字段。必须安装 CraftEngine 插件。需要 BentoBox 3.15.0+。

    !!! example "示例"
        ```yaml
            fixedBlocks:
              0:
                type: block-data
                data: minecraft:chest[waterlogged=true]
              1: GRASS_BLOCK
              2: GRASS_BLOCK
            blocks:
              - type: block-data
                data: minecraft:chest[waterlogged=true]
                probability: 10
              - type: block-data
                data: minecraft:chest
                probability: 10
              - type: mob
                mob: ZOMBIE
                underlying-block: STONE
                probability: 5
              - type: itemsadder
                id: mypack:ruby_ore
                probability: 10
              - type: nexo
                id: mypack:custom_block
                probability: 10
              - type: craftengine
                id: mypack:custom_block
                probability: 10
              - DIRT: 10     # 旧语法仍然有效。
        ```

    !!! tip "ItemsAdder 和 Nexo"
        要使用来自 ItemsAdder 或 Nexo 的自定义方块，必须在服务器上安装相应的插件。
        AOneBlock 在启动时自动检测这些插件并注册相应的方块处理器。
        如果你配置了 `itemsadder` 或 `nexo` 方块但插件未安装，方块将降级为 STONE。


在宝箱文件中，它只有阶段号和宝箱部分。

=== "chests"
    !!! summary "描述"
        如果在 blocks 部分列出了 CHEST，则它将根据此部分随机填充。 
        您可以定义任意多的宝箱。第一个数字是唯一的宝箱编号。
        然后是宝箱内容，包括槽号和物品堆内容。
        最后是宝箱的稀有度，可以是 COMMON、UNCOMMON、RARE 或 EPIC。它们的几率是硬编码的，值为：62%，25%，9% 和 4%。
        
        设置宝箱的最佳方式是在游戏中进行。
        用您想要的内容填充一个宝箱，然后在看着它时输入命令 `/<admin_cmd> setchest <phase> <rarity>`，其中 <phase> 是阶段的名称，rarity 是稀有度。使用 Tab Complete 查看选项。宝箱将自动添加到 oneblocks.yml 文件中并准备使用。目前，删除宝箱必须通过编辑 oneblocks.yml 文件并重新加载插件来完成。
    
        编辑宝箱物品时要非常小心，并检查材料是否是真正的 Bukkit 材料并且拼写正确。


### 可定制 GUI

BentoBox 1.17 API 引入了一个功能，允许实现可定制的 GUI。此插件是首批使用此功能的插件之一。我们尝试尽可能简化定制，但是，某些功能需要解释。
您可以在这里找到更多

关于 BentoBox 自定义 GUI 工作原理的信息：[Custom GUI's](/en/latest/Tutorials/generic/Customizable-GUI/)

??? question "我如何定制 GUI"
    要定制插件 GUI，您需要拥有 1.10 版本。这是第一个实现它们的版本。插件将在 `/plugins/BentoBox/addons/AOneBlock` 下创建一个名为 `panels` 的新目录

??? question "什么是 `PREVIOUS`|`NEXT` 按钮类型？"
    PREVIOUS 和 NEXT 按钮类型允许创建自动分页，当您拥有的岛屿多于 GUI 中的空间时。
    这些类型在 data 下有额外的参数：

    - `indexing` - 指示按钮是否会显示页面编号。

    示例: 
    ```yaml
        icon: tipped_arrow[potion_contents={custom_color:11546150}]
        title: aoneblock.gui.buttons.previous.name
        description: aoneblock.gui.buttons.previous.description
        data:
          type: PREVIOUS
          indexing: true
        actions:
          previous:
            click-type: LEFT
            tooltip: aoneblock.gui.tips.click-to-previous
    ```

??? question "什么是 `PHASE` 按钮类型？"
    这个按钮允许玩家查看阶段名称和要求。如果用户可以更改阶段，并且他们已经达到了一个阶段，他们可以再次选择它并重播它。

    icon, title 和 description 是根据阶段属性动态生成的。然而，您可以手动更改它。

    示例: 
    ```yaml
      # icon: PLAYER_HEAD
      # title: aoneblock.gui.buttons.phase.name
      # description: aoneblock.gui.buttons.phase.description
      data:
        type: PHASE
      actions:
        select:
          click-type: LEFT
          tooltip: aoneblock.gui.tips.click-to-change
    ```


## 命令

!!! tip
    `[player_command]` 和 `[admin_command]` 是根据您运行的游戏模式不同而不同的命令。
    
    游戏模式的 `config.yml` 文件包含允许您修改这些值的选项。
    
    例如，在 AOneBlock 上，默认的 `[player_command]` 是 `ob`，默认的 `[admin_command]` 是 `oba`。
    
    请注意，此插件允许在插件 `config.yml` 文件中更改玩家命令别名。

=== "AOneBlock 独特的玩家命令"
    - `/[player_command] count`：在 chant 中发送关于当前阶段进度的消息。
    - `/[player_command] phases`：打开 GUI，允许查看和选择阶段。
    - `/[player_command] setcount <number>`：允许更改当前阶段，其中 <number> 是阶段开始编号。
    - `/[player_command] check`：在魔法方块周围产生粒子或重新生成它，如果由于某种原因它丢失了。

=== "管理员命令"
    - `/[admin_command] sanity [<phase>]`：如果阶段（或 <phase>）的宝箱正确，则发送消息。
    - `/[admin_command] setcount <player> <number>`：允许更改 <player> 的当前阶段，其中 <number> 是阶段开始编号。
    - `/[admin_command] setchest <phase> <rarity>`：将玩家正在看的宝箱保存到 <phase> 宝箱部分，并带有 <rarity>。
    - `/[admin_command] phases`：打开阶段顺序编辑器。（1.26.0 起）

    ??? tip "使用阶段顺序编辑器"
        `/[admin_command] phases` 会按顺序列出每个阶段，并显示其计算出的起始方块数、长度和状态。它编辑的是 `phases_index.yml`，放置和开关操作会立即保存索引并重新加载阶段。

        - **左键点击**一个阶段可以把它拿起来——其余阶段会向左收拢。点击它应该去的位置，即可把其他阶段向右推开并放下它，也可以使用末尾的放置槽位。点击其他任意位置，或关闭面板，都会把它放回原处且不保存。
        - **右键点击**可以开启或关闭一个阶段。
        - **Shift+左键点击**可以设置阶段的长度（1.26.1 起）。面板会关闭，并在聊天中提示当前长度；输入一个整数即可应用，输入 `cancel` 则保持不变。无效输入会重新提示，提示会在 60 秒后超时。第一次编辑长度时会把 `adminLengths: true` 写入索引，从此你设置的值再也不会被重新计算。

        已禁用的阶段显示为灰色玻璃，受版本限制的阶段显示为屏障——两者仍然可以重新排序。没有配置图标的阶段会使用它的第一个方块作为图标。


默认情况下，BentoBox GameMode 插件附带默认的子命令集，但是，每个插件都可能引入更多子命令。

[完整的 AOneBlock 命令列表](Commands)


## 权限

!!! tip
    对于 AOneBlock 插件的每个位置，`[gamemode]` 前缀都必须替换为 `aoneblock`。

=== "玩家权限"
    - `aoneblock.count` - 允许

玩家使用 '/[player_command] count' 命令。默认启用。
    - `aoneblock.phases` - 允许玩家使用 '/[player_command] phases' 命令。默认禁用。
    - `aoneblock.island.setcount` - 允许玩家使用 '/[player_command] setcount' 命令。默认禁用。
    - `aoneblock.respawn-block` - 允许玩家使用 '/[player_command] check' 命令。默认启用。

=== "管理员权限"
    - `aoneblock.admin.sanity` - 允许玩家使用 '/[admin_command] sanity' 命令。默认 OP。
    - `aoneblock.admin.setchest` - 允许玩家使用 '/[admin_command] setchest' 命令。默认 OP。
    - `aoneblock.admin.setcount` - 允许玩家使用 '/[admin_command] setcount' 命令。默认 OP。
    - `aoneblock.admin.phases` - 允许玩家使用 '/[admin_command] phases' 命令打开阶段顺序编辑器。默认 OP。（1.26.0 起）

默认情况下，BentoBox GameMode 插件附带默认的子权限集，但是，每个插件都可能引入更多子权限。

[完整的 AOneBlock 权限列表](Permissions)


## 标志

AOneBlock 引入了几个用于控制游戏行为的自定义标志：

| 标志 | 类型 | 描述 | 默认值 |
|------|------|-------------|---------|
| `START_SAFETY` | 世界设置 | 启用后，玩家在创建新岛屿时会有短暂时间无法移动，以防止他们立即掉落。持续时间由配置中的 `starting-safety-duration` 设置。 | false |
| `ONEBLOCK_BOSSBAR` | 岛屿设置 | 切换是否为玩家显示 OneBlock 阶段进度的 boss 血条。仅在配置中设置 `bossbar: true` 时可用。 | true |
| `ONEBLOCK_ACTIONBAR` | 岛屿设置 | 切换是否为玩家显示 OneBlock 阶段进度的动作栏。仅在配置中设置 `actionbar: true` 时可用。 | true |
| `MAGIC_BLOCK` | 保护 | 设置破坏魔法方块所需的最低岛屿等级。默认等级为 Coop。 | COOP |


## 占位符

AOneBlock 插件有其独特的占位符。这些占位符与 AOneBlock 存储的数据相关。

|占位符|描述|AOneBlock 版本|
|--- |--- |--- |
|%aoneblock_my_island_phase%|你岛屿的阶段|1.1.2|
|%aoneblock_my_island_count%|你岛屿的方块计数|1.1.2|
|%aoneblock_visited_island_phase%|你所站立的岛屿的阶段|1.1.2|
|%aoneblock_visited_island_count%|你所站立的岛屿的方块计数|1.1.2|
|%aoneblock_my_island_next_phase%|你岛屿的下一个阶段|1.1.2|
|%aoneblock_visited_island_next_phase%|你所站立的岛屿的下一个阶段|1.1.2|
|%aoneblock_my_island_blocks_to_next_phase%|直到下一个阶段的方块数，或“无限”如果没有下一个阶段|1.5.2|
|%aoneblock_visited_island_blocks_to_next_phase%|你所站立的岛屿直到下一个阶段的方块数|1.5.2|
|%aoneblock_my_island_percent_done%|阶段完成百分比|1.5.2|
|%aoneblock_visited_island_percent_done%|你所站立的岛屿的阶段完成百分比|1.5.2|
|%aoneblock_my_island_done_scale%|你岛屿的阶段完成比例|1.5.2|
|%aoneblock_visited_island_done_scale%|你所站立的岛屿的阶段完成比例|1.5.2|
|%aoneblock_my_island_lifetime_count%|你岛屿的终身方块计数|1.10.0|
|%aoneblock_visited_island_lifetime_count%|你所站立的岛屿的终身方块计数|1.10.0|

默认情况下，BentoBox GameMode 插件附带[默认占位符集](../../BentoBox/Placeholders)，但是，每个插件都可能引入更多占位符。

[完整的 AOneBlock 占位符列表](Placeholders)

## 常见问题

??? question "你能添加功能 X 吗？"
    请在[这里](https://github.com/BentoBoxWorld/AOneBlock/issues)添加。

??? question "我遇到了一个错误，我应该在哪里报告它？"
    请在[这里](https://github.com/BentoBoxWorld/AOneBlock/issues)添加。

??? question "有哪些阶段？"
    内置了 20 个阶段，顺序如下：平原、地下、冬季、海洋、丛林、沼泽、地牢、沙漠、下界、丰饶、荒芜、深暗之域、末地、繁茂洞穴、溶洞、红树林沼泽、草甸、樱花树林、尖峭山峰、硫磺洞穴。

    每个阶段都有适合该环境的一组方块、物品和怪物。

    硫磺洞穴需要 Minecraft 26.2 或更高版本。在更旧的服务端上它会被跳过，改由尖峭山峰一直延续到循环点。你可以用 `/[admin_command] phases` 自行重新排序、禁用和调整阶段长度，也可以把自己的阶段文件放进 `phases` 文件夹。

??? question "所有阶段一共有多少个方块？"
    在 Minecraft 26.2+ 的服务端上，内置阶段共有 15,500 个方块；不含硫磺洞穴阶段时为 15,000 个。

??? question "最后一个阶段之后会发生什么？"
    阶段会重复——方块计数会跳回 `phases_index.yml` 中的 `gotoAtEnd` 值，默认为 0。

??? question "为什么我不断地跌落并死亡！"
    生存有诀窍，但可能很困难！你需要建造防御。

??? question "为什么某些方块比其他方块出现得更频繁？"
    它们就是这样！您可以在 phases 文件夹中的配置文件中设置相对概率。

??? question "我怎么知道哪个是魔法方块？"
    击中它，它会发出绿色粒子。

??? question "我的魔法方块不见了！我怎么再得到一个？"
    你必须放置一个方块。最坏的情况，杀死自己，一个将被生成。

??? question "我的魔法方块是液体！我怎样才能开采它？"
    使用桶。

??? question "哪些怪物可以生成？"
    每个阶段都有一组不同的怪物可以生成。小心，因为它们可能会推你下去！如果你仔细听，你可能会听到敌对怪物来临。

??? question "我对敌对怪物的生成没有反应时间！"
    做好准备。当你开采一个方块时仔细听，你会在它们生成之前听到敌对怪物来临的声音。如果你处于一个敌对阶段，那么预计会有怪物，并建造防御以保护自己。你可以从相当远的地方开采一个方块。

??? question "当怪物生成时，我的防御被摧毁了！为什么？"
    怪物生成时会制造空间。如果有任何东西挡道，它会被破坏并掉落。你必须相应地建造。

??? question "宝箱会生成吗？"
    是的。宝箱会随机填充当前阶段的随机物品。有普通、不常见、稀有和史诗宝箱。带有闪光的宝箱很好。

??? question "在这张地图上可以到达下界或末地吗？"
    默认情况下存在原版下界，但没有末地世界。

    然而，BentoBox 是可定制的，您可以在 AOneBlock 配置文件中启用下界岛屿和末地世界。

    请注意，魔法方块仅位于主世界。

??? question "最终目标是什么？"
    这取决于你！ 

??? question "如何使用全息图？"
    如果您使用 1.12.3 及以下版本，AOneBlock 使用 [Holographic Displays](https://dev.bukkit.org/projects/holographic-displays) 插件进行全息图。
    您需要安装这个插件才能使用全息图部分！
    
    但是，自 1.13 版本和 Minecraft 1.19.4 以来，您不再需要任何额外插件就可以显示全息图。它们将使用 Minecraft 文本实体显示。

??? question "我应该使用 Levels 插件吗？"
    这取决于你，但如果你这样做，请注意因为玩家有一个无限方块，等级可能会变得

很高。
    我建议不使用它，而是使用 Likes 插件。

## 更新日志

??? warning "v1.23.0 新内容 — 需要语言文件更新"
    **发布于:** 2026-04-11

    - **Nexo 自定义方块支持。** AOneBlock 现在支持在阶段定义中使用 [Nexo](https://github.com/Nexo-MC/Nexo) 自定义方块（与现有 ItemsAdder 支持并列）。在 phases 配置中使用 `type: nexo` 和 `id` 字段定义它们。
    - **动作栏支持十六进制/MiniMessage 颜色。** `/ob actionbar` 文本现在能正确渲染十六进制颜色和完整的 MiniMessage 格式。
    - 🔡 俄语语言文件更新为 MiniMessage 格式并修正了语法错误。
    - 修复了多个动作栏语言文件和翻译错误。

    🔺 **Nexo 支持是一个新的配置选项。** 如果你使用 Nexo，请在 phase `.yml` 文件中添加 Nexo 类型的方块条目。

    🔡 **如果有自定义内容，请重新生成语言文件。**

    [发布 v1.23.0](https://github.com/BentoBoxWorld/AOneBlock/releases/tag/1.23.0)

??? warning "v1.24.0 新内容 — 需要 BentoBox 3.15.0"
    **发布于：** 2026-04-26

    - **CraftEngine 自定义方块支持。** 阶段现在可以使用 `type: craftengine` 生成 [CraftEngine](https://github.com/Xiao-MoMi/craft-core) 方块。需要 BentoBox 3.15.0+。
    - **可按稀有度配置的箱子粒子效果。** UNCOMMON/RARE/EPIC 箱子上方显示的粒子类型和颜色现可在 `config.yml` 的 `world.chest-particles` 下配置。将粒子设为 `NONE` 可禁用该效果。
    - **`CHEST_WITH_X` 固定方块写法。** 阶段 `fixedBlocks` 现在接受 `CHEST_WITH_<ITEM>` 格式，用于放置预先填充该物品的箱子（如 `CHEST_WITH_WATER_BUCKET`）。
    - **`OBSIDIAN_SCOOPING` 默认关闭。** 新安装的默认值为 `false`。已有明确设置的服务器不受影响。
    - 🔡 无岛屿玩家的占位符默认值：`%aoneblock_my_island_phase%`、`%aoneblock_my_island_count%` 和 `%aoneblock_my_island_percent_done%` 现在分别返回 `Unknown`、`0` 和 `0%`，而不是空字符串。

    🔺 **需要 BentoBox 3.15.0 或更高版本** — 此版本无法在旧版 BentoBox 上加载。

    ⚙️ **新配置节** `world.chest-particles` — 如需配置粒子效果，请从最新 `config.yml` 中复制该节。

    🔡 **重新生成语言文件**以获取新键。

    [Release v1.24.0](https://github.com/BentoBoxWorld/AOneBlock/releases/tag/1.24.0)

??? note "v1.25.0 新内容"
    **发布于：** 2026-05-03

    - **Plenty 阶段中的蜂巢生成。** Plenty 阶段现在会以与现有蜂蜜物品相同的密度生成 `bee_nest`（内含 3 只蜜蜂，`honey_level=0`），填补了长期存在的蜂蜜养殖空缺。
    - **怪物生成后魔法方块的客户端重新同步。** 当魔法方块掷出怪物时，被取消的破坏事件会让方块在客户端看起来透明，直到下一次区块同步。方块状态现在会立即重新发送给挖掘玩家。
    - 🐛 **CraftEngine 启动顺序修复。** `AOneBlock` 的 `onEnable` 在 CraftEngine 填充其方块注册表之前运行，先前会导致大量错误的 `Bad custom block` 报错。方块解析器现在在配置加载时信任显式的 `type: craftengine` 声明，并在放置时验证 ID。
    - 🐛 **更严格的 CraftEngine 方块 ID 验证。** 空 ID 和缺少 `namespace:key` 形式的 ID 现在会在配置加载时被拒绝，而不是默默接受后在放置时失败。
    - 🐛 **可配置的箱子粒子在非 `DUST` 类型上不再崩溃。** 数据类型为非 `Void` 的粒子（如 `ITEM`、`BLOCK`、`ENTITY_EFFECT`）以前会抛出 `IllegalArgumentException`。现在会被检测、记录警告并跳过。`DUST` 和 void 数据粒子（如 `FLAME`）不受影响。

    🔺 如需新的蜂巢，请将新条目复制到您的 `phases/8500_plenty.yml`（或删除 phases 文件夹让其重新生成）— 自定义阶段文件不会在升级时被覆盖。

    [Release v1.25.0](https://github.com/BentoBoxWorld/AOneBlock/releases/tag/1.25.0)

??? note "v1.25.1 新内容"
    **发布于：** 2026-07-03

    bug 修复版本 — 即插即用替换，无配置或本地化更改。

    - 🐛 **矿工仆从现在可以再次挖掘魔法方块。** 使用 JetsMinions 矿工仆从破坏魔法方块抛出 `NullPointerException` 并将方块留作缺失状态，直到用 `/ob respawnblock` 手动恢复。仆从破坏路径不再运行仅限玩家的魔法方块保护检查，该检查导致了崩溃，所以方块像预期一样循环和重生。这个回归自 1.22.0 以来一直存在。
    - 🐛 **访问团队成员时 `my_island_*` 占位符已修复。** 当属于团队的玩家访问另一个岛屿时，`my_island_*` 占位符解析为访问的岛屿的团队数据而不是玩家自己的岛屿。现在它们总是解析为玩家自己的岛屿。

    [Release v1.25.1](https://github.com/BentoBoxWorld/AOneBlock/releases/tag/1.25.1)

??? note "v1.25.2 新内容"
    **发布于：** 2026-07-18

    bug 修复版本 —— 即插即用替换，无配置或本地化更改。

    - 🐛 **修复 Jobs Reborn 无限奖励漏洞。** 当 `MAGIC_BLOCK` 标志阻止玩家破坏魔法方块时，监听方块破坏的插件（例如 Jobs Reborn）仍然认为这次破坏成功了并照常发放奖励。由于该方块会立即重生，访客可以无限次开采同一个高价值方块来刷取职业奖励。现在被拒绝的破坏会在其他插件处理之前被取消。
    - 🐛 **`actionbar: false` 现在真的会关闭动作栏。** 如果 boss 血条处于启用状态，即使设置了 `actionbar: false`，动作栏进度显示依然会出现，反过来对 boss 血条也是如此。现在两个设置都会被遵守，而且当两者同时启用时，进度显示不会再在每次破坏方块时被更新两遍。

    [Release v1.25.2](https://github.com/BentoBoxWorld/AOneBlock/releases/tag/1.25.2)

!!! warning "v1.26.0 新内容 —— 阶段索引（升级后请检查）"
    **发布于：** 2026-07-20

    新增面向 Minecraft 26.2 服务器的硫磺洞穴阶段；而由于要把一个仅限 26.2 的阶段发布给同时运行在 1.21.x 上的插件，就必须有真正的版本处理机制，于是引入了阶段索引来控制哪些阶段被加载、以什么顺序加载、以及在哪些服务端版本上加载。兼容性：BentoBox API 3.15.0+ · Minecraft 1.21.5 或更高版本 · Java 21。

    - **硫磺洞穴阶段。** 位于 15000 位置的新阶段：硫磺与辰砂层叠在典型的地下方块之间，按 wiki 的生成权重配置了硫磺块怪、洞穴蜘蛛等怪物，还有可能掉落 *Bounce* 音乐唱片的主题宝箱。游戏结束后的循环点从 15000 移到 15500。该阶段声明了 `requiredMinecraftVersion: '26.2'`，因此在 26.2+ 的服务端上会自动出现，在更旧的服务端上则只输出一行 info 日志后跳过——由尖峭山峰一直延续到循环点。
    - 🔺 **新增 `phases_index.yml`。** 现在它是阶段顺序、长度、启用状态和所需 Minecraft 版本的唯一依据。起始方块数是其上方各阶段长度的累加和，因此阶段可以自由移动，被跳过的阶段也会从进度中自动收起。索引会在解析任何阶段文件**之前**被读取，这也彻底消除了以往较新版本的物品在较旧服务端上引发的 `Tried to load invalid item` 和 `ConfigurationSerialization` 堆栈报错。详见上面的"配置"章节。
    - **受版本限制的方块、怪物和宝箱物品。** 宝箱文件现在逐个物品读取，因此当前服务器版本不认识的物品会被跳过并输出一行日志，宝箱其余内容照常加载。方块和怪物条目支持带有各自 `requiredMinecraftVersion` 的对象写法。
    - 🔡 **新增 `/[admin_command] phases` 面板**（权限 `aoneblock.admin.phases`，默认 OP），可以在物品栏面板中通过点击来重新排序、插入和开关阶段。

    🔺 **首次启动时会根据数据文件夹中的阶段文件生成 `phases_index.yml`，** 此后由它控制阶段顺序和长度。首次启动后值得快速检查一遍，尤其是当你手工编辑过阶段时。格式错误的索引会回退到旧的直接加载文件方式，因此不会出现卡死的情况。

    🔺 **现有安装不会自动获得新的阶段文件。** `addons/AOneBlock/phases/` 中的文件从不会被覆盖。在 1.26.0 上你需要自行从 jar 中复制 `15000_sulfur_caves.yml` 和 `15000_sulfur_caves_chests.yml`；从 1.26.1 起，协调过程会帮你恢复它们。

    🔡 **为阶段顺序编辑器新增了本地化键**——请重新生成或更新已翻译的本地化文件。

    [Release v1.26.0](https://github.com/BentoBoxWorld/AOneBlock/releases/tag/1.26.0)

!!! warning "v1.26.1 新内容 —— phases 文件夹现在是唯一依据"
    **发布于：** 2026-07-21

    针对 1.26.0 阶段索引的 bug 修复版本。在 1.26.0 中，升级的服务器收到的是*原厂*的 `phases_index.yml`，它引用的是当前 jar 中的文件名——但已有的 `phases/` 文件夹里存放的是更旧的或自定义过的布局。结果是阶段悄无声息地加载失败，升级后的服务器上硫磺洞穴始终没有出现，而 `/[admin_command] phases` 显示的是一套预设，而不是服务器的真实情况。

    - 🔺 **可自我修复的阶段索引。** 现在每次加载以及每次从面板保存时，索引都会与 `phases/` 文件夹进行协调：在插件版本之间被重命名的条目会按阶段名称重新指向你的文件，缺失但 jar 中自带的条目会被恢复（因此硫磺洞穴会在升级后的 26.2 服务器上出现），自定义阶段文件会被自动添加，文件确实已经消失的条目会被移除并给出警告。在需要修复时，长度会依据你的文件中历史遗留的起始方块键重新计算，从而保留服务器实际运行过的布局。
    - 🔡 **在面板中设置阶段长度。** Shift+左键点击一个阶段，即可通过聊天提示设置它的长度。第一次编辑长度会把 `adminLengths: true` 写入 `phases_index.yml`，此后协调过程再也不会重新计算长度。
    - **阶段文件名中的数字现在是可选的。** 带有 `desert:` 小节的自定义 `desert.yml` 即可正常工作；宝箱文件仍然按文件名配对。
    - 🔡 **面板细节打磨。** 阶段图标会回退为该阶段的第一个方块而不是石头，"如何使用"说明书排成四行，每个阶段的说明文字也更短，以适应小尺寸显示器。

    🔺 **首次启动时你的 `phases_index.yml` 很可能会被重写，** 以便与 phases 文件夹中的文件保持一致。请留意日志中以 `Phase index:` 开头的行——它们会准确说明重新指向、恢复、添加或移除了什么。在 1.26.0 升级后消失的阶段会自行回来。

    🔺 **要永久移除一个阶段，请删除它的文件，** 或在面板中把它关闭。只删除索引条目已经不管用了——协调过程会重新加入它在文件夹中找到的任何阶段文件。

    🔡 **为长度输入提示和重做后的面板文本新增并修改了本地化键。**

    [Release v1.26.1](https://github.com/BentoBoxWorld/AOneBlock/releases/tag/1.26.1)

??? note "v1.26.2 新内容"
    **发布于：** 2026-07-25

    针对 1.26.0 引入的战利品回归问题的 bug 修复版本。**如果你正在使用 1.26.0 或 1.26.1，请更新。**

    - 🐛 **宝箱物品重新保留其 meta。** 自 1.26.0 起，宝箱文件改用原始 SnakeYAML 读取，而不再使用 `YamlConfiguration`，这样服务器版本不认识的物品才能被单独跳过，而不会拖垮整个宝箱文件。其副作用是读取过程中不再进行反序列化：物品的 `meta` 小节以普通 map 的形式传入，而 Bukkit 的物品反序列化器会默默忽略尚未成为 `ItemMeta` 的 meta。附魔、药水效果和名称就这样被丢弃，且日志中没有任何记录——最明显的是平原宝箱中的附魔书，但实际上所有阶段的每一件宝箱物品都受影响，包括药水、药箭、自定义命名物品、旗帜、玩家头颅和成书。

        现在宝箱物品的定义会被正确遍历，并在构建物品之前反序列化其 meta。1.26.0 的行为保持不变——你的 Minecraft 版本上不存在的物品仍会被跳过并记录一行日志——而无法读取的 meta 小节现在只会损失它自己的 meta，并在日志中说明，而不会连整件物品一起丢掉。

    无需修改阶段文件：内置阶段 YAML 中旧式的附魔名称（`PROTECTION_FALL` 之类）仍然会被服务器转换，因此自定义的宝箱文件可以原样使用。玩家**已经**取走的物品会保持现状——meta 是在宝箱填充时丢失的，因此事后没有什么可以修复。从现在起生成的每一个宝箱都是正确的。

    [Release v1.26.2](https://github.com/BentoBoxWorld/AOneBlock/releases/tag/1.26.2)

## Translations

{{ translations("AOneBlock") }}

## API

Since BentoBox 1.17 API implemented a feature that solved an issue with classloaders. Plugins that wants to use access to the code directly, now can do it.

You just need to add AOneBlock to your project as dependency. You can use Maven for that:

```xml
<dependency>
    <groupId>world.bentobox</groupId>
    <artifactId>aoneblock</artifactId>
    <version>1.10.0</version>
    <scope>provided</scope>
</dependency>
```

AOneBlock addon stores data in a separate database table.

=== "OneBlockIslands"
    !!! summary "Description"
        OneBlockIslands stores all information about island progress through phases.

        Link to the source code: [OneBlockIslands](https://github.com/BentoBoxWorld/AOneBlock/blob/develop/src/main/java/world/bentobox/aoneblock/dataobjects/OneBlockIslands.java)

    !!! question "Variables"
        - "uniqueId": the island unique ID. It is equal to the Island uniqueId.
        - "blockNumber": the current broken block number.
        - "lifetime": the overall number of broken blocks.
        - "phaseName": the current phase name.
        - "hologram": the hologram text that is shown.

    !!! example "Code example"
        To access this data, you need to access to AOneBlock addon. It can be several ways, but example bellow shows
        a generic way that is accessible from everywhere.
        
        ```java
        public void accessToAOneBlockData(@NonNull Island island) {
           BentoBox.getInstance().getAddonsManager().<AOneBlock>getAddonByName("AOneBlock").ifPresent(aOneBlock -> {
                OneBlockIslands oneBlockData = aOneBlock.getOneBlocksIsland(island);           
                        
                String islandUniqueId = oneBlockData.getUniqueId();
                int brokenBlocks = oneBlockData.getBlockNumber();
                long lifetimeBlocks = oneBlockData.getLifetime();
                String phase = oneBlockData.getPhaseName();
                String hologram = oneBlockData.getHologram();
           });
        }
        ```

### Events

AOneBlock has some custom events that are called only in AOneBlock. But BentoBox GameMode events are still triggered in AOneBlock.

=== "BlockClearEvent"
    !!! summary "Description"
        This event is triggered before entity is spawned. It contains a list of blocks that will be cleared or replaced with water.

        Can be cancelled.

        Link to the class: [BlockClearEvent](https://github.com/BentoBoxWorld/AOneBlock/blob/develop/src/main/java/world/bentobox/aoneblock/events/BlockClearEvent.java)

    !!! question "Variables"
        - `Entity entity` - entity that is spawned.
        - `List<Block> airBlocks` - the list of blocks that will be replaced with air.
        - `List<Block> waterBlocks` - the list of blocks that will be replaced with water.
        - `boolean cancelled` - the boolean that indicates if event is cancelled.
 
    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onBlockClear(BlockClearEvent event) {
            Entity entity = event.getEntity();
            List<Block> airBlocks = event.getAirBlocks();
            List<Block> waterBlocks = event.getWaterBlocks();

            boolean cancelled = event.isCancelled();
        }
        ```

=== "MagicBlockEntityEvent"
    !!! summary "Description"
        This event is triggered after entity is spawned. It just contains basic information about spawned entity.

        Link to the class: [MagicBlockEntityEvent](https://github.com/BentoBoxWorld/AOneBlock/blob/develop/src/main/java/world/bentobox/aoneblock/events/MagicBlockEntityEvent.java)

    !!! question "Variables"
        - `EntityType entityType` - entityType that is spawned.
        - `@NonNull Island island` - the island where entity is summoned
        - `@Nullable UUID playerUUID` - the user id who triggered entity spawning. Can be Null.
        - `@NonNull Block block` - the magic block location.
 
    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onMagicBlockEntity(MagicBlockEntityEvent event) {
            EntityType entityType = event.getEntityType();

            Island island = event.getIsland();
            UUID playerUUID = event.getPlayerUUID();
            Block block = event.getBlock();
        }
        ```

=== "MagicBlockEvent"
    !!! summary "Description"
        This event is triggered after magic block is broken.

        Link to the class: [MagicBlockEvent](https://github.com/BentoBoxWorld/AOneBlock/blob/develop/src/main/java/world/bentobox/aoneblock/events/MagicBlockEvent.java)

    !!! question "Variables"
        - `@Nullable ItemStack tool` - the tool that broke magic block.
        - `@NotNull Material nextBlockMaterial` - the next magic block material.
        - `@NonNull Island island` - the island where block is summoned.
        - `@Nullable UUID playerUUID` - the user id who broke magic block. Can be Null.
        - `@NonNull Block block` - the magic block location.
 
    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onMagicBlock(MagicBlockEvent event) {
            ItemStack tool = event.getTool();
            Material nextBlockMaterial = event.getNextBlockMaterial();

            Island island = event.getIsland();
            UUID playerUUID = event.getPlayerUUID();
            Block block = event.getBlock();
        }
        ```

=== "MagicBlockPhaseEvent"
    !!! summary "Description"
        This event is triggered after a new phase has started.

        Link to the class: [MagicBlockPhaseEvent](https://github.com/BentoBoxWorld/AOneBlock/blob/develop/src/main/java/world/bentobox/aoneblock/events/MagicBlockPhaseEvent.java)

    !!! question "Variables"
        - `String phase` - the name of the new phase.
        - `String oldPhase` - the name of previous phase.
        - `int blockNumber` - the block number when new phase starts.
        - `@NonNull Island island` - the island where block is summoned.
        - `@Nullable UUID playerUUID` - the user id who broke magic block. Can be Null.
        - `@NonNull Block block` - the magic block location.
 
    !!! example "Code example"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onMagicBlockPhase(MagicBlockPhaseEvent event) {
            String phase = event.getPhase();
            String oldPhase = event.getOldPhase();
            int blockNumber = event.getBlockNumber();

            Island island = event.getIsland();
            UUID playerUUID = event.getPlayerUUID();
            Block block = event.getBlock();
        }
        ```
