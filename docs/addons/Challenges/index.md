# 挑战

**Challenges** 插件允许你的玩家 **完成各种可自定义的挑战并获得奖励**!

由 [BONNe](https://github.com/BONNe) 创建和维护。

{{ addon_description("Challenges") }}

## 安装

1. 将插件 jar 文件放入 BentoBox 插件的 addons 文件夹
2. 重启服务器
3. 运行管理员挑战命令,例如 `/bsbadmin challenges` 来配置插件

## 配置

默认情况下,挑战插件没有任何挑战或等级。首次运行时只有管理员 GUI 可以访问。
管理员可以创建自己的挑战或加载一组默认挑战。默认挑战包含 5 个等级和 57 个挑战。
还有一个网络库,管理员可以在其中下载公共挑战。可以通过点击管理员 GUI 中的网络图标访问它。

### config.yml

配置文件包含插件的主要功能。

最新的 config.yml 可以在[这里](https://github.com/BentoBoxWorld/Challenges/blob/develop/src/main/resources/config.yml)找到。

### 模板

挑战插件包含一个模板文件,可用于将挑战导入数据库。这个文件对于不喜欢使用游戏内 GUI 的人来说,批量添加挑战非常有用。但是请注意,模板文件并非支持所有功能,有些物品/选项只能通过 GUI 添加。
你可以拥有任意数量的模板文件。管理员 GUI 将允许选择要导入的文件。
示例模板文件: [template.yml](https://github.com/BentoBoxWorld/Challenges/blob/develop/src/main/resources/template.yml)

!!! tip
    模板文件必须包含挑战和等级。没有它们,模板将无法工作。

??? question "什么是挑战类型?"
    挑战插件有 4 种不同类型的挑战。每种类型都提供了不同的东西来测试挑战是否完成。这些类型是:

    - 物品栏挑战 (`INVENTORY_TYPE`) - 需要玩家物品栏中的物品才能完成的挑战。
    - 岛屿挑战 (`ISLAND_TYPE`) - 需要玩家岛屿上的方块或实体才能完成的挑战。
    - 其他挑战 (`OTHER_TYPE`) - 需要玩家 XP、金钱或岛屿等级才能完成的挑战。
    - 统计挑战 (`STATISTIC_TYPE`) - 需要达到玩家统计数据中某个值才能完成的挑战。

??? question "我可以为需要/奖励的物品指定附魔吗?"
    不幸的是,Spigot 没有通用的物品解析机制。所以插件作者需要自己创建。挑战插件使用 BentoBox 的[物品解析器](/en/latest/BentoBox/ItemParser/)。如果它不支持某个功能,那么你就不能使用。
    
    但是,你始终可以使用游戏内管理员 GUI 来设置你想要的任何物品。没有任何限制。

??? question "我如何知道可以在统计挑战类型中放入什么值?"
    你可以在这里找到统计类型: [Statistic](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Statistic.html)。

    一些信息可以在 fandom 网站上找到: [minecraft.fandom](https://minecraft.fandom.com/wiki/Statistics)

    但是,没有一个地方可以找到你可以指定的所有内容。我建议使用游戏内管理员 GUI 来创建统计挑战,因为它有更多选项来检测可以填写的字段。

### 可自定义的 GUI

BentoBox 1.17 API 引入了一个允许实现可自定义 GUI 的功能。挑战插件是最早使用此功能的插件之一。我们尽量让自定义变得简单,但有些功能需要解释。
你可以在这里找到更多关于 BentoBox 自定义 GUI 如何工作的信息: [自定义 GUI](/en/latest/Tutorials/generic/Customizable-GUI/)

??? question "我如何自定义 GUI?"
    要自定义挑战插件的 GUI,你需要 1.0 版本。这是第一个实现它们的版本。插件会在 `/plugins/bentobox/addons/challenges` 下创建一个名为 `panels` 的新目录。

    目前你可以自定义 3 个 GUI:

    - 主挑战面板: `main_panel` - 玩家可以看到挑战列表时打开的面板。
    - 多次完成面板: `multiple_panel` - 玩家想要指定挑战必须完成的次数时打开的面板。
    - 游戏模式选择面板: `gamemode_panel` - 当设置中启用 `commands.global-command` 并且安装了多个游戏模式时打开的面板。

    每个 GUI 都包含仅由其自身支持的功能。

??? question "`PREVIOUS`|`NEXT` 按钮类型是什么?"
    此按钮在 main_panel 和 gamemode_panel 中可用。
    PREVIOUS 和 NEXT 按钮类型允许在挑战多于 GUI 中的空间时创建自动分页。
    这些类型在 data 下有额外的参数:
    - `target` - 指示按钮是否将在 main_panel 中切换 `LEVEL` 或 `CHALLENGE`,在 gamemode_panel 中切换 `GAMEMODE`。 
    - `indexing` - 指示按钮是否显示页码。

    示例:
    ```yaml
        icon: tipped_arrow[potion_contents={custom_color:11546150}]
        title: challenges.gui.buttons.previous.name
        description: challenges.gui.buttons.previous.description
        data:
          type: PREVIOUS
          target: CHALLENGE
          indexing: true
        action:
          left: 
            tooltip: challenges.gui.tips.click-to-previous
    ```

??? question "`CHALLENGE` 按钮类型是什么?"
    此按钮在 main_panel 中可用。
    CHALLENGE 按钮为挑战创建一个动态条目。只有存在挑战时,按钮才会被填充。例如,如果你只有 3 个挑战,但在 GUI 中为挑战定义了 7 个位置,那么只有 3 个位置会被填充。其他位置将保持为空。

    默认情况下,挑战将按照它们的顺序号排序,但是,你可以使用 data 下的 `id` 参数指定特定的等级放在特定的位置。

    ```yaml
      data:
        type: CHALLENGE
        id: example_challenge
    ```

    指定标题、描述和图标将覆盖基于数据库数据的动态生成。默认情况下,这些值将从数据库条目生成。
    此按钮支持 3 种不同的操作类型:

    - COMPLETE - 只完成一次挑战。
    - COMPLETE_MAX - 尽可能多地完成挑战。
    - MULTIPLE_PANEL - 打开多次完成面板,允许选择必须完成的次数。

    示例:
    ```yaml
      data:
        type: CHALLENGE
      actions:
        left:
          type: COMPLETE
          tooltip: challenges.gui.tips.click-to-complete
        right:
          type: MULTIPLE_PANEL
          tooltip: challenges.gui.tips.right-click-multiple-open
        shift_left:
          type: COMPLETE_MAX
          tooltip: challenges.gui.tips.shift-left-click-to-complete-all
    ```

??? question "`LEVEL` 按钮类型是什么?"
    此按钮在 main_panel 中可用。
    LEVEL 按钮为挑战等级创建一个动态条目。只有存在等级时,按钮才会被填充。例如,如果你只有 3 个等级,但在 GUI 中为等级定义了 7 个位置,那么只有 3 个位置会被填充。其他位置将保持为空。

    默认情况下,等级将按照它们的进展排序,但是,你可以使用 data 下的 `id` 参数指定特定的等级放在特定的位置。

    ```yaml
      data:
        type: LEVEL
        id: example_level
    ```

    指定标题、描述和图标将覆盖基于数据库数据的动态生成。默认情况下,这些值将从数据库条目生成。

    示例:
    ```yaml
      data:
        type: LEVEL
      actions:
        left:
          tooltip: challenges.gui.tips.click-to-select
    ```

??? question "`UNASSIGNED_CHALLENGES` 按钮类型是什么?"
    此按钮在 main_panel 中可用。
    UNASSIGNED_CHALLENGES 按钮允许为自由挑战选择一个按钮。
    它没有任何额外的功能或动态生成。

??? question "`GAMEMODE` 按钮类型是什么?"
    此按钮在 gamemode_panel 中可用。
    它为每个安装了挑战的游戏模式插件生成一个按钮。

??? question "`INCREASE`|`REDUCE` 按钮类型是什么?"
    这些按钮在 multiple_panel 中可用。
    这些类型允许增加/减少挑战完成次数。

    在 `data` 下指定 `value: <number>` 允许设置不同的自定义增量/减量数。

??? question "`ACCEPT` 按钮类型是什么?"
    此按钮在 multiple_panel 中可用。
    此类型允许接受输入的数字并完成那么多次挑战。

    在操作下指定 `type: ACCEPT` 允许完成挑战。
    在操作下指定 `type: INPUT` 允许要求玩家在聊天中写入数字。

## 命令

!!! tip
    `[player_command]` 和 `[admin_command]` 是根据你运行的游戏模式而不同的命令。
    游戏模式的 `config.yml` 文件包含允许你修改这些值的选项。
    例如,在 BSkyBlock 中,默认的 `[player_command]` 是 `island`,默认的 `[admin_command]` 是 `bsbadmin`。

=== "玩家命令"
    - `/challenges`: 访问玩家挑战 GUI。包含当前世界中的挑战或启用了挑战的世界列表。必须在配置中启用。
    - `/[player_command] challenges [challenge] [number]`: 访问 BSkyBlock 玩家挑战 GUI。如果提供了挑战名称,则此方法将完成该挑战一次。如果提供了数字,则它将完成 0-number 次挑战。

=== "管理员命令"
    - `/challengesadmin`: 访问管理员挑战 GUI。包含启用了挑战的世界列表。必须在配置中启用。
    - `/[admin_command] challenges`: 访问 BSkyBlock 管理员挑战 GUI。
    - `/[admin_command] challenges reload [hard]`: 能够重新加载挑战插件配置。此方法还会清除缓存数据。参数 hard 允许重置数据库连接。

## 权限

!!! tip
    `[gamemode]` 是一个根据你运行的游戏模式而不同的前缀。
    前缀是游戏模式的小写名称,即如果你使用 BSkyBlock,前缀就是 `bskyblock`。
    类似地,如果你使用 AcidIsland,前缀就是 `acidisland`。

=== "玩家权限"
    - `[gamemode].challenges` - (默认: `true`) - 允许玩家使用 '/[player_command] challenges' 命令。
    - `[gamemode].challenges.multiple` - (默认: `true`) - 允许玩家一次完成挑战多次。
    - `[gamemode].challenges.complete` - (默认: `false`) - 允许玩家使用 '/[player_command] challenges complete <challenge> <number>' 命令。
    - `addon.challenges` - (默认: `true`) - 如果在配置中启用,允许访问 '/challenges' 命令。
    - `[gamemode].command.challengeexempt` - (默认: `false`) - 允许阻止为玩家执行奖励命令。

=== "管理员权限" 
    - `[gamemode].admin.challenges` - (默认: `op`) - 允许玩家使用 '/[admin_command] challenges' 命令。
    - `[gamemode].admin.challenges.complete` - (默认: `op`) - 允许玩家使用 '/[admin_command] challenges complete' 命令。
    - `[gamemode].admin.challenges.reset` - (默认: `op`) - 允许玩家使用 '/[admin_command] challenges reset' 命令。
    - `addon.admin.challenges` - (默认: `op`) - 如果在配置中启用,允许访问 '/challengesadmin' 命令。

??? question "有缺失的内容吗?"
    你可以在此插件的 [addon.yml](https://github.com/BentoBoxWorld/Challenges/blob/develop/src/main/resources/addon.yml) 文件中找到完整的权限列表。
    如果下面的列表中确实缺少了什么,请告诉我们!

## 占位符

{{ placeholders_source(source="Challenges") }}

## 常见问题

??? question "你能添加 X 功能吗?"
    请将其添加到[这里](https://github.com/BentoBoxWorld/Challenges/issues)的列表中。