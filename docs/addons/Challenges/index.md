# 挑战

**Challenges** 插件允许你的玩家 **完成各种可自定义的挑战并获得奖励**!

由 [BONNe](https://github.com/BONNe) 创建和维护。

{{ addon_description("Challenges") }}

## 安装

1. 将插件 jar 文件放入 BentoBox 插件的 addons 文件夹
2. 重启服务器
3. 运行管理员挑战指令,例如 `/bsbadmin challenges` 来配置插件

## 配置

默认情况下,挑战插件没有任何挑战或等级。首次运行时只有管理员 GUI 可以访问。
管理员可以创建自己的挑战或加载一组默认挑战。默认挑战包含 5 个等级和 57 个挑战。
还有一个网络库,管理员可以在其中下载公共挑战。可以通过点击管理员 GUI 中的网络图标访问它。

### config.yml

配置文件包含插件的主要功能。

最新的 config.yml 可以在[这里](https://github.com/BentoBoxWorld/Challenges/blob/develop/src/main/resources/config.yml)找到。

??? note "gui-settings.undeployed-view-mode"
    未部署的挑战在玩家 GUI 中如何显示。

    - `VISIBLE` —— 始终显示未部署的挑战。
    - `HIDDEN` —— 从不显示未部署的挑战。
    - `TOGGLEABLE` —— 玩家 GUI 中会出现一个按钮，让每位玩家自行决定显示或隐藏未部署的挑战。默认为显示，因此初始表现与 `VISIBLE` 一致。既能为即将推出的挑战造势，又能让玩家把界面整理干净。此模式在 1.8.0 中才真正实现，在此之前它的表现与 `VISIBLE` 相同。

    默认值：`VISIBLE`

??? note "gui-settings.open-anywhere"
    允许玩家不在自己岛屿上时也能打开挑战 GUI。在启用世界保护的情况下，完成挑战仍然需要待在岛屿上。

    默认值：`false`（1.8.0 新增）

??? note "gui-settings.description-color"
    应用于挑战自身描述文本每一行的默认颜色，这样你就不必给每个挑战都加上相同的颜色前缀。使用 MiniMessage 标签，包括十六进制写法（例如 `<white>`、`<#55FFFF>` 或 `<color:#55FFFF>`）；旧式 `&` 代码同样仍然可用。留空表示不设默认颜色。描述文本中自行写明的颜色仍会覆盖此设置。不影响各挑战单独的语言文件覆盖项。

    默认值：`''`（1.8.0 新增）

??? note "gui-settings.reward-text-color"
    应用于挑战自身奖励文本每一行的默认颜色，首次完成和重复完成的奖励文本都包含在内。格式与 `description-color` 相同。留空表示不设默认颜色。

    默认值：`''`（1.8.0 新增）

??? note "include-undeployed"
    未部署的挑战是否计入等级的完成进度。关闭后只有已部署的挑战才计入，因此未部署的挑战不会阻碍某个等级的完成。

    默认值：`true`（自 1.8.0 起随 `config.yml` 一同提供）

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

??? question "什么是团队挑战？"
    自 **1.7.0** 起，任何挑战都可以额外标记为**团队挑战** — 仅对拥有团队的岛屿可用的挑战。团队挑战可以要求可配置百分比的团队在线后才能完成，并支持两种协作模式：

    - **汇总（"共同贡献"）** — 所需的物品或统计数据在在线成员之间求和。消费物品时，成本在贡献者之间公平分配：每个人贡献相等的份额，短缺的人贡献他们拥有的，其余的人弥补差异。
    - **按成员（"共饮盛宴"）** — 每个在场成员都必须贡献自己的份额，所以没有人能白吃饭；配置的金额是团队总数，在在线成员之间分配。

    奖励发放给每个在线成员，完成和冷却时间由整个团队共享，团队统计挑战只计算*在团队中时*获得的进度。团队挑战可以显示为对独行侠灰显以招募提示，或完全隐藏。五个参考挑战 — **全力以赴、共同贡献、协作构建、团结一致**和**共饮盛宴** — 包含在捆绑的 `default.json` 中，管理员挑战编辑器公开了所有新选项的切换。

??? question "可以让奖励变得稀有，或者需要碰运气才能拿到吗？"
    可以。自 **1.8.0** 起，每个挑战都可以设定一个百分比几率，决定完成时是否真的发放奖励，在管理员编辑器中逐个挑战设置。借此你可以做出「拼手气」的挑战，奖励并非必得——非常适合可重复挑战和刷宝式玩法。

??? question "完成挑战可以提升岛屿等级吗？"
    可以。自 **1.8.0** 起，挑战或等级可以通过 [Level 附属](/en/latest/addons/Level/)直接给予岛屿等级分，这样挑战就能真正融入岛屿的成长进程，而不只是发放物品、金钱和经验。在管理员编辑器中与其他奖励类型一并设置即可。

??? question "可以要求玩家处于特定生物群系才能完成挑战吗？"
    对岛屿挑战可以。自 **1.8.0** 起，岛屿挑战新增了**所需生物群系**选项：玩家必须站在所选的其中一个生物群系内才能完成该挑战。生物群系在管理员 GUI 的分页生物群系选择器中挑选——左键点击添加，右键点击清空。生物群系按键名存储，因此数据在不同 Minecraft 版本间都很稳健，无法识别的生物群系则永远不会匹配。

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

## 指令

!!! tip
    `[player_command]` 和 `[admin_command]` 是根据你运行的游戏模式而不同的指令。
    游戏模式的 `config.yml` 文件包含允许你修改这些值的选项。
    例如,在 BSkyBlock 中,默认的 `[player_command]` 是 `island`,默认的 `[admin_command]` 是 `bsbadmin`。

=== "玩家指令"
    - `/challenges`: 访问玩家挑战 GUI。包含当前世界中的挑战或启用了挑战的世界列表。必须在配置中启用。
    - `/[player_command] challenges [challenge] [number]`: 访问 BSkyBlock 玩家挑战 GUI。如果提供了挑战名称,则此方法将完成该挑战一次。如果提供了数字,则它将完成 0-number 次挑战。

=== "管理员指令"
    - `/challengesadmin`: 访问管理员挑战 GUI。包含启用了挑战的世界列表。必须在配置中启用。
    - `/[admin_command] challenges`: 访问 BSkyBlock 管理员挑战 GUI。
    - `/[admin_command] challenges reload [hard]`: 能够重新加载挑战插件配置。此方法还会清除缓存数据。参数 hard 允许重置数据库连接。

## 权限

!!! tip
    `[gamemode]` 是一个根据你运行的游戏模式而不同的前缀。
    前缀是游戏模式的小写名称,即如果你使用 BSkyBlock,前缀就是 `bskyblock`。
    类似地,如果你使用 AcidIsland,前缀就是 `acidisland`。

=== "玩家权限"
    - `[gamemode].challenges` - (默认: `true`) - 允许玩家使用 '/[player_command] challenges' 指令。
    - `[gamemode].challenges.multiple` - (默认: `true`) - 允许玩家一次完成挑战多次。
    - `[gamemode].challenges.complete` - (默认: `false`) - 允许玩家使用 '/[player_command] challenges complete <challenge> <number>' 指令。
    - `addon.challenges` - (默认: `true`) - 如果在配置中启用,允许访问 '/challenges' 指令。
    - `[gamemode].command.challengeexempt` - (默认: `false`) - 允许阻止为玩家执行奖励指令。

=== "管理员权限" 
    - `[gamemode].admin.challenges` - (默认: `op`) - 允许玩家使用 '/[admin_command] challenges' 指令。
    - `[gamemode].admin.challenges.complete` - (默认: `op`) - 允许玩家使用 '/[admin_command] challenges complete' 指令。
    - `[gamemode].admin.challenges.reset` - (默认: `op`) - 允许玩家使用 '/[admin_command] challenges reset' 指令。
    - `addon.admin.challenges` - (默认: `op`) - 如果在配置中启用,允许访问 '/challengesadmin' 指令。

??? question "有缺失的内容吗?"
    你可以在此插件的 [addon.yml](https://github.com/BentoBoxWorld/Challenges/blob/develop/src/main/resources/addon.yml) 文件中找到完整的权限列表。
    如果下面的列表中确实缺少了什么,请告诉我们!

## 占位符

{{ placeholders_source(source="Challenges") }}

## 更新日志

!!! warning "v1.8.0 新内容 —— 可切换的未部署挑战需要更新面板文件"
    **发布于：** 2026-07-26

    兼容性：BentoBox 3.14.0 · Minecraft 1.21.x · Java 21。

    - ✨ **可选的奖励几率。** 每个挑战现在都可以掷一个可配置的百分比几率来决定是否真的发放奖励，因此奖励可以设得稀有，或者让玩家去赌。在管理员编辑器中逐个挑战设置。
    - 💎 **岛屿等级奖励。** 完成挑战或等级可以通过 Level 附属直接提升岛屿等级，让挑战融入岛屿的成长进程，而不只是发放物品、金钱和经验。
    - 🔡 **岛屿挑战的生物群系要求。** 岛屿挑战可以要求玩家站在指定的若干生物群系之一内，生物群系从管理员 GUI 中新增的分页选择器里挑选。生物群系按键名存储，因此无法识别的生物群系永远不会匹配。
    - 🔡 ⚙️ 🔺 **可切换的未部署挑战。** `undeployed-view-mode: TOGGLEABLE` 此前形同虚设，表现与 `VISIBLE` 无异。现在它已完整实现：玩家会得到一个按钮，可自行显示或隐藏未部署的挑战，默认为显示。
    - ⚙️ **默认文本颜色。** 新增 `gui-settings.description-color` 与 `gui-settings.reward-text-color` 两个设置，为挑战描述和奖励文本的每一行应用默认的 MiniMessage 颜色，无需再逐个挑战手动加前缀。文本中自行写明的颜色仍会覆盖默认值。
    - 📊 **完成百分比占位符。** 新增 `[gamemode]_challenges_completed_percent` 和 `[gamemode]_challenges_latest_level_completed_percent` 占位符，可用于计分板、Tab 列表等由占位符驱动的显示。
    - 🔡 ⚙️ **在岛屿之外打开 GUI。** 新增的 `gui-settings.open-anywhere` 选项允许玩家不站在自己岛屿上也能打开挑战 GUI。在启用世界保护的情况下，完成挑战本身仍需身处岛屿之上。
    - 🐛 已锁定的等级不会再在状态仍显示为「已锁定」时就展示「恭喜……」的解锁提示。
    - 🐛 玩家 GUI 现在会遵循挑战各自的 `removeWhenCompleted` 标记，因此带有该标记的一次性挑战在完成后会按预期消失。
    - 🐛 管理员通过管理模式为玩家完成挑战时，现在会执行等级完成检查，因此管理员的代完成也能计入等级的达成。
    - 🐛 启用「忽略元数据」时，药水类需求现在会比较基础药水类型，而不再把药水当成空白物品处理。
    - 🔡 确认提示现在会告诉玩家输入 `confirm` / `cancel`，导入、重置和清空时的确认不再靠猜。
    - ⚙️ `include-undeployed` 设置现已随 `config.yml` 一同提供并附有说明。

    🔺 **可切换的未部署挑战需要更新面板文件。** 新的显示/隐藏按钮位于玩家面板模板（`panels/main_panel.yml`）中。已经拥有该文件的服务器不会看到这个按钮，需要删除该文件让它重新生成，或手动把 `TOGGLE_UNDEPLOYED` 按钮加进去。全新安装会自动获得该按钮。`VISIBLE` 与 `HIDDEN` 模式保持不变。

    ⚙️ **新增配置项** `gui-settings.open-anywhere`、`gui-settings.description-color`、`gui-settings.reward-text-color` 以及顶层的 `include-undeployed` 会以安全的默认值自动加入你的 `config.yml`——行为不会发生变化。

    🔡 **语言文件说明。** 本次新增了若干语言键（奖励几率、生物群系选择器、切换按钮、确认提示等）。如果你维护自定义翻译，请重新生成或合并，以便新文本能够显示出来。

    [发布 v1.8.0](https://github.com/BentoBoxWorld/Challenges/releases/tag/1.8.0)

??? note "v1.7.0 新内容"
    **发布于：** 2026-07-01

    - 🔡 **团队挑战** — 为岛屿团队构建的全新挑战类别。团队挑战仅对拥有团队的玩家出现，可以要求团队的一部分在线，并可以汇总资源或要求每个成员贡献。捆绑的挑战集中包含五个即用示例。详见上面的 *"什么是团队挑战？"* 常见问题。
    - **更清晰的导入错误。** 导入挑战时出现的失败现在会报告给运行导入的管理员，包含详细信息，而不是被默认地写入控制台日志。
    - 🔡 **所有翻译已刷新** — 每个语言文件都与英文源同步，包括新的团队挑战字符串。如果你维护自定义翻译，请对照 `en-US.yml` 重新检查，因为添加了几个新密钥（团队挑战按钮、错误和说明）。

    现有挑战不受影响 — 所有团队行为都是可选的，默认关闭。需要 BentoBox 3.14.0+。

    [发布 v1.7.0](https://github.com/BentoBoxWorld/Challenges/releases/tag/1.7.0)

??? warning "v1.6.0 新内容 — 需要语言文件迁移"
    **发布于:** 2026-04-13

    - 🔡 **所有语言文件迁移至 MiniMessage。** 每个语言文件已从旧版 `&` 颜色代码转换为 MiniMessage 标签。删除 `BentoBox/locales/Challenges/` 并重启以重新生成更新的文件。
    - 新挑战菜单设置（由 @stuffyerface 贡献）。
    - 改进的网络库面板：添加了语言过滤器，说明文字自动换行，下载目录时显示加载指示器，妥善处理格式错误的目录条目。
    - 为挑战和等级说明中的奖励文本应用了自动换行，以获得更清晰的显示。
    - **新增可下载的挑战库**，可通过游戏内网络库访问：
        - **Skyblock** — 具有多个进度路径的现代 Skyblock 挑战（EN、ZH-CN、DE、ES、RU、FR）
        - **AcidIsland** — 从沉船到海军上将的海洋挑战进度（EN、ZH-CN、DE、ES、RU、FR）
        - **Poseidon** — Poseidon 游戏模式的默认挑战（EN、ZH-CN、DE、ES、RU、FR）
    - 需要 BentoBox API 3.12.0+。

    [发布 v1.6.0](https://github.com/BentoBoxWorld/Challenges/releases/tag/1.6.0)

??? note "v1.6.1 新内容"
    **发布于：** 2026-05-26

    - 🐛 **确认对话在被放弃时不再触发 NPE。** 当确认对话被放弃而非回应时(例如在输入 `confirm` 之前多次点击库条目,或让提示超时),网络库以及管理 GUI 中的擦除/删除提示可能会向控制台抛出大量 `NullPointerException`。现在放弃操作会被静默地视为无操作。

    直接替换——无需更改配置或语言文件。

    [发布 v1.6.1](https://github.com/BentoBoxWorld/Challenges/releases/tag/1.6.1)

## 常见问题

??? question "你能添加 X 功能吗?"
    请将其添加到[这里](https://github.com/BentoBoxWorld/Challenges/issues)的列表中。

??? question "我如何添加新挑战?"
    官方的方式是通过管理员 GUI 或模板文件添加挑战。
    请注意,模板文件仅在使用管理员 GUI 中的正确图标("导入模板")后才会导入。GUI 将允许选择要导入到游戏模式中的模板。
    
    但是,也可以选择编辑导出的数据库文件。可以通过以下方式完成：`/[admin_command] challenges` 并单击"导出数据库"按钮。

??? question "我可以按岛屿启用挑战吗?这样所有岛屿成员都有相同的挑战?"
    是的,你可以通过插件配置文件来实现：`store-island-data: true`

??? question "我可以按玩家启用挑战吗?"
    是的,你可以通过插件配置文件来实现：`store-island-data: false`

??? question "奖励指令不起作用。为什么?"
    最可能的原因是奖励指令定义不正确。指令不需要在其前面加上 `/` 符号。
    
    如果你想从玩家的角度调用指令，你需要在指令调用前添加 `[SELF]`，例如 `[SELF] kill` 将导致玩家调用 `/kill` 指令。

    也可能是由权限导致的。`[gamemode].command.challengeexempt` 将防止玩家执行指令。检查玩家是否没有此权限。

??? question "如何在奖励指令中添加占位符?"
    目前，插件不支持在奖励指令中使用占位符。如果有必要，你可以在 GitHub 上请求。
    
    当前在奖励指令中唯一支持的占位符是 `[player]` 它返回完成挑战的玩家的名字。

??? question "我不喜欢挑战描述中元素的顺序。我可以改变它吗?"
    是的,元素的顺序是在插件语言文件中定义的。

    [挑战描述](https://github.com/BentoBoxWorld/Challenges/blob/develop/src/main/resources/locales/en-US.yml#L852-L994)
    [等级描述](https://github.com/BentoBoxWorld/Challenges/blob/develop/src/main/resources/locales/en-US.yml#L995-L1042)

    切换或删除说明的某些部分将改变其中显示元素的顺序。

    ```yaml
        lore: |-
            [description]
            [status]
            [cooldown]
            [requirements]
            [rewards]
    ```

    这些部分中的每一个都由下面的标签生成，你也可以改变它们。例如 [status] 部分是由以下内容生成的：

    ```yaml
    status:
        # 已完成不可重复挑战的状态消息
        completed: "&2&l Completed"
        # 包含无限可重复挑战完成次数的状态消息
        completed-times: "&2 Completed &7&l [number] &r&2 time(-s)"
        # 包含可重复挑战最大可用完成次数的状态消息
        completed-times-of: "&2 Completed &7&l [number] &r&2 out of &7&l [max] &r&2 times"
        # 表示达到可重复挑战最大完成次数的状态消息
        completed-times-reached: "&2&l Completed all &7 [max] &2 times"
    ```

## 翻译

!!! info "挑战的翻译"
    翻译不涵盖挑战。
    每个挑战都有自己的"显示名称"和"描述"，为了保持最终用户的配置过程尽可能简单，这些不会被本地化。
    但是，你可以在我们的[在线挑战库](https://github.com/BentoBoxWorld/weblink/tree/master/challenges/library)上找到或提供各种挑战的翻译。

    你也可以选择通过语言[文件](https://github.com/BentoBoxWorld/Challenges/blob/develop/src/main/resources/locales/en-US.yml#L1248-L1270)翻译部分内容

{{ translations("Challenges") }}

## API

自 Challenges 1.0 和 BentoBox 1.17 以来，其他插件可以直接访问 Challenges 插件数据。但是，插件请求仍然是那些不想使用过多依赖的插件的好解决方案。

### Maven 依赖

Challenges 为其他插件提供了 API。这涵盖 1.1.0 及以后的版本。

!!! note
    将 Challenges 依赖添加到你的 Maven POM.xml：

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
                <artifactId>challenges</artifactId>
                <version>1.1.0</version>
                <scope>provided</scope>
            </dependency>
        </dependencies>
    ```

使用最新的 Challenges 版本。

Challenges 的 JavaDocs 可以在[这里](https://ci.codemc.io/job/BentoBoxWorld/job/Challenges/ws/target/apidocs/index.html)找到。

### 事件

自 BentoBox 1.17 API 以来，实现了解决类加载器问题的功能。想要直接使用事件的插件现在可以这样做。

=== "ChallengeCompletedEvent"
    !!! summary "描述"
        当玩家完成挑战时触发的事件。

        此事件仅提供信息。不能被取消。

        链接到类：[ChallengeCompletedEvent](https://github.com/BentoBoxWorld/Challenges/blob/develop/src/main/java/world/bentobox/challenges/events/ChallengeCompletedEvent.java)


    !!! question "变量"
        - `String challengeId` - 被完成的挑战的 id。
        - `UUID user` - 完成挑战的玩家的 id。
        - `Boolean admin` - 表示挑战是否由管理员完成。
        - `Integer completionCount` - 挑战完成次数。
        
    !!! example "代码示例"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onLevelCompletion(ChallengeCompletedEvent event) {
            UUID user = event.getPlayerUUID();
            String challenge = event.getChallengeID();
            boolean isAdmin = event.isAdmin();
            int count = event.getCompletionCount();
        }
        ``` 

=== "LevelCompletedEvent"
    !!! summary "描述"
        当玩家完成等级时触发的事件。

        此事件仅提供信息。不能被取消。

        链接到类：[LevelCompletedEvent](https://github.com/BentoBoxWorld/Challenges/blob/develop/src/main/java/world/bentobox/challenges/events/LevelCompletedEvent.java)


    !!! question "变量"
        - `String levelId` - 被完成的等级的 id。
        - `UUID user` - 完成等级的玩家的 id。
        - `Boolean admin` - 表示等级是否由管理员完成。
        
    !!! example "代码示例"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onLevelCompletion(LevelCompletedEvent event) {
            UUID user = event.getPlayerUUID();
            String levelId = event.getLevelID();
            boolean isAdmin = event.isAdmin();
        }
        ``` 

=== "ChallengeResetAllEvent"
    !!! summary "描述"
        当玩家的所有挑战被重置时触发的事件。它包括挑战等级数据。

        此事件仅提供信息。不能被取消。

        链接到类：[ChallengeResetAllEvent](https://github.com/BentoBoxWorld/Challenges/blob/develop/src/main/java/world/bentobox/challenges/events/ChallengeResetAllEvent.java)

    !!! question "变量"
        - `String worldName` - 挑战被重置的世界的名称。
        - `UUID playerUUID` - 被针对的玩家的 id。
        - `Boolean admin` - 表示重置是否由管理员完成。
        - `String reason` - 包含重置的原因。

    !!! warning "常量值"
        - `reason` - 如果由玩家完成则设置为"ISLAND_RESET"，如果由管理员完成则设置为"RESET_ALL"。

    !!! example "代码示例"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onLevelCompletion(ChallengeResetAllEvent event) {
            UUID user = event.getPlayerUUID();
            String worldName = event.getWorldName();
            boolean isAdmin = event.isAdmin();
            String reason = event.getReason();
        }
        ``` 

=== "ChallengeResetEvent"
    !!! summary "描述"
        当管理员重置挑战时触发的事件。

        此事件仅提供信息。不能被取消。

        链接到类：[ChallengeResetEvent](https://github.com/BentoBoxWorld/Challenges/blob/develop/src/main/java/world/bentobox/challenges/events/ChallengeResetEvent.java)

    !!! question "变量"
        - `String challengeID` - 被重置的挑战的 id。
        - `UUID playerUUID` - 被针对的玩家的 id。
        - `Boolean admin` - 表示挑战是否由管理员重置。
        - `String reason` - 包含重置的原因。

    !!! warning "常量值"
        - `admin` - 设置为 true。尚未实现非管理员的单个挑战重置。
        - `reason` - 设置为"RESET"。

    !!! example "代码示例"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onLevelCompletion(ChallengeResetEvent event) {
            UUID user = event.getPlayerUUID();
            String challengeId = event.getChallengeID();
            boolean isAdmin = event.isAdmin();
            String reason = event.getReason();
        }
        ```

### 插件请求处理器

在 BentoBox 1.17 之前，由于我们用来加载插件的类加载器，访问 BentoBox 环境之外的数据存在问题。
这意味着数据仅可从其他插件访问。但 BentoBox 实现了 PlAddon 功能，这意味着请求处理器不再必要。

更多关于插件请求处理器的信息可以在[这里](/en/latest/BentoBox/Request-Handler-API---How-plugins-can-get-data-from-addons/)找到

=== "challenge-list"
    !!! summary "描述"
        返回在给定世界中定义的所有挑战的 uniqueIds 列表。

    !!! question "输入"
        - `world-name`: String - 世界的名称。

    !!! success "输出"
        输出是一个 `List<String>` 包含为指定世界定义的挑战的 uniqueIds 列表。

    !!! failure
        如果未提供 `world-name`，或 `world-name` 不存在或不是游戏模式世界，此处理器将返回空列表。

    !!! example "代码示例"
        ```java
        public List<String> getChallenges(String worldName) {
            return (List<String>) new AddonRequestBuilder()
                .addon("Challenges")
                .label("challenge-list")
                .addMetaData("world-name", worldName)
                .request();
        }
        ```

=== "challenge-data"
    !!! summary "描述"
        返回一个 `Map<String, Object>` 包含关于所请求挑战的所有信息。

    !!! question "输入"
        - `challenge-name`: String - 所请求挑战的唯一 ID。

    !!! success "输出"
        输出是一个 `Map<String, Object>` 具有以下键：

        - `uniqueId`: String - 所请求挑战的唯一 ID。
        - `name`: String - 挑战的显示名称。
        - `icon`: ItemStack - 在 GUI 中代表挑战的物品。
        - `levelId`: String - 分配所请求挑战的等级的 uniqueId。
        - `order`: Integer - 给定挑战的顺序号。
        - `deployed`: Boolean - 如果挑战被部署则为 `true`，否则为 `false`。
        - `description`: List&lt;String&gt; - 挑战的描述。
        - `type`: String - 所请求的挑战类型的名称。
        - `repeatable`: Boolean - 如果挑战可重复则为 `true`，否则为 `false`。
        - `maxTimes`: Integer - 所请求挑战的最大完成次数。

    !!! failure
        如果未提供 `challengeId`，或在数据库中找不到 `challengeId`，此处理器将返回空映射。

    !!! example "代码示例"
        ```java
        public Map<String, Object> getChallengeDataMap(String challengeId) {
            return (Map<String, Object>) new AddonRequestBuilder()
                .addon("Challenges")
                .label("challenge-data")
                .addMetaData("challenge-name", challengeId)
                .request();
        }
        ```

=== "level-list"
    !!! summary "描述"
        返回在给定世界中定义的所有等级的 uniqueIds 列表。

    !!! question "输入"
        - `world-name`: String - 世界的名称。

    !!! success "输出"
        输出是一个 `List<String>` 包含为指定世界定义的等级的 uniqueIds 列表。

    !!! failure
        如果未提供 `world-name`，或 `world-name` 不存在或不是游戏模式世界，此处理器将返回空列表。

    !!! example "代码示例"
        ```java
        public List<String> getChallengeLevels(String worldName) {
            return (List<String>) new AddonRequestBuilder()
                .addon("Challenges")
                .label("level-list")
                .addMetaData("world-name", worldName)
                .request();
        }
        ```

=== "level-data"
    !!! summary "描述"
        返回一个 `Map<String, Object>` 包含关于所请求等级的所有信息。

    !!! question "输入"
        - `level-name`: String - 所请求等级的唯一 ID。

    !!! success "输出"
        输出是一个 `Map<String, Object>` 具有以下键：

        - `uniqueId`: String - 所请求等级的唯一 ID。
        - `name`: String - 等级的显示名称。
        - `icon`: ItemStack - 在 GUI 中代表等级的物品。
        - `world`: String - 等级操作的世界名称。
        - `order`: Integer - 给定等级的顺序号。
        - `message`: String - 给定等级的解锁消息。
        - `waiveramount`: Integer - 在解锁前可以保留未完成的挑战数。
        - `challenges`: List&lt;String&gt; - 分配的挑战的 ids 列表。

    !!! failure
        如果未提供 `levelId`，或在数据库中找不到 `levelId`，此处理器将返回空映射。

    !!! example "代码示例"
        ```java
        public Map<String, Object> getChallengeLevelData(String levelId) {
            return (Map<String, Object>) new AddonRequestBuilder()
                .addon("Challenges")
                .label("level-data")
                .addMetaData("level-name", levelId)
                .request();
        }
        ```

=== "completed-challenges"
    !!! summary "描述"
        返回在给定世界中定义的已完成挑战的 uniqueIds 列表，由给定玩家完成。

    !!! question "输入"
        - `player`: UUID - 玩家的 UUID。
        - `world-name`: String - 世界的名称。

    !!! success "输出"
        输出是一个 `Set<String>` 包含玩家为指定世界完成的挑战的 uniqueIds 集合。

    !!! failure
        如果未提供 `world-name`，或 `world-name` 不存在或不是游戏模式世界，此处理器将返回空集合。
        如果未提供 `player` 或 `player` 不存在，此处理器将返回空集合。

    !!! example "代码示例"
        ```java
        public List<String> getCompletedChallenges(UUID playerUUID, String worldName) {
            return (List<String>) new AddonRequestBuilder()
                .addon("Challenges")
                .label("completed-challenges")
                .addMetaData("player", playerUUID)
                .addMetaData("world-name", worldName)
                .request();
        }
        ```