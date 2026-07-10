# CaveBlock

**CaveBlock** 让 ~~矮人~~ 玩家在地下生存。挖矿、合成，挖洞（*diggy diggy hole*）！

由 [BONNe](https://github.com/BONNe) 创建并维护。

{{ addon_description("CaveBlock") }}

## 安装

0. 安装 BentoBox 并至少在服务器上运行一次以创建其数据文件夹。
1. 将此 jar 放入 BentoBox 插件的 addons 文件夹中。
2. 重启服务器。
3. 该插件将创建世界和一个数据文件夹，文件夹内将有一个 config.yml 文件。
4. 停止服务器。
5. 根据需要编辑 config.yml。
6. 如果你做了可能影响默认创建的世界的更改，请删除这些世界。
7. 重启服务器。

## 配置

主 `config.yml` 文件包含有关游戏模式插件设置的基本信息。

### config.yml

插件成功安装后，它将创建 config.yml 文件。此文件中的每个选项都带有相关注释。请查看文件以获取更多信息。

你可以在此找到最新的配置文件：[config.yml](https://github.com/BentoBoxWorld/CaveBlock/blob/develop/src/main/resources/config.yml)

!!! info "世界生成在 1.21.0 中重新设计"
    自 **1.21.0** 起，主世界由 Minecraft 自己的原版 1.18+ 噪声生成器雕刻，所以岛屿穿过真正的奶酪、意大利面、繁茂、滴滴答答和深暗洞穴 — 完整的原版矿石、装饰、结构和地下生物群系。然后每列被限制，所以世界保持固体岩石，没有开放天空。因为服务器现在处理雕刻、矿石和生物群系，旧的方块替换生成选项（`generation-tries`、`use-new-material-generator`、每维度 `blocks` 列表和 `natural-*` 切换）被移除。下界和末地保持填充和装饰方法，配备新的矿脉填充器。升级前请查看此页面底部的更新日志。

=== "world.world-depth"
    !!! summary "说明"
        世界深度表示世界中将生成块的高度。将其设置为 -64 将创建一个基本的虚空世界。

        允许在你的洞穴上方创建一些新鲜空气。

=== "world.structures"
    !!! summary "说明"
        *在 1.23.0 中新增。* 可能在**主世界**洞穴世界中生成的原版结构的映射。将某个结构设置为 `false` 可阻止其生成；未在此列出的结构会正常生成。使用原版结构键，例如 `ancient_city`、`trial_chambers`、`mineshaft`、`mineshaft_mesa`、`stronghold`、`mansion`、`monument`、`pillager_outpost`、`ruined_portal`、`trail_ruins`、`village_plains`、`desert_pyramid`、`jungle_pyramid`、`igloo`、`swamp_hut`。

        像远古城市和试炼密室这样的大型结构可能会填满或破坏固体洞穴世界的平衡，所以它们**默认禁用**。仅影响新生成的主世界区块。

        默认值：
        ```yaml
        structures:
          ancient_city: false
          trial_chambers: false
          mansion: false
          mineshaft: true
          stronghold: true
        ```

=== "world.overworld-cave-fill"
    !!! summary "说明"
        *在 1.23.0 中新增。* 主世界洞穴密度。原版会生成密集的 1.18+ 洞穴网络（奶酪和意大利面洞穴），在固体洞穴世界上这可能会让人感觉"除了通道什么都没有"。此设置在生成后使用低频噪声场重新固化一部分洞穴空气，使整片区域封闭成独立的腔室，而不是随机打出单个孔洞。

        - `0.0` 保留所有原版洞穴（最密集，原始行为）。
        - `1.0` 填满几乎所有洞穴（几乎全为固体）。
        - 尝试 `0.4` – `0.6` 来将它们稀释。

        无论哪种方式，地下生物群系、矿石、装饰和结构都会被保留。仅影响新生成的区块。

        默认值：`0.0`

=== "world.overworld-carvers"
    !!! summary "说明"
        *在 1.23.0 中新增。* 在主世界中生成原版雕刻洞穴（大型峡谷和长而圆的隧道）。这些叠加在噪声洞穴之上。设置为 `false` 可移除峡谷和宽隧道，同时保留噪声洞穴。

        !!! warning
            BentoBox 不支持在游戏进行中更改此值。如果你需要更改它，请对你的世界和数据库进行完整重置。

        默认值：`true`

=== "world.normal.roof"
    !!! summary "说明"
        允许切换主世界顶部方块是否应为基岩方块。否则，它将由石头制成。

=== "world.normal.floor" 
    !!! summary "说明"
        允许切换主世界底部方块是否应为基岩方块。否则，它将由石头制成。

=== "world.normal.main-block"
    !!! summary "说明"
        主要方块用于限制原版生成地形上方的空气间隙。原版洞穴雕刻、矿石、结构和地下生物群系（繁茂洞穴、滴滴答答洞穴、深暗）由服务器产生；此设置仅影响用于填充表层的材料。将其设置为空气将在洞穴上方留下开放天空。

=== "world.nether.roof"
    !!! summary "说明"
        允许切换下界顶部方块是否应为基岩方块。否则，它将由地狱岩制成。

=== "world.nether.floor"
    !!! summary "说明"
        允许切换下界底部方块是否应为基岩方块。否则，它将由地狱岩制成。

=== "world.nether.main-block"
    !!! summary "说明"
        允许设置将用于下界世界生成的主要方块。将其设置为空气将创建虚空世界。矿石脉（古代碎片、地狱石英、黑曜石、荧石等）由脉填充器在其顶部放置。

=== "world.end.roof"
    !!! summary "说明"
        允许切换末地顶部方块是否应为基岩方块。否则，它将由末地石制成。

=== "world.end.floor"
    !!! summary "说明"  
        允许切换末地底部方块是否应为基岩方块。否则，它将由末地石制成。

=== "world.end.main-block"
    !!! summary "说明"
        允许设置将用于末地世界生成的主要方块。将其设置为空气将创建虚空世界。矿脉由脉填充器在其顶部放置。

## 命令

!!! tip
    `[player_command]` 和 `[admin_command]` 是根据您运行的游戏模式而有所不同的命令。
    
    游戏模式的 `config.yml` 文件包含允许您修改这些值的选项。
    
    例如，在 CaveBlock 中，默认的 `[player_command]` 是 `cave`，默认的 `[admin_command]` 是 `cba`。
    
    请注意，此插件允许在插件的 `config.yml` 文件中更改玩家命令别名。


默认情况下，BentoBox 游戏模式插件带有默认的子命令集，但是，每个插件可能会引入更多子命令。

[完整的 CaveBlock 命令列表](Commands)

## 权限

!!! tip
    在 CaveBlock 插件的每个位置，`[gamemode]` 前缀必须替换为 `caveblock`。

默认情况下，BentoBox 游戏模式插件带有默认的子权限集，但是，每个插件可能会引入更多子权限。

[完整的 CaveBlock 权限列表](Permissions)


## 占位符

默认情况下，BentoBox 游戏模式插件带有[默认的占位符集](../../BentoBox/Placeholders)，但是，每个插件可能会引入更多占位符。

[完整的 CaveBlock 占位符列表](Placeholders)


## 标志

插件引入了 1 个 BentoBox 设置标志：

- ![feather](https://static.wikia.nocookie.net/minecraft_gamepedia/images/e/e2/Feather_JE3_BE2.png){: loading=lazy width=16px } SKY_WALKER_FLAG：世界设置中的标志，允许启用/禁用玩家在洞穴顶部行走。


## 常见问题

??? question "你能添加一个 X 功能吗？"
    请将其添加到[这里](https://github.com/BentoBoxWorld/CaveBlock/issues)的列表中。

??? question "我遇到了一个错误，我应该在哪里报告它？"
    请将其添加到[这里](https://github.com/BentoBoxWorld/CaveBlock/issues)的列表中。


## 更新日志

??? note "v1.23.0 新内容"
    **发布于：** 2026-07-07

    在 1.22.0 生成工作的基础上，将主世界洞穴世界中填充内容的直接控制权交给管理员。

    - ⚙️ **可配置的主世界结构。** `config.yml` 中新的 `structures:` 部分可切换单个原版结构（远古城市、试炼密室、林地府邸、废弃矿井、要塞等）。最大的、填满世界的结构默认禁用。修复 [#112](https://github.com/BentoBoxWorld/CaveBlock/issues/112)。
    - ⚙️ **主世界洞穴密度控制。** 新的 `overworld-cave-fill` 设置（`0.0`–`1.0`，默认 `0.0`）会重新固化一部分密集的原版洞穴网络，使世界不那么像无尽的通道，同时保持生物群系、矿石、装饰和结构完好。修复 [#111](https://github.com/BentoBoxWorld/CaveBlock/issues/111)。
    - ⚙️ **雕刻洞穴开关。** 新的 `overworld-carvers` 设置（默认 `true`）会移除原版峡谷和宽隧道，同时保留噪声洞穴。此项无法在游戏进行中更改。

    新选项会在首次运行时自动写入 `config.yml`，且仅影响**新生成的**区块；默认值保留 1.22.0 的行为，除了最大的结构现在默认关闭。详见上面的"配置"部分。

    [发布 v1.23.0](https://github.com/BentoBoxWorld/CaveBlock/releases/tag/1.23.0)

??? warning "v1.22.0 新内容 — 下界 & 末地生成重新设计"
    **发布于：** 2026-07-06

    重建**下界**和**末地**的生成方式。以前这两个维度都是一整块岩石，零星点缀着随机的单个方块 —— 包括造成卡顿的散落漂浮火焰 —— 且没有真正的洞穴。

    - 🔺 **下界 & 末地生成大修。** 两个维度现在都被填充为固体，并由 3D 噪声洞穴生成器雕刻成相连的隧道和腔室，在地板和顶部留有固体边缘。
    - 🌋 **下界岩浆海。** 最低处的洞穴空隙填充岩浆而非开放空气；地板和顶部保持固体，使世界保持封闭。
    - 🗺️ **自然的下界生物群系。** 五种下界生物群系被分配为自然的、面积大致相等的区域，因此单个岛屿内会出现多个生物群系。
    - 🌿 **生物群系感知的装饰。** 绯红/诡异菌岩、菌根、菌类和藤蔓；带有灵魂火和骸骨的灵魂沙峡谷；带有玄武岩柱和岩浆火的玄武岩三角洲；荧石天花板斑块；末地的末地烛和紫颂。
    - ⚡ **不再有卡顿的漂浮火焰。** 火焰现在稀疏且落在下界岩/岩浆块上。

    🔺 **世界生成已更改：** 新生成器仅影响**新生成的**区块。已生成的下界/末地区块保持旧外观，因此你可能会在新旧交界处看到接缝。如果你想要一致的外观，请重新生成这些维度（或开始新世界）。

    [发布 v1.22.0](https://github.com/BentoBoxWorld/CaveBlock/releases/tag/1.22.0)

??? warning "v1.21.0 新内容 — 重大变更：世界生成重新设计"
    **发布于：** 2026-06-27

    主要的生成过载。CaveBlock 现在针对 **Paper 1.21.11 on Java 21** 和 **BentoBox 3.14 API**。

    - 🔺 **原版洞穴世界生成。** 主世界委托给 Minecraft 自己的 1.18+ 噪声生成器，所以岛屿穿过真正的奶酪、意大利面、繁茂、滴滴答答和深暗洞穴，完整的原版矿石、装饰、结构（矿井、地牢、试验房间、紫水晶地洞、远古城市）和地下生物群系。天空被石头限制，所以世界从基岩保持固体岩石到屋顶。
    - 💎 **重新设计的下界 & 末地矿脉。** 下界和末地保持填充和装饰方法，配备新的脉填充器，放置正确大小的矿脉块（古代碎片、石英、黑曜石、荧石等），而不是单个方块。
    - ⚙️ **配置清理。** 世界生成设置被重新设计，死选项被移除 — `generation-tries`、`use-new-material-generator`、每维度 `blocks` 列表、`natural-surface`/`natural-caves`/`natural-bedrock` 切换和旧的 `netherBlocks`/`endBlocks`/`debug` 设置已移除。升级前备份你现有的 `config.yml`。
    - 🔡 **MiniMessage 本地化。** 所有语言文件都从旧版颜色代码迁移至 MiniMessage，并将高度限制消息密钥重命名为 `caveblock.general.errors.cave-limit-reached`。如果你自定义了它们，请重新生成你的语言文件。
    - 🧪 添加了完整的 JUnit 5 + MockBukkit 测试套件以保护生成、高度限制和附属生命周期。

    🔺 **世界生成已更改：** 新生成的主世界块现在使用原版噪声洞穴而不是固体填充雕刻。已生成的块保持不变，但世界边缘的新地形看起来会与较旧的区域不同。升级前在副本上测试，如果这对你重要。

    [发布 v1.21.0](https://github.com/BentoBoxWorld/CaveBlock/releases/tag/1.21.0)

## 翻译

{{ translations("CaveBlock") }}
