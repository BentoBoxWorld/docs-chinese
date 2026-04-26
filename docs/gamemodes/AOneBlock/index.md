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

### 阶段配置文件

阶段的配置文件位于 `phases` 文件夹中。

每个阶段有两个文件 - 一个包含方块和怪物的文件，以及一个包含宝箱的文件。

任何文件的第一个数字是需要开采多少个方块才能达到该阶段。这是阶段的关键数字。

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
        目前，有 4 个要求字段：
    
        - `economy-balance` - 最低玩家经济余额（需要 Vault 和经济插件）
        - `bank-balance` - 最低岛屿银行余额（需要 Bank 插件）
        - `level` - 岛屿等级（需要 Levels 插件）
        - `permission` - 权限字符串

    !!! example

 "示例"
        ```yaml
            requirements:
              bank-balance: 10000
              level: 10
              permission: ready.for.battle
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
              - DIRT: 10     # 旧语法仍然有效。
        ```


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

默认情况下，BentoBox GameMode 插件附带默认的子权限集，但是，每个插件都可能引入更多子权限。

[完整的 AOneBlock 权限列表](Permissions)


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
    有 11 个阶段：平原、地下、冬季、海洋、丛林、沼

泽、地牢、沙漠、下界、丰饶、荒芜和末地。

    每个阶段都有适合该环境的一组方块、物品和怪物。

??? question "11 个阶段中有多少个方块？"
    目前有 11 千个方块！

??? question "最后一个阶段之后会发生什么？"
    阶段会重复。

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

??? warning "v1.23.0 新内容"
    **发布于:** 2026-04-xx

    - **Nexo 自定义方块支持。** AOneBlock 现在可以在阶段配置中使用 Nexo 自定义方块作为方块和固定方块。使用 `nexo:<block_id>` 语法。
    - 🔡 动作栏消息已迁移至 MiniMessage 格式。删除 `BentoBox/addons/AOneBlock/locales/` 并重启以重新生成。

    [在 GitHub 上查看发布记录](https://github.com/BentoBoxWorld/AOneBlock/releases)

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
