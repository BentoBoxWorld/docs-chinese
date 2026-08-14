# Level

**Level** 可让你的玩家通过放置方块来提升岛屿等级,竞争最高的岛屿等级!

由 [tastybento](https://github.com/tastybento) 创建和维护。

{{ addon_description("Level") }}

## 安装

1. 将 level 插件 jar 文件放入 BentoBox 插件的 addons 文件夹
2. 重启服务器 
3. 插件将创建一个数据文件夹,里面有一个 config.yml 文件
4. 根据需要编辑 config.yml。该配置文件指定方块的价值(见下文)
5. 如果进行了更改,请重启服务器

## 配置

Level 插件有 3 个通用配置项:

- config.yml 文件包含插件的默认配置。
- blockconfig.yml 文件包含每个方块的价值。
- /panels/ 包含管理玩家 GUI 的文件。

### config.yml

配置文件包含插件的主要功能。

最新的 config.yml 可以在[这里](https://github.com/BentoBoxWorld/Level/blob/develop/src/main/resources/config.yml)找到。

本节定义了插件的许多整体设置。

??? note "disabled-game-modes"
    允许指定 Level 插件不应在哪些游戏模式插件中运行。
    
    Level 将不会与这些游戏模式插件挂钩。

    默认值: `[]`

??? note "log-report-to-console"
    如果从控制台执行指令,则允许查看等级报告。

    默认值: `true`

??? note "concurrent-island-calcs" 
    允许指定一次可以进行多少个岛屿等级计算。

    如果队列中有多个,且你的 CPU 可以处理,你可以并行运行岛屿计算。

    默认值: `1`

??? note "calculation-timeout"
    允许指定等级计算应在多少分钟后停止。

    一般来说,计算只需要几秒钟,所以如果这个值被触发,说明有些不对劲。

    默认值: `5`

??? note "zero-new-island-levels"
    允许指定起始方块是否应包含在岛屿等级中。

    如果为 true,Level 将计算初始岛屿的等级,并将其从任何未来的等级计算中移除。
    如果移除所有起始方块,玩家等级可能会变成负值。
    
    如果为 false,玩家的初始岛屿方块将计入他们的等级。

    默认值: `true`

??? note "login"
    允许设置在玩家登录时计算岛屿等级。

    这会在玩家登录时静默计算他们的岛屿等级。

    默认值: `false`

??? note "nether"
    允许在等级计算中包含下界岛屿。

    警告:在游戏中途启用此选项会让拥有岛屿的玩家的岛屿等级突然提高。新岛屿将被正确归零。

    默认值: `false`

??? note "end"
    允许在等级计算中包含末地岛屿。

    警告:在游戏中途启用此选项会让拥有岛屿的玩家的岛屿等级突然提高。新岛屿将被正确归零。

    默认值: `false`

??? note "include-chests"
    允许在等级计算中包含箱子内容。

    警告:等级计算时间会更长,服务器性能可能受到影响。

    默认值: `false`

??? note "underwater"
    允许指定水下方块倍数。

    如果方块低于海平面,它们可以有更高的价值。例如 2 倍。
    如果有海洋,则可以促进水下开发。该值可以是小数。

    默认值: `1.0`

??? note "levelcost"
    允许指定一个岛屿等级的价值。

    默认值: `100`

    最小值: `1`

??? note "level-calc"
    允许指定等级计算公式。

    * blocks - 所有方块价值的总和,减去任何死亡惩罚
    * level_cost - 在线性方程中,一个等级的价值

    此公式可以包括 +、=、*、/、sqrt、^、sin、cos、tan、log(自然对数)。
    结果将始终四舍五入为长整数。

    例如,另一个非线性选项可以是: `3 * sqrt(blocks / level_cost)`

    默认值: `blocks / level_cost`

??? note "levelwait" 
    允许指定等级请求之间的冷却时间(秒)。

    默认值: `60`

??? note "deathpenalty"
    允许指定死亡惩罚。

    玩家每死一次将损失多少方块价值。
    默认值 100 意味着每死一次,玩家将损失 1 级(如果 levelcost 为 100)。

    设置为零可不使用此功能。

    默认值: `100`

??? note "sumteamdeaths"
    允许对死亡惩罚中的所有队员求和。

    如果为 false,则只计算队长的死亡次数。

    默认值: `false`

??? note "shorthand"
    允许显示较短的岛屿等级数字。

    显示向下取整的大等级值,例如 10,345 -> 10k

    默认值: `false`

### blockconfig.yml

方块配置文件包含方块的价值。

最新的 blockconfig.yml 可以在[这里](https://github.com/BentoBoxWorld/Level/blob/develop/src/main/resources/blockconfig.yml)找到。

本节定义了方块的价值和限制。

!!! tip
    此文件中的值仅支持整数 -> 完整数字。

!!! tip
    正确的材料名称可以在 Spigot 材料页面找到。

    注意:这是最新的 spigot 材料列表: [材料](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html)

??? note "limits"
    本节列出了任何特定方块的限制。
    超过此数量的方块不会被计算。
    此限制适用于所有游戏模式,不是特定于世界的。

    格式: `MATERIAL: NUMBER`

    从 Level 2.28.0 起，这些限制同样适用于**捐献**的方块，玩家无法通过捐献而非放置来突破某种方块的上限赚取积分：

    - 等级计算会按当前限制为每种被捐献的方块封顶。如果管理员在玩家捐献之后调低了某个限制，那么只有不超过新限制的部分才会计入。
    - `/[player_command] donate hand`、`/[player_command] donate inv` 和捐献面板都会预先检查限制，把确认提示裁剪到真正会计入的数量（发生裁剪时会给出一行警告），当玩家提供的东西已全部触及上限时则直接拒绝。
    - 限制查找不区分大小写，因此大小写混用的自定义方块 ID（例如 Oraxen 物品）在各处都会解析到同一个限制。

??? note "blocks"
    本节列出了所有游戏模式(世界)中方块的价值。
    要指定特定世界的价值,请使用下一节。
    任何未列出的方块将具有 0 的价值。空气始终为零。

    格式: `MATERIAL: NUMBER`

    CraftEngine 自定义方块也受支持（需要 BentoBox 3.15.0+）。使用其命名空间 ID 作为键：

    ```yaml
    blocks:
      mynamespace:my_block: 50
      mynamespace:custom_ore: 3
    ```

??? note "worlds" 
    列出在特定世界中具有不同价值的任何方块。
    如果未列出某个方块,将使用 blocks 部分的默认值。
    以世界名称为前缀。如果存在,这些值将应用于相关的下界和末地。

    示例:

    ```
        worlds:
          AcidIsland_world:
            SAND: 0
            SANDSTONE: 0
            ICE: 0
    ```

    在此示例中,AcidIsland 将对所有方块使用与 BSkyBlock 相同的值,除了沙子、沙石和冰。

### 可自定义 GUI

BentoBox 1.17 API 引入了一个允许实现可自定义 GUI 的功能。我们尽量让自定义变得简单,但有些功能需要解释。
你可以在这里找到更多关于 BentoBox 自定义 GUI 如何工作的信息: [自定义 GUI](/en/latest/Tutorials/generic/Customizable-GUI/)

??? question "我如何自定义 GUI?"
    要自定义 Level 插件的 GUI,你需要 2.10.0 版本。这是第一个实现它们的版本。插件将在 `/plugins/bentobox/addons/level` 下创建一个名为 `panels` 的新目录。

    目前你可以自定义 3 个 GUI:

    - 排行榜面板: `top_panel` - 允许查看前 10 名岛屿。
    - 详细方块面板: `detail_panel` - 允许在游戏中查看详细的方块价值列表。 
    - 方块价值面板: `value_panel` - 允许在游戏中查看每个方块的价值。

    每个 GUI 都包含仅由其自身支持的功能。

??? question "`PREVIOUS`|`NEXT` 按钮类型是什么?"
    此按钮在 detail_panel 和 value_panel 中可用。
    PREVIOUS 和 NEXT 按钮类型允许在方块多于 GUI 中的空间时创建自动分页。
    这些类型在 data 下有额外的参数:

    - `indexing` - 指示按钮是否显示页码。

      示例:
      ```yaml
          icon: tipped_arrow[potion_contents={custom_color:11546150}]
          title: level.gui.buttons.previous.name
          description: level.gui.buttons.previous.description
          data:
            type: PREVIOUS
            indexing: true
          action:
            left:
              tooltip: level.gui.tips.click-to-previous
      ```

??? question "`TOP` 按钮类型是什么?"
    此按钮在 top_panel 中可用。它按岛屿等级显示排名前 X 的岛屿。

    `icon` 默认为 `PLAYER_HEAD`,带有正确的玩家皮肤。启用它将使用指定的材料替换它。

    data 字段中的 `index` 允许指定当前位置应显示前 10 名中的哪个位置。

    排行榜面板有 2 个实现的操作,功能需要额外的插件:

    - `warp` - 需要 Warps 插件。仅当玩家岛屿上存在传送标志时才会显示。
    - `visit` - 需要 Visit 插件。仅当玩家岛屿上允许访问时才会显示。

    Fallback 允许在排行榜位置上没有玩家时更改背景图标。

    示例:
    ```yaml
        #icon: PLAYER_HEAD
        title: level.gui.buttons.island.name
        description: level.gui.buttons.island.description
        data:
          type: TOP
          index: 1
        actions:
          warp:
            click-type: LEFT
            tooltip: level.gui.tips.click-to-warp
          visit:
            click-type: RIGHT
            tooltip: level.gui.tips.right-click-to-visit
        fallback:
          icon: LIME_STAINED_GLASS_PANE
          title: level.gui.buttons.island.empty
    ```

??? question "`VIEW` 按钮类型是什么?"
    此按钮在 top_panel 中可用。它显示查看者的岛屿等级。

    `icon` 默认为 `PLAYER_HEAD`,带有正确的玩家皮肤。启用它将使用指定的材料替换它。

    `view` 操作允许查看玩家岛屿的详细菜单。

    示例:
    ```yaml
        #icon: PLAYER_HEAD
        title: level.gui.buttons.island.name
        description: level.gui.buttons.island.description
        data:
          type: VIEW
        actions:
          view:
            click-type: unknown
            tooltip: level.gui.tips.click-to-view
    ```

??? question "`BLOCK` 按钮类型是什么?"
    此按钮在 detail_panel 和 value_panel 中可用。此按钮将给定材料显示为图标。

    示例:
    ```yaml
      #icon: STONE
      title: level.gui.buttons.value.name
      description: level.gui.buttons.value.description
      data:
        type: BLOCK
    ```

## 指令

!!! tip
    `[player_command]` 和 `[admin_command]` 是根据你运行的游戏模式而不同的指令。
    游戏模式的 `config.yml` 文件包含允许你修改这些值的选项。
    例如,在 BSkyBlock 中,默认的 `[player_command]` 是 `island`,默认的 `[admin_command]` 是 `bsbadmin`。

=== "玩家指令"
    - `/[player_command] top`: 访问排行榜面板。需要 `[gamemode].island.top` 权限。
    - `/[player_command] level`: 触发玩家的等级计算。需要 `[gamemode].island.level` 权限。
    - `/[player_command] value [material]`: 允许检查方块价值。需要 `[gamemode].island.value` 权限。
    - `/[player_command] donate`: 打开方块捐献 GUI,将方块价值捐献给岛屿等级。需要 `[gamemode].island.level.donate` 权限。
    - `/[player_command] donate hand [amount]`: 将手持物品捐献指定数量给岛屿等级。
    - `/[player_command] donate inv`: 列出玩家物品栏中每一种可捐献方块及其单价与合计，确认后全部捐献并触发一次等级重算。没有配置价值的物品和非方块物品会留在物品栏中。需要 `[gamemode].island.level.donate` 权限。

    !!! note "说明"
        从 2.28.0 起，三条捐献途径都会遵守 [`blockconfig.yml`](#blockconfigyml) 中设置的方块 `limits`，并且每次重算时都会按当前的方块价值重新计算捐献积分。

=== "管理员指令"
    - `/[admin_command] level <player>`: 触发玩家的等级计算。需要 `[gamemode].admin.level` 权限。
    - `/[admin_command] levelstatus`: 显示有多少岛屿在队列中。需要 `[gamemode].admin.levelstatus` 权限。
    - `/[admin_command] sethandicap <player> <number>`: 允许设置岛屿等级的初始数值。需要 `[gamemode].admin.level.sethandicap` 权限。
    - `/[admin_command] top`: 在聊天中显示前 10 名岛屿。需要 `[gamemode].admin.top` 权限。
    - `/[admin_command] top remove <player>`: 允许从排行榜中移除玩家。需要 `[gamemode].admin.top.remove` 权限。

## 权限

!!! tip
    `[gamemode]` 是一个根据你运行的游戏模式而不同的前缀。
    前缀是游戏模式的小写名称,即如果你使用 BSkyBlock,前缀就是 `bskyblock`。
    类似地,如果你使用 AcidIsland,前缀就是 `acidisland`。

=== "玩家权限"
    - `[gamemode].intopten` - (默认: `true`) - 让玩家出现在前 10 名面板中。
    - `[gamemode].island.level` - (默认: `true`) - 允许玩家使用 `/[player_command] level` 指令。
    - `[gamemode].island.top` - (默认: `true`) - 允许玩家使用 `/[player_command] top` 指令。
    - `[gamemode].island.value` - (默认: `true`) - 允许玩家使用 `/[player_command] value` 指令。
    - `[gamemode].island.level.donate` - (默认: `true`) - 允许玩家使用 `/[player_command] donate` 指令。
    - `[gamemode].island.level.details.blocks` - (默认: `true`) - 允许玩家查看岛屿的详细方块列表。
    - `[gamemode].island.level.details.spawners` - (默认: `false`) - 允许玩家查看岛屿的详细刷怪笼列表。
    - `[gamemode].island.level.details.underwater` - (默认: `false`) - 允许玩家查看岛屿的详细水下方块列表。
    - `[gamemode].island.level.details.above-sea-level` - (默认: `false`) - 允许玩家查看岛屿海平面以上的详细方块列表。

=== "管理员权限"
    - `[gamemode].admin.level` - (默认: `op`) - 允许玩家使用 `/[admin_command] level <player>` 指令。
    - `[gamemode].admin.levelstatus` - (默认: `op`) - 允许玩家使用 `/[admin_command] levelstatus` 指令。
    - `[gamemode].admin.level.sethandicap` - (默认: `op`) - 允许玩家使用 `/[admin_command] sethandicap <player> <number>` 指令。
    - `[gamemode].admin.top` - (默认: `op`) - 允许访问 `/[admin_command] top` 指令。
    - `[gamemode].admin.top.remove` - (默认: `op`) - 允许访问 `/[admin_command] top remove <player>` 指令。

??? question "有缺失的内容吗?"
    你可以在此插件的 [addon.yml](https://github.com/BentoBoxWorld/Level/blob/develop/src/main/resources/addon.yml) 文件中找到完整的权限列表。
    如果下面的列表中确实缺少了什么,请告诉我们!

## 占位符

{{ placeholders_source(source="Level") }}

## 常见问题

??? question "你能添加 X 功能吗?"
    请将其添加到[这里](https://github.com/BentoBoxWorld/Level/issues)的列表中。

??? question "如何让 `level-cost` 在每个等级后增加?"
    `level-cost` 设置是一个固定值，无法按等级逐步增加，因为 BentoBox 通过将单一公式应用于总方块数来计算岛屿等级，而非逐级迭代。

    实现等级成本递增的方式是使用 `level-calc` 公式。例如，若要让每个等级比前一个等级难 50%（即 1 级需要 100 个方块，2 级需要 150 个，3 级需要 225 个，以此类推），公式如下：

    `level-calc: 2.4661 * log(blocks) - (2.4661 * log(level_cost) - 1)`

    其中 `level_cost` 是达到 1 级所需的方块数。

    以下是该进度曲线的图表：

    ![template](https://user-images.githubusercontent.com/4407265/212771452-edc943fe-c861-4ba1-b581-8ec987e52f94.png){: loading=lazy }

    !!! warning
        该公式在 25 级左右开始渐近——达到 26 或 27 级需要极大量的方块，这可能导致大多数玩家最终趋向相同的最高等级。在选择进度曲线时请考虑这一点。

    **推导自定义公式**

    要构建适合特定进度曲线的公式：

    1. 在电子表格（如 Excel 或 Google Sheets）中创建目标等级及其对应方块成本的表格。
    2. 绘制该表格的 X/Y 图表。
    3. 右键单击图表并添加趋势线，选择最适合曲线的近似类型（线性、对数、指数等），然后启用"在图表上显示方程"。
    4. 在生成的方程中，将 `x` 替换为 `blocks`，并将其作为 `level-calc` 的值。

    例如，上述 50% 进度就是通过这种方式推导出来的，结果为：

    `level-calc: 2.4661 * log(blocks) - 10.357`

    ![template](https://user-images.githubusercontent.com/4407265/212773894-6f635ed4-f337-4936-b50f-3b616b6bf041.png){: loading=lazy }
    ![template](https://user-images.githubusercontent.com/4407265/212773929-b51ae6b3-5df3-43ae-b35f-bc6fcb42d78f.png){: loading=lazy }

## 更新日志

??? note "v2.23.0 新内容"
    **发布于:** 2026-02-21

    - **Oraxen/Nexo 自定义方块支持。** Level 现在可以计算 Oraxen 和 Nexo 自定义方块的价值。在 `blockconfig.yml` 中使用 `oraxen:block_id` 或 `nexo:block_id` 格式定义价值。
    - **每方块占位符。** 针对岛屿中跟踪的每种方块类型动态注册占位符(例如 `[gamemode]_island_count_<block>`)。由于这些是基于配置动态生成的,请参考 `blockconfig.yml` 了解你服务器上可用的标识符。

    [发布 v2.23.0](https://github.com/BentoBoxWorld/Level/releases/tag/2.23.0)

??? warning "v2.24.0 新内容 — 需要操作"
    **发布于:** 2026-04-12

    - **方块捐献系统。** 玩家现在可以通过 `/[player_command] donate`（GUI）或 `/[player_command] donate hand [amount]`（快速捐献手中物品）永久捐献方块给岛屿等级。捐献的积分存储在每个岛屿上，并在每次等级重新计算后重新添加。
    - 新的 `ISLAND_BLOCK_DONATION` 保护标志控制谁可以捐献。默认仅所有者；可扩展至成员等级。
    - 排行榜面板中新增 `DONATED` 标签，显示岛屿的捐献历史。
    - 等级公式中新增 `island_members` 变量，用于对较大团队进行调整。
    - 管理员等级报告现在包括捐献方块的详细信息。
    - 所有语言文件已迁移至 MiniMessage 格式。
    - 🆕 添加俄语（`ru.yml`）语言文件。
    - 在并发写入下修复了前十的排序。
    - 悬挂标志、藤蔓和洞穴藤蔓的方块图标现在可以正确呈现。

    🔺 **在重启前删除 `plugins/BentoBox/addons/Level/panels/detail_panel.yml`** 以生成包含新 DONATED 标签模板的文件。升级时不会覆盖该文件。

    🔡 **如果你有自定义设置，请重新生成语言文件** — 旧的 `&` 颜色代码不再有效。

    [发布 v2.24.0](https://github.com/BentoBoxWorld/Level/releases/tag/2.24.0)

??? note "v2.25.0 新内容"
    **发布于：** 2026-04-26

    - **CraftEngine 自定义方块支持。** CraftEngine 方块现在可在岛屿等级计算中被计数。在 `blockconfig.yml` 中使用命名空间 ID 添加（如 `mynamespace:my_block: 50`）。需要 BentoBox 3.15.0+。可通过在 `config.yml` 中设置 `disabled-plugin-hooks: [CraftEngine]` 禁用。
    - **可本地化的 `hand` 关键字。** `/island donate` 和 `/island value` 中的 `hand` 参数现可通过新的 `island.donate.hand.keyword` 语言键翻译。英文 `hand` 始终作为备用被接受。
    - 🔡 所有 16 个非英语语言文件已更新，包含缺失的键。
    - 🔡 乌克兰语语言文件现已完整翻译。

    🔡 **重新生成语言文件**以获取新的 `island.donate.hand.keyword` 键。

    [发布 v2.25.0](https://github.com/BentoBoxWorld/Level/releases/tag/2.25.0)

??? note "v2.26.0 新内容"
    **发布于：** 2026-05-04

    - **可配置捐献面板。** 捐献 GUI 现在通过新的 `panels/donation_panel.yml` 模板完全可配置，与价值面板、详情面板和前十面板一致。管理员可以将面板调整为 1 至 6 行、重新排列四个命名按钮（`INFO`、`CANCEL`、`PREVIEW`、`CONFIRM`）、更换图标，并添加装饰性物品。捐献网格会自动填充非边框、非命名按钮的所有格子。
    - `force-shown: [1,2,3,4]` 控制面板使用的行数（支持 1–6 行）。四个必需按钮按其 `data.type` 放置。如果模板缺失或任一必需按钮不存在，面板将回退到先前硬编码的 4 行布局。
    - 🐛 装饰性模板物品现在会真正显示在物品栏中；自定义 `title:` 现已生效；`force-shown` 现作为列表解析（与其他面板 YAML 一致）。
    - 无 API 破坏、无语言变化、无 `config.yml` 迁移。

    ⚙️ **捐献面板布局。** 首次启动时会生成新的 `panels/donation_panel.yml` — 不修改即保持 2.25.0 的布局，或编辑以自定义。

    [发布 v2.26.0](https://github.com/BentoBoxWorld/Level/releases/tag/2.26.0)

??? warning "v2.27.0 新内容 — 需要操作"
    **发布于:** 2026-05-13

    🔺 **需要 BentoBox 3.16.0 或更高版本。** 此版本将 `addon.yml` 中的 `api-version` 更新至 `3.16.0`，并依赖新的 `CraftEngineHook.getItemId` / `getItemStack` 助手。较旧的 BentoBox 版本将拒绝加载该插件。

    - ⚙️ **仅捐献模式。** `config.yml` 中的新 `donations-only` 选项（默认 `false`）。设置为 `true` 时，每次重新计算时跳过分块扫描，岛屿等级仅从捐献积分计算。在此模式下不会注册 `/island detail`，前十查看器按钮停止打开详细面板。存储的 `initialCount` 在 `/island level` 时被忽略，因此为现有岛屿启用该模式不会推送玩家到极低负等级。
    - 💎 **`/island donate inv` — 捐献物品栏中的所有内容。** 新的可确认 `inv` 子指令：列出玩家物品栏中每种可捐献方块的值和总计，然后在确认时捐献所有内容并运行等级重新计算。没有配置值的物品和非方块物品保留在物品栏中。制表符补完现在为第一个参数建议 `hand` / `inv`，为持有物品的数量建议。
    - 🧱 **跨价值、详情和捐献菜单的自定义方块支持。** Oraxen、Nexo、ItemsAdder 和 CraftEngine 自定义方块不再从 `/level value` 中筛选出或在 `/level detail` 中呈现为无名称的纸张图标。价值面板和详情面板从每个插件的注册表中查找真实的自定义方块 `ItemStack`，以便保留配置的纹理/模型数据和显示名称。`/island value hand` 在持有自定义物品时现在报告配置的值和显示名称。捐献路径（`/island donate hand`、`/island donate inv`、捐献面板）接受自定义方块物品并在自定义 ID 下记录捐献。
    - 🐛 **负进度修复。** 非线性 `level-calc` 公式（例如 `3 * sqrt(blocks / level_cost)`）不再在等级之间低于零。感谢 @msmith-codes！
    - ⚡ **性能。** `tidyUp()` 在计算点边界时不再在主线程上线性遍历多达 1000 万个点 — 前向和后向扫描现在使用二进制搜索（约 23 次迭代而不是数百万次）。

    🔡 **语言文件已更新。** 所有 18 个预装语言文件获得了新的 `island.donate.inv.*` 键（`keyword`、`confirm-header`、`confirm-line`、`confirm-total`）。如果你在 `plugins/BentoBox/addons/Level/locales/` 中有自定义语言文件，请将新的 `donate.inv` 块复制到其中，否则新的 `/island donate inv` 流程将显示原始键。

    [发布 v2.27.0](https://github.com/BentoBoxWorld/Level/releases/tag/2.27.0)

??? warning "v2.28.0 新内容 —— 需要注意"
    **发布于：** 2026-07-28

    兼容性：BentoBox API 3.16.0，Minecraft 1.21.x 和 26.1.x，Java 21。

    - 🔺 **捐献限制在各个环节全面生效。** [`blockconfig.yml`](#blockconfigyml) 中定义的方块限制现在会在所有涉及捐献的地方生效。等级计算按当前限制为每种被捐献的方块封顶；`/island donate hand`、`/island donate inv` 和捐献 GUI 都会预先检查限制 —— 把确认提示裁剪到真正会计入的数量，跳过已经触及上限的材料，并在玩家提供的东西全部触顶时给出明确的“已达捐献限制”提示，而不是一个令人误解的 0 积分确认框。管理员的等级报告也会按当前限制截断捐献条目（标注为 “capped at N”），使其与捐献总数相符。
    - **捐献积分现在跟随当前方块价值。** 每次重算都会用当前的（以及特定世界的）价值，从已保存的捐献方块记录重新计算积分，因此修改 `blockconfig.yml` 中的价值会追溯应用到过去的捐献，而不是沿用陈旧的存储总值。捐献 GUI 中的“当前已捐献”显示的也是等级所使用的同一个实际积分。
    - 限制查找不区分大小写，因此大小写混用的自定义方块 ID（例如 Oraxen 物品）在各处都会解析到同一个限制。
    - 除 Modrinth 外，发布时现在会自动推送到 CurseForge 和 Hangar；支持的版本新增了 Minecraft 26.1.2。

    🔺 **升级后岛屿等级可能会下降。** 在玩家曾经越过方块限制捐献的服务器上，超出的那部分方块现在会被排除在等级计算之外。这是有意为之的修复，但请做好应对玩家提问的准备。

    🔡 **语言文件已更新。** 全部 17 个随包语言文件在 `island.donate` 下新增了三个键（`limit-reached`、`limit-notice`、`limit-reached-all`）。如果你在 `plugins/BentoBox/addons/Level/locales/` 中有自定义的语言文件，请补上这些键，否则限制警告会显示原始键名。

    !!! note "使用开发版的用户请注意"
        本周期的快照版本中出现过的实验性逐区块清零引擎已在发布前移除，**不**包含在 2.28.0 中。使用稳定版的用户不受影响。

    [发布 v2.28.0](https://github.com/BentoBoxWorld/Level/releases/tag/2.28.0)

??? note "v2.28.1 新内容"
    **发布于：** 2026-07-29

    一个错误修复版本，可直接替换 2.28.0，没有语言、配置或面板方面的改动。

    - 🐛 **价值面板的搜索按钮不再堆叠重复的聊天提示。** 每点击一次就会开启一个新的、时长 90 秒的“请输入搜索内容”对话。如果第一个提示没有显示出来 —— 例如被 CMI 之类的聊天管理插件吞掉 —— 玩家就会反复点击按钮，堆积起来的对话随后会以 `Conversation cancelled!` 和 `Please enter a search value` 交替刷屏的形式重放，并且每次都会重新打开 GUI。现在搜索输入会先检查玩家是否已有待处理的对话，若有则只是重复提问，而不会再排入第二个对话。

    [发布 v2.28.1](https://github.com/BentoBoxWorld/Level/releases/tag/2.28.1)

## 翻译

{{ translations("Level") }}

## API

从 Level 2.7.2 和 BentoBox 1.17 开始,其他插件可以直接访问 Level 插件数据。但是,对于不想使用太多依赖项的插件来说,插件请求仍然是一个很好的解决方案。

### Maven 依赖
Level 为其他插件提供了 API。这涵盖了 Level 2.8.1 及更高版本。

!!! note
    将 Level 依赖项添加到你的 Maven POM.xml 中:

    ```xml
        <repositories>
            <repository>
                <id>codemc-repo</id>
                <url>https://repo.codemc.io/repository/maven-public/</url>
            </repository>
        </repositories>
        
        <dependencies>
            <dependency>
                <groupId>world.bentobox</groupId>
                <artifactId>level</artifactId>
                <version>2.8.1</version>
                <scope>provided</scope>
            </dependency>
        </dependencies>
    ```
使用最新的 Level 版本。

然后,一旦你拥有岛屿所在的世界,并确认玩家是该世界中岛屿的所有者,你就可以通过询问 Level 来获得玩家的等级。

Level 的 JavaDoc 可以在[这里](https://ci.codemc.io/job/BentoBoxWorld/job/Level/ws/target/apidocs/index.html)找到。

### 事件

=== "IslandLevelCalculatedEvent"
    !!! summary "描述"
        当玩家等级被计算时触发的事件。

        链接到类: [IslandLevelCalculatedEvent](https://github.com/BentoBoxWorld/Level/blob/develop/src/main/java/world/bentobox/level/events/IslandLevelCalculatedEvent.java)

    !!! question "变量"
        - `Island island` - 岛屿对象。
        - `UUID targetPlayer` - 计算等级的玩家的 ID。
        - `Results results` - 计算出的岛屿结果。
        
    !!! example "代码示例"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onLevelCalculated(IslandLevelCalculatedEvent event) {
            UUID user = event.getTargetPlayer();
            Island island = event.getIsland();
            Results results = event.getResults();
            
            // 来自结果的死亡惩罚。
            int deathHandicap = event.getDeathHandicap();

            // 来自结果的岛屿初始等级。
            long initialLevel = event.getInitialLevel();
            
            // 来自结果的岛屿等级。
            long level = event.getLevel();

            // 这将覆盖岛屿等级为 100。
            event.setLevel(100);
            
            // 达到下一级所需的点数
            long pointsToNextLevel = event.getPointsToNextLevel();

            // 来自结果的报告文本。
            List<String> report = event.getReport();
        }
        ``` 

=== "IslandPreLevelEvent "
    !!! summary "描述"
        在计算玩家等级之前触发的事件。

        链接到类: [IslandPreLevelEvent](https://github.com/BentoBoxWorld/Level/blob/develop/src/main/java/world/bentobox/level/events/IslandPreLevelEvent.java)

    !!! question "变量"
        - `Island island` - 岛屿对象。
        - `UUID targetPlayer` - 计算等级的玩家的 ID。
        
    !!! example "代码示例"
        ```java
        @EventHandler(priority = EventPriority.LOW)
        public void beforeLevelCalculated(IslandPreLevelEvent event) {
            UUID user = event.getTargetPlayer();
            Island island = event.getIsland();
        }
        ```

### 插件请求处理程序

直到 BentoBox 1.17,由于我们用于加载插件的类加载器,我们在访问 BentoBox 环境之外的数据时遇到了问题。
这意味着数据只能从其他插件访问。但是 BentoBox 实现了 PlAddon 功能,这意味着请求处理程序不再是必需的。

有关插件请求处理程序的更多信息可以在[这里](/en/latest/BentoBox/Request-Handler-API---How-plugins-can-get-data-from-addons/)找到。

=== "island-level"
    !!! summary "描述"
        返回给定世界中玩家的岛屿等级。

    !!! question "输入"
        - `world-name`: String - 世界名称。
        - `player`: UUID - 玩家的 UUID。

    !!! success "输出"
        玩家的岛屿等级,如果输入无效或该玩家在此世界中没有岛屿,则为 `0L`。

    !!! failure
        如果未提供 `world-name` 或 `world-name` 不存在或不是游戏模式世界,此处理程序将返回 `0L`。

    !!! example "代码示例"
        ```java
            /**
             * 返回给定世界中玩家的岛屿等级。
             * @param playerUUID 玩家的 UUID,不为 null。
             * @param worldName 岛屿所在的世界(主世界)名称,不为 null。
             * @return 玩家的岛屿等级,如果输入无效或该玩家在此世界中没有岛屿,则为 {@code 0L}。
             */
            public long getIslandLevel(UUID playerUUID, String worldName) {
                return (Long) new AddonRequestBuilder()
                    .addon("Level")
                    .label("island-level")
                    .addMetaData("world-name", worldName)
                    .addMetaData("player", playerUUID)
                    .request();
            }
        ```

=== "top-ten-level"
    !!! summary "描述"
        返回拥有的岛屿位于前 10 名的玩家,映射到他们岛屿的等级。

    !!! question "输入"
        - `world-name`: String - 世界名称。

    !!! success "输出"
        `Map<UUID, Long>`,包含拥有的岛屿位于前 10 名的岛主的 UUID,映射到他们岛屿的等级。

    !!! failure 
        如果未提供 `world-name` 或 `world-name` 不存在或不是游戏模式世界,此处理程序将返回空 map。

    !!! example "代码示例"
        ```java
            /**
             * 返回拥有的岛屿位于前 10 名的玩家,映射到他们岛屿的等级。
             * @param worldName 岛屿所在的世界(主世界)名称,不为 null。
             * @return 一个 Map,包含拥有的岛屿位于前 10 名的岛主的 UUID,映射到他们岛屿的等级,
             *         如果指定的世界不存在或不包含岛屿,则返回一个空 map。
             */
            public Map<UUID, Long> getTopTen(String worldName) {
                return (Map<UUID, Long>) new AddonRequestBuilder()
                    .addon("Level")
                    .label("top-ten-level")
                    .addMetaData("world-name", worldName)
                    .request();
            }
        ```