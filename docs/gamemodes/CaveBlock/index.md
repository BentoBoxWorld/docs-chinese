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

!!! warning "v1.21.0 新内容 — 重大变更：世界生成重新设计"
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
