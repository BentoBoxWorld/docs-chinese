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

=== "world.world-depth"
    !!! summary "说明"
        世界深度表示世界中将生成块的高度。将其设置为 -64 将创建一个基本的虚空世界。

        允许在你的洞穴上方创建一些新鲜空气。

=== "world.generation-tries"
    !!! summary "说明"
        这允许指定将主维度方块更改为矿石方块需要多少次尝试。

=== "world.use-new-material-generator"
    !!! summary "说明"
        改进的材料生成器会生成类似原版的矿石团块、花岗岩、闪长岩和凝灰岩斑块，并使用一些深板岩。

        但是，它将禁用你通过维度方块配置添加的任何自定义设置。

=== "world.normal.roof"
    !!! summary "说明"
        允许切换主世界顶部方块是否应为基岩方块。否则，它将由石头制成。

=== "world.normal.natural-surface"
    !!! summary "说明" 
        该选项允许切换世界生成器是否应生成具有泥土和草方块的自然（类似）表面。
        目前，自然（类似）只是泥土和草方块层。

        此选项禁用 `world.normal.roof` 选项。

=== "world.normal.natural-caves"
    !!! summary "说明"
        该选项允许切换世界生成器是否应像原版世界一样生成自然洞穴。
        洞穴将使用所有方块和生物群系生成。

=== "world.normal.floor" 
    !!! summary "说明"
        允许切换主世界底部方块是否应为基岩方块。否则，它将由石头制成。

=== "world.normal.natural-bedrock"
    !!! summary "说明" 
        允许切换主世界基岩是否应像原版世界一样生成4个方块高度。

=== "world.normal.main-block"
    !!! summary "说明"
        允许设置将用于主世界生成的主要方块。将其设置为空气将创建虚空世界。

=== "world.normal.blocks"
    !!! summary "说明"
        将偶尔随机替换主要方块的方块。
        方块只会替换主方块，并会尝试创建在其字符串中设置的包。
        也需要生成的机会。
        
        对于材料，第一个字符串必须是 MATERIAL，对于实体：ENTITY。
        
        通过生成器生成的实体不受保护免于消失。
        目前仅适用于 2 格高的生物。

    !!! example "示例"
        ```yaml
            blocks:
                - MATERIAL:DIAMOND_ORE:100:5 
        ```        
        意味着每个子区块中有 100% 的机会生成钻石，最大数量为 5 个！

=== "world.nether.roof"
    !!! summary "说明"
        允许切换下界顶部方块是否应为基岩方块。否则，它将由地狱岩制成。

=== "world.nether.floor"
    !!! summary "说明"
        允许切换下界底部方块是否应为基岩方块。否则，它将由地狱岩制成。

=== "world.nether.main-block"
    !!! summary "说明"
        允许设置将用于下界世界生成的主要方块。将其设置为空气将创建虚空世界。

=== "world.nether.blocks"
    !!! summary "说明"
        将偶尔随机替换主要方块的方块。
        方块只会替换主方块，并会尝试创建在其字符串中设置的包。
        也需要生成的机会。
        
        对于材料，第一个字符串必须是 MATERIAL，对于实体：ENTITY。
        
        通过生成器生成的实体不受保护免于消失。
        目前仅适用于 2 格高的生物。

    !!! example "示例"
        ```yaml
            blocks:
                - MATERIAL:DIAMOND_ORE:100:5 
        ```        
        意味着每个子区块中有 100% 的机会生成钻石，最大数量为 5 个！

=== "world.end.roof"
    !!! summary "说明"
        允许切换末地顶部方块是否应为基岩方块。否则，它将由末地石制成。

=== "world.end.floor"
    !!! summary "说明"  
        允许切换末地底部方块是否应为基岩方块。否则，它将由末地石制成。

=== "world.end.main-block"
    !!! summary "说明"
        允许设置将用于末地世界生成的主要方块。将其设置为空气将创建虚空世界。

=== "world.end.blocks"
    !!! summary "说明"
        将偶尔随机替换主要方块的方块。
        方块只会替换主方块，并会尝试创建在其字符串中设置的包。
        也需要生成的机会。
        
        对于材料，第一个字符串必须是 MATERIAL，对于实体：ENTITY。
        
        通过生成器生成的实体不受保护免于消失。
        目前仅适用于 2 格高的生物。

    !!! example "示例" 
        ```yaml
            blocks:
                - MATERIAL:DIAMOND_ORE:100:5 
        ```        
        意味着每个子区块中有 100% 的机会生成钻石，最大数量为 5 个！

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


## 翻译

{{ translations("CaveBlock") }}
