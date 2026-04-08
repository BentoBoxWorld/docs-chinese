# 岛屿飞行

**岛屿飞行**允许玩家在他们的岛屿上飞行。

由[tastybento](https://github.com/tastybento)创建和维护。

{{ addon_description("IslandFly") }}

## 安装

0. 安装BentoBox并至少运行一次服务器以创建其数据文件夹。
1. 将这个jar文件放入BentoBox插件的addons文件夹中。
2. 重启服务器。
3. 插件将创建一个数据文件夹，并且文件夹内将有一个config.yml文件。
4. 停止服务器。
5. 按你想要的方式编辑config.yml文件。
7. 重启服务器。

## 配置

插件成功安装后，它将创建config.yml文件。这个文件中的每个选项都附有注释。请检查文件以获取更多信息。
你可以在这里找到最新的配置文件：[config.yml](https://github.com/BentoBoxWorld/IslandFly/blob/develop/src/main/resources/config.yml)

=== "fly-timeout"
    !!! 摘要 "描述"
        玩家离开岛屿后插件等待多少秒才禁用飞行模式。

=== "logout-disable-fly"
    !!! 摘要 "描述"
        当玩家断开连接时是否应禁用飞行模式。

=== "disabled-gamemode"
    !!! 摘要 "描述"
        这个列表储存了哪些游戏模式中IslandFly插件不应该工作。要禁用插件，需要在以-开头的新行中写下它的名字。
        
    !!! 示例 "示例"
        ```yaml
            disabled-gamemodes:
            - BSkyBlock
        ```   

=== "allow-command-outside-protection-range"
    !!! 摘要 "描述"
        允许玩家在岛屿保护范围外使用命令。

## 命令

!!! 小贴士
    `[player_command]` 和 `[admin_command]` 是根据你运行的游戏模式而不同的命令。
    游戏模式的`config.yml`文件包含允许你修改这些值的选项。
    例如，在BSkyBlock上，默认的`[player_command]`是`island`，默认的`[admin_command]`是`bsbadmin`。

=== "玩家命令"
    - `/[player_command] fly`: 切换飞行开/关。

## 权限

!!! 小贴士
    `[gamemode]` 是一个根据你运行的游戏模式而不同的前缀。
    前缀是游戏模式的小写名称，即如果你使用BSkyBlock，前缀是`bskyblock`。
    类似地，如果你使用AcidIsland，前缀是`acidisland`。

=== "权限"
    - `[gamemode].island.fly` - (默认: `true`) - 允许玩家使用 '/[player_command] fly' 命令。
    - `[gamemode].island.flyspawn` - (默认: `op`) - 允许玩家在出生岛上飞行。
    - `[gamemode].island.flybypass` - (默认: `op`) - 允许玩家在其他玩家的岛屿上飞行。

## 常见问题解答

??? 问题 "你可以添加功能X吗？"
    请在[这里](https://github.com/BentoBoxWorld/IslandFly/issues)添加。

??? 问题 "我遇到了一个bug，我应该在哪里报告？"
    请在[这里](https://github.com/BentoBoxWorld/IslandFly/issues)添加。

## 翻译

{{ translations("IslandFly") }}

