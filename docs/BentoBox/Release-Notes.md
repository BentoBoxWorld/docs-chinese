# BentoBox 发布说明

服务器管理员最近 BentoBox 版本的亮点。对于每个变化，请参见 [GitHub 发布](https://github.com/BentoBoxWorld/BentoBox/releases)。游戏模式和附属在其页面底部列出他们自己的变化。

!!! note "v3.23.6 新内容 —— 始终允许的实体类型与蓝图加载修复"
    **发布于：** 2026-11-07

    没有 `config.yml` 变化。兼容性：Paper Minecraft 1.21.5 – 26.3，Java 25+。

    - 🔡 **始终允许的实体类型（`ALLOW_MOBS`）。** 每个游戏模式的管理员设置面板中新增一个世界设置（铁锭图标），列出即使关闭了动物或怪物生成也仍会生成的实体类型，在世界和岛屿层面均适用。铁傀儡默认在列表中，因此村庄刷铁机可以继续工作。如果某个类型同时出现在两个列表中，**限制实体类型生成**阻止列表仍然优先。权限：`[gamemode].admin.settings.ALLOW_MOBS`。参见[生物生成优先级](About/Protections.md#mob-spawning-precedence)。
    - 🔺 **"所有蓝图已加载"可能不会触发。** 当多个游戏模式同时加载蓝图时，BentoBox 可能漏掉一次完成通知，从而永远无法进入就绪状态，导致附属的 `allLoaded()` 钩子、需等待就绪的指令以及 `BentoBoxReadyEvent` 都不会运行。此问题已修复，另外还修复了四个相关的主线程/异步竞争问题。
    - 📊 **bStats：** 失败的指令现在会把玩家看到的语言键作为原因上报，并按服务器计数；新的 `worldSize` 图表以区间形式报告岛屿世界在磁盘上的大小。
    - 修复了新的核心世界设置存储在首次运行时误报的 `File not found` 日志。

    🔺 **刷铁机：** 如果之前为了阻止铁傀儡而关闭了动物生成，铁傀儡现在会重新生成。要恢复旧行为，请从"始终允许的实体类型"中移除铁傀儡。

    🔺 **新的数据存储：** 允许列表由 BentoBox 按游戏模式保存，而不是保存在游戏模式的 `config.yml` 中——平面文件数据库为 `plugins/BentoBox/database/CoreWorldSettings/<GameMode>.json`，SQL/Mongo 为 `WorldSettings` 表。

    🔡 **语言文件注意：** 新增了 `protection.flags.ALLOW_MOBS` 下的键（`name`、`description`、`always`、`flags`）。缺少这些键的自定义语言文件会直接显示键名。

    [发布 v3.23.6](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.23.6)

??? note "v3.23.5 新内容 —— 硫磺立方 TNT 保护与 `/island go` 下划线"
    **发布于：** 2026-10-31

    一个 bug 修复版本。没有 `config.yml`、地区或面板模板变化。兼容性：Paper Minecraft 1.21.5 – 26.3，Java 25+。

    - 🔺 **硫磺立方的爆炸现在遵循 TNT 标志。** 吸收了 TNT 的硫磺立方会以自身而非点燃的 TNT 爆炸，因此不会经过 `TNT_DAMAGE` 检查，可能在关闭了 TNT 伤害的岛屿上摧毁建筑。现在其爆炸在岛屿上遵循 `TNT_DAMAGE`，在岛屿外遵循 `WORLD_TNT_DAMAGE`，对方块伤害和实体伤害均适用。玩家用打火石或火焰弹点燃硫磺立方时，会像 TNT 方块一样检查 `TNT_PRIMING`。由红石、发射器或其他爆炸引发的点燃没有对应玩家，因此 `TNT_PRIMING` 无法适用，但爆炸仍遵循 `TNT_DAMAGE`。Minecraft 26.2 之前的服务器没有硫磺立方，因此不受影响。
    - 🐛 **`/island go` 将下划线视为空格。** `/island go happy_place` 现在能找到名为 `Happy Place` 的家园。精确匹配仍然优先，匹配到多个目的地的名称会被拒绝而不是猜测。参见[找到正确的家园](About/IslandManagement.md#homes)。

    **AOneBlock 注意：** AOneBlock 默认设置为 `TNT_DAMAGE: true`，因此除非你将其设为 `false`，否则那里的硫磺立方爆炸仍会造成伤害。

    [发布 v3.23.5](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.23.5)

??? note "v3.23.4 新内容 —— 安全的末地到达与面板中的物品栏使用"
    **发布于：** 2026-10-17

    一个 bug 修复版本。没有 `config.yml`、地区或面板模板变化。兼容性：Paper Minecraft 1.21.5 – 26.3，Java 25+。

    - 🐛 **末地传送门不再把玩家掉进虚空。** 使用 `create-obsidian-platform: false` 时，无论是否有地面，玩家都被直接发送到门户目标。不安全的末地到达现在去最近的安全位置，然后最高的方块，然后是一个小平台。当玩家站在门户内时，重复的门户事件被取消，所以他们不会被发送到原版末地重生点。已经安全的到达仍然会立即传送，启用平台时没有任何变化。安全位置的小平台现在将玩家放在方块的中心。
    - ✨ **当面板打开时使用自己的物品栏。** 玩家可以在 BentoBox 面板（如 `/island settings`）打开时在自己的物品栏中拾起、放置、交换和丢弃物品（Q / Ctrl+Q）并使用包裹。Shift 点击、双击收集和触及面板槽的拖动保持被阻止，所以物品无法进入面板。
    - 🧩 **附属 API：** `PanelListener` 有一个新的默认方法 `allowsPlayerInventoryClicks()`，返回 `false`，所以带有监听器的面板（如 Challenges 和 Biomes 中的图标选择器）表现如前。返回 `true` 来选择加入。见[模板化面板](../Tutorials/api/Templated-Panel.md#listener-method)。`Addon.getConfig()` 现在在附属没有 `config.yml` 时返回空配置而不是 `null`，所以 `saveConfig()` 不再抛出异常。

    [发布 v3.23.4](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.23.4)

??? note "v3.23.3 新内容 —— 黑曜石挖取复制修复与命令等级面板"
    **发布于：** 2026-10-03

    一个 bug 修复和面板发布。没有 `config.yml` 或地区变化。兼容性：Paper Minecraft 1.21.5 – 26.3，Java 25+。

    - 🐛 **黑曜石挖取复制已修复。** 使用 OBSIDIAN_SCOOPING 时，岩浆在点击后一个 tick 被分配而没有重新检查，所以在那个 tick 内挖掘黑曜石会同时给出黑曜石和岩浆，移动桶出手可能给出岩浆而不使用桶。两者现在都先重新检查。**建议每个启用了 OBSIDIAN_SCOOPING 的服务器更新。**
    - ⚙️ **可自定义命令等级面板。** 由新的 `panels/command_ranks_panel.yml`（首次启动时写入；游戏模式自己的副本优先）布局，带有 `COMMAND`、`NEXT` 和 `PREVIOUS` 按钮。现在在 45 个命令处分页——旧面板默默地丢弃了第 49 个之后的每个命令。参见[自定义命令等级面板](Island-Protection,-Flags-&-Ranks.md#customizing-the-command-ranks-panel)。
    - ✨ **设置面板改进。** `/island settings` 在玩家最后选择的基础/高级/专家模式中打开，保护和设置选项卡共享一种模式（管理面板仍在专家模式中打开）。命令等级隐藏玩家无权限的子命令（操作员仍看到一切）。中断生成器图标不再显示原版的生成卵工具提示。
    - 🐛 **Multiverse `auto-load` 被尊重。** 自 3.22.0 以来，Multiverse 钩子在每次 BentoBox 启动时重置 `auto-load: false` 在每个 BentoBox 世界上。现在仅当 BentoBox 首次导入世界时设置；现有的 Multiverse 条目保持配置状态。
    - 🧩 **附属 API：** 管理员 `deaths set|add|remove|reset` 命令触发 `PlayerDeathsChangedEvent`（世界、玩家、操作、数量、旧计数和新计数），所以 Level 可以跟随管理员变化。不为自然死亡触发。

    [发布 v3.23.3](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.23.3)

??? note "v3.23.1 新内容 —— Minecraft 26.3 与模板驱动的设置面板"
    **发布于：** 2026-09-25

    兼容性：Paper Minecraft 1.21.5 – 26.3，Java 25+。

    - 🎮 **Minecraft 26.3"Wilderness Bound"支持。** 新的坐垫受现有标志保护——放置需要 PLACE_BLOCKS，敲击或射击需要 BREAK_BLOCKS，坐下需要 RIDING——稻草床由 BED 保护，所以访客不能再在岛屿的稻草床上睡觉（和用完）。没有新标志。发布时，Paper 26.3 仅作为 alpha 版本提供（在版本 41 上测试）。
    - ⚙️🔡 **可自定义设置面板。** `/island settings` 和 `/admin settings` 由 `panels/settings_panel.yml` 和 `panels/admin_settings_panel.yml` 构建，首次启动时写入。选项卡布局、钉住的标志、面板标题和标志的 lore 顺序可以自定义；默认值看起来完全像旧面板。参见[自定义设置面板](Island-Protection,-Flags-&-Ranks.md#customizing-the-settings-panel)。
    - 🐛 **删除的岛屿不再对玩家计数。** 重置或 `/[admin] delete` 后，岛屿一直在每玩家索引中直到重启，阻止了转移（"玩家已拥有 N 个岛屿"）并混淆了 `/[admin] delete`。
    - 🐛 一个模板按钮的 `fallback:` 记录现在正确呈现。

    🔡 **地区注意。** 一个新键 `panels.settings.title` 单独从选项卡名称设置设置面板标题。缺少它的自定义地区文件回落到捆绑文本。标志 lore 布局（`protection.panel.flag-item.description-layout`）现在可以使用 `[ranks]` 和 `[tooltips]` 占位符，但除非你选择加入否则不变。

    [发布 v3.23.1](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.23.1)

??? note "v3.23.0 新内容 —— console-ready setrank"
    **发布于：** 2026-09-19

    兼容性：Paper Minecraft 1.21.x – 26.2，Java 25+。

    - 🔡 **`/[admin] setrank` 从控制台工作。** 新语法 `/[admin] setrank <player> <rank> [island owner | x,y,z]`，向后兼容。等级可以按关键词、翻译后的名称或编号给予；当玩家拥有一个岛屿且是另一个的成员时选择正确的岛屿；岛屿可以由其中心命名。选项卡完成偏移一，已修复。受影响的玩家被告知其等级已改变——参见上面的[命令表](Commands.md#admin-commands)。
    - 💡 **行为变化：** 没有岛屿论证时，`setrank` 现在作用于玩家是**成员**的岛屿而不是他们自己的，所以它不能再意外降级所有者。设置 `owner` 被拒绝并指向 `setowner`。
    - 🐛 **元数据控制台垃圾邮件已修复。** 玩家和岛屿元数据映射现在是线程安全的。损坏的映射之前在每次玩家移动时抛出 `NoSuchElementException`（通过 Border 看到），直到重启。

    🔡 **地区注意。** `commands.admin.setrank` 获得 `cannot-set-owner`、`already-rank` 和 `admin-changed-rank`；`unknown-rank` 现在接受 `[rank]` 和 `[ranks]`。所有 24 个捆绑地区都已更新；添加新键到任何自定义地区文件。

    [发布 v3.23.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.23.0)

??? note "v3.22.4 新内容"
    **发布于：** 2026-09-06

    一个 bug 修复和性能发布。兼容性：Paper Minecraft 1.21.x – 26.2，Java 25+。

    - 🔡 **`/[admin] info <player>` 显示每个岛屿。** 玩家在世界中的所有岛屿（拥有和团队）都被列出，每个块由岛屿名称主要的块，一个新的可选 `[island name]` 论证仅选择一个——参见上面的[命令表](Commands.md#admin-commands)。名称匹配是宽容的（精确、然后不区分大小写和空格、然后唯一的前缀），多词名称不需要引号，选项卡完成提供玩家的岛屿和家点名称。
    - ⚙️ **岛屿历史帽。** 一个新的 `island.history.max-entries` 选项在 `config.yml` 中限制了每个岛屿保持多少历史（日志）条目；最旧的被首先丢弃。默认**`0`** 意味着无限制，所以现有服务器保持其当前行为。限制可以在旧 `JOINED` 条目被丢弃后低估历史成员占位符。
    - 🐛 **清除不再崩溃。** `/[admin] purge <days> confirm` 在第一个完全收集的岛屿上失败并显示 `IslandEvent may only be triggered synchronously`，并在其数据库行后面留下。岛屿事件现在在异步区域删除后在主线程上触发。
    - 🐛 **子命令标签不再改变。** 输入别名如 `/ob h` 重命名了共享的 `go` 命令为 `h` 在每个人的选项卡完成和帮助中——自 3.22.0 Brigadier 注册以来更加可见。已修复；`home` / `h` 别名不变。
    - 🐛 **玩家头通过服务器解析。** 在线玩家的头来自他们的直播人物资料，其他人都在 Paper 自己的人物资料缓存中查找后再回落到 mc-heads 或 Mojang，所以像 TopBlock 这样的面板在速率限制后显示真实头而不是 Steve。
    - ⚡ 性能：边界检查不再分配，映射扫描使用迭代器，共享的 GSON 实例替换每个呼叫构造。

    🔡 **地区注意。** `commands.admin.info.parameters` 现在读 `<player> [island name]` 并添加了新键 `commands.admin.info.island-name`。所有 24 个捆绑地区都已更新；如果你维护自定义地区文件，添加新键或管理员信息块将显示岛屿名称行的原始键。

    [发布 v3.22.4](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.22.4)

??? note "v3.22.3 新内容 —— bStats 选择退出与 Paper 26.2"
    **发布于：** 2026-08-22

    主要是 bug 修复和 API 发布。兼容性：Paper Minecraft 1.21.5 – 26.2，Java 25+。

    - ⚙️ **bStats 指标选择退出。** `config.yml` 中的一个新 `general.metrics` 选项（默认**`true`**）让你禁用 BentoBox 的匿名、汇总使用统计而不接触 `plugins/bStats/config.yml` 中的全局开关，关闭每个插件的 bStats。将其设为 `false` 并**重启**——收集器在启动时注册，所以 `/bbox reload` 不够。永远不会发送个人数据；参见[隐私与数据收集](Privacy.md)。
    - 🔺 **针对 Paper 26.2 和 Adventure 5 构建。** 附属作者：Adventure 5 密封 `Component`（Mockito 不能再模拟它）并用 `payload()` 替换 `ClickEvent.value()`。已部署在 26.2 服务器上的附属可能在运行时受到影响；针对 BentoBox 3.22.3 重新编译表面任何编译时问题——参见[PR #3067](https://github.com/BentoBoxWorld/BentoBox/pull/3067)完整移除列表。服务器管理员无需做任何事。
    - 🔲 **附属开发者的对话框网格布局。** `DialogBuilder#columns(int)` 在网格而不是默认的两宽列表中布置多动作对话框的按钮，`DialogButton` 获得宽度（1–1024）加上 `withWidth(int)`。现有调用不受影响。
    - 🐛 **玩家头 429 垃圾邮件已修复。** 打开带有玩家头的面板（一个前十名列表，比如）可以用来自 `sessionserver.mojang.com` 的 HTTP 429 错误淹没控制台，因为没有纹理数据的头在每次打开时都被重新解析。无纹理头现在降级为纯头，失败的获取不再清除已经有效的缓存头。
    - 🐛 **YAML 数字加载到声明的字段类型中。** 配置值如 `20`，没有小数点写入，现在正确加载到 `double`、`float` 和 `long` 字段中，而不是抛出 `ClassCastException`。
    - 🐛 **面板中的文字颜色名称。** 管理面板在颜色重构后显示附属名称如 `whiteChallenges`；已修复。
    - 📄 发布了 `.blueprint` 和蓝图包文件格式的 JSON 模式（draft 2020-12）。

    [发布 v3.22.3](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.22.3)

??? note "v3.22.2 新内容"
    **发布于：** 2026-08-10

    3.22.0 之上的 bug 修复补丁——没有新功能、配置键或地区变化；一个直接替换。没有 3.22.1 发布。兼容性：Paper Minecraft 1.21.5 – 26.2，Java 25+。

    - 🔺 🐛 **玩家名称查找解析到正确的帐户。** `/[player_command] team trust <name>` 和 `/[player_command] info <name>` 可能会默默地回答一个数月来没有持有该名称的 UUID：已取代的名称记录从未从数据库中删除，查找取第一个匹配。名称现在不区分大小写匹配，陈旧记录被删除，在线玩家首先检查。**在更新前进行备份**——现有数据库随玩家登入而自我修复（清除每重命名一次，而不是每次加入），不需要手动迁移。
    - 🐛 **基岩玩家可以再次使用面板。** Geyser 将一个点击扩展为同一 tick 中的多个 Java 点击数据包，在 3.22.0 中引入的 `panel.click-cooldown-ms` 检查吞下了重要的——每个点击都得到 `slow-down` 且什么都没发生。同 tick 点击现在被视为一个手势；垃圾邮件保护在一个行动承担点击每 tick 不变。
    - 🐛 **禁用的附属不再留下损坏的命令。** 因缺少依赖而被丢弃的游戏模式（没有 Level 的 ChunkBlock，例如）保持了其已注册的命令，每个子命令抛出 NPE。命令、标志和监听器现在在附属启用失败时都被撤回。
    - 🐛 **从标准地狱返回让你在你自己的岛屿上。** 使用共享地狱和 `create-and-link-portals: false`（AOneBlock 的默认），通过门户返回的玩家被倾倒在坐在 0,0 最近的岛屿上。目标现在回落到岛屿的家点位置。

    [发布 v3.22.2](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.22.2)

??? note "v3.22.0 新内容 —— Brigadier 命令"
    **发布于：** 2026-08-01

    一个命令和可见性发布。兼容性：Paper Minecraft 1.21.5 – 26.2，Java 25+。

    - ⚙️ 🔺 **命令使用 Paper 的 Brigadier API 注册。** 玩家现在看到 BentoBox 子命令和完成**当他们输入时**——`/island t…` 在聊天栏中提供 `team`——而不是客户端直到输入或 TAB 才知道什么。子命令树被广告到 4 的深度；更深的子命令仍然工作，他们只是不被预先广告。别名和 `plugin:label` 形式作为重定向而不是重复树发送。`config.yml` 中的一个新 `general.brigadier-commands` 选项默认**打开**；将其设为 `false` 并 `/bbox reload` 如果另一个插件冲突回落到旧命令映射。如果它不能钩住注册器，BentoBox 也会自动回落。
    - 🔺 **结构搜索在生成没有结构的世界中自动被压制。** 绘图师卷制图师-地图贸易——或末影眼、海豚或宝藏地图——过去运行同步结构搜索永远无法在虚无世界成功，扫描到半径上限并吹过 60 秒监视狗。BentoBox 现在问世界的生成器是否根本放置结构并跳过搜索如果它没有，**无需配置**。AOneBlock 和 BSkyBlock 自动获得这个；SkyGrid、Boxed、CaveBlock 和 AcidIsland 不受影响因为他们确实生成结构。世界级 `structures` 条目 `true` 仍强制启用结构作为转换包含预先存在的世界的逃生舱口。这补充了 3.20.0 中添加的选择加入 `world.disabled-structures` 列表。
    - **`/island settings` 现在打开在世界中。** 远离任何岛屿的玩家，或在他们永远不拥有岛屿的游戏模式中，过去得到"你没有岛屿！"。面板现在使用一个只读的**世界保护**选项卡打开，显示哪些保护标志对世界活跃——这正是什么控制他们他们站立的位置。参见[保护](About/Protections.md#viewing-the-world-rules-off-island)。
    - 🐛 **在关闭期间排队的附属数据不再被丢弃。** 任何附属从 `onDisable()` 保存的东西被排队到已经停止排水的数据库管道，所以它默默地、间歇性地在每次重启时丢失。九个捆绑附属保存禁用——Boxed、AOneBlock、Raft、Challenges、Limits、DragonFights、CheckMeOut、ControlPanel 和 InvSwitcher——且 InvSwitcher 陈旧存储的物品栏然后在加入时重新应用，使其成为回滚而不是只是丢失的写入。关闭写入现在在数据库关闭前排水。
    - 🐛 **BentoBox 命令从 NPC、标志和 GUI 插件再次工作。** Brigadier 注册已经从其他插件调度的 Bukkit 命令映射中取出 BentoBox 命令，所以 NPC 运行 `/oneblock go` 回答服务器的无权限消息和运行什么都没有。命令现在也用命令映射注册。这仅曾经影响 3.22.0 开发版本。
    - 🐛 **`Island.setFlag` 不再丢弃写入。** 设置一个保护等级在从未有过该标志条目的岛屿上——这是每个新创建岛屿——默默地什么都没做。`SETTING` 和 `WORLD_SETTING` 标志不受影响。
    - 🐛 **重复的警告保持受限。** 在两个不同限制消息之间交替的玩家完全绕过了 4 秒通知冷却。每个不同的消息现在独立受限。
    - 🐛 **BlueMap 标记集保持在他们自己的世界中。** 附属的标记集不再出现在服务器上每个其他地图的边栏中，`createMarkerSet()` / `removeMarkerSet()` 在 `/bluemap reload` 期间不再抛出。
    - 🐛 **Multiverse 整理。** BentoBox 世界现在获得 `auto-load: false` 即使 Multiverse 已经知道他们，死种子世界（`<world>/bentobox`）注册消失了。现有陈旧条目仍需 `/mv remove`。
    - 🐛 **缺少依赖而被丢弃的附属的标志被清理。** 其硬依赖缺失的附属已注册其标志和监听器才被丢弃，为永远不存在的世界留下监听器触发。
    - **六个新 bStats 图表**报告附属和游戏模式版本、附属 API 级别、设置改变离开他们的默认，以及如何在哪里命令失败。仅失败种类和稳定权限衍生命令键被提交——永不论证或玩家名称。
    - 🔡 **繁体中文（`zh-TW`）地区**添加，由 @qwe664 贡献。没有现有地区键改变，所以自定义地区文件无需工作。

    [发布 v3.22.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.22.0)

??? note "v3.21.0 新内容 —— 模态对话框"
    **发布于：** 2026-07-22

    一个玩家体验发布。兼容性：Paper Minecraft 1.21.5 – 26.2，Java 25+。

    - ⚙️ 🔡 **用于高摩擦流的模态对话框。** 敏感命令确认、`/island go` 目标选择器、团队邀请和首次加入游戏模式选择器现在可以显示为真实的模态对话框，玩家不能误读或滚过。`config.yml` 中的一个新 `island.dialogs` 部分为每个流——`confirmations`、`go-picker` 和 `team-invites` 默认**打开**、`game-mode-selection` 默认**关闭**因为它是设计上的侵入——持有一个切换。对话框需要 Minecraft 26+ 服务器；在任何旧的每个切换被忽略并使用经典聊天/命令行为，所以没有行动需要那里。
    - **原谅 `/island go` 匹配。** `/island go myisland`、`hom` 或以错误大小写或迷路的双空格输入的名称现在传送玩家到他们意思的地方而不是失败精确匹配并倾倒完整列表。参见[家点位置](About/IslandManagement.md#homes)。
    - 🔡 **地区注意：** 新的对话框键（`general.dialogs.*`，加上确认、`island go` 和团队邀请命令下的对话框和选择器键）被添加到所有 22 个捆绑地区。重新生成或更新任何自定义地区文件。
    - 🔧 **附属开发者**得到与核心相同的 `world.bentobox.bentobox.api.dialogs` API——参见[模态对话框](Developer-Documentation.md#modal-dialogs)。

    [发布 v3.21.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.21.0)

??? note "v3.20.0 新内容 —— 命令建议与核心结构压制"
    **发布于：** 2026-07-11

    生活质量发布。兼容性：Paper Minecraft 1.21.5 – 26.2，Java 25+。升级时不改变任何东西除非你选择加入。

    - 🔡 ⚙️ **"你的意思是"命令建议。** 一个拼错的命令如 `/teams` 或 `/island invit Floris` 现在提供最接近的匹配 BentoBox 命令——可点击，或在 30 秒内接受输入 `yes`/`y`——而不是倾倒帮助文本。建议匹配标签和别名跨每个命令树，权限过滤，并使用玩家站立的游戏模式世界来消除歧义。两个新的切换在 `config.yml` 的 `general.did-you-mean` 下——`unknown-commands` 和 `subcommands`——两个默认**打开**；将要么设为 `false` 并 `/bbox reload` 禁用。
    - ⚙️ 🔺 **核心原版结构压制为每个游戏模式。** 禁用一个原版结构现在是单核心设置而不是每个附属工作。`config.yml` 中的一个新 `world.disabled-structures` 列表（应用于每个 BentoBox overworld/nether/end）停止列出的结构生成**和**在结构搜索中跳过他们——`/locate`、末影眼、探险/宝藏地图、海豚和村民制图师交易——修复长期存在的 `/locate` 主线程冻结和接近生成结构泄漏。键是不区分大小写的分离符（`trial_chambers`、`ancient-city`）。游戏模式可以按结构覆盖列表。**列表默认为空，所以行为不改变直到你选择加入。**
    - 🔌 **Nexo 钩。** BentoBox 现在可以放置和检测 [Nexo](https://nexomc.com/) 自定义块和物品，与其他自定义物品集成并排。
    - 🔌 **Oraxen 块放置。** `OraxenHook.placeBlock` 公开 Oraxen 自定义块放置给附属，匹配其他自定义块钩。
    - 🔡 **地区注意：** 三个新 `general.did-you-mean` 键被添加到所有 22 个捆绑地区，预先存在的缺失键 `commands.admin.team.setowner.specify-island` 被填充在每个非英语文件中。重新生成或更新任何自定义地区文件。

    [发布 v3.20.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.20.0)

??? warning "v3.19.0 新内容 —— 床/锚重生现在被尊重"
    **发布于：** 2026-07-08

    兼容性：Paper Minecraft 1.21.5 – 26.2，Java 25+。

    - 🔡 **新 `FISHING` 保护标志。** 阻止玩家从岛屿外钓到被保护区域（标志检查钓钩的位置）。默认为访客等级，所以在你提高它前没什么改变。
    - 🔺 **床与重生锚重生现在被尊重。** 在岛屿上死亡现在在你的床或充电重生锚重生你，当它在你是成员的岛屿上。由新的 `BED_ANCHOR_RESPAWN` 世界设置控制（**默认启用**）；经济敏感的服务器想要旧的"总是在岛屿家点重生"行为应禁用它。
    - 🐛 **末地退出门户不再把你倾倒在世界重生。** 跳过末地退出门户现在路由你到多游戏模式服务器上的安全岛屿家点。
    - 🐛 **物品框架和绘画在蓝图中存活。** 框架保持面向和内容，绘画恢复他们的艺术品，而不是弹出或面向错误的方式。
    - 🔡 **恢复待删除的岛屿。** 新 `/[admin] undelete`，一个站立 `/[admin] delete`（无玩家论证），和 `/[admin] register` 的确认提示现在可以在区域文件被清除之前拯救软删除的岛屿（参见上面的每游戏模式管理员命令表）。
    - ⚙️ **BlueMap 岛屿层在重新加载中存活。** 所有者引脚和区域框不再在 `/bluemap reload` 后消失。`config.yml` 中的一个新 `bluemap` 部分添加 `island-markers` 和 `island-areas` 切换（两个默认 `true`），镜像 Dynmap 切换，加上标记自定义。
    - ⚙️ **可配置的团队面板按钮图标 + 成员/前景文本。** 团队面板中的 STATUS、RANK-filter 和 INVITE 按钮现在尊重 `team_panel.yml` 中设置的 `icon:`，成员/前景按钮名称和描述现在由地区键驱动。默认重现确切的先前外观。
    - ⚡ **设置 GUI 点击垃圾邮件不再尖峰 MSPT。** 垃圾邮件点击 `/is settings` 从 ~30–40 MSPT 下降到通过就地面板刷新和翻译缓存的可忽略不计。

    [发布 v3.19.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.19.0)

??? warning "v3.18.0 新内容 —— Minecraft 26.2 支持需要 Java 25（服务器）"
    **发布于：** 2026-06-27

    - 🔺 **Minecraft 26.2 支持 + Java 25。** BentoBox 现在在 Minecraft 26.x 线上运行（26.2 在运行时支持）并构建已迁移到 Java 25 工具链。**你的服务器必须运行在 Java 25 能力 Paper 构建用于 26.x 线。** 已构建附属 jars 保持不变工作——仅附属**开发者**重新编译对这个发布需要移动他们自己的构建到 Java 25。兼容性：Paper Minecraft 1.21.5 – 26.2，Java 25+。
    - ⚙️ **Dynmap 岛屿标记 / 区域切换。** `config.yml` 中的一个新 `dynmap` 部分添加 `island-markers`（房子图标在每个岛屿的中心）和 `island-areas`（被保护区域边界框）开关。两个默认 `true`，保留现有行为；将要么设为 `false` 并运行 `/bbox reload` 隐藏在密集岛屿淹没地图的服务器上那些覆盖。
    - **管理员范围奖励管理。** 新 `/[admin] range removebonus` 和 `/[admin] range purgebonus` 命令清除奖励保护范围从一个岛屿或每个岛屿——理想在卸载授予他们的附属后（参见上面的每游戏模式管理员命令表）。
    - 🐛 `/is team setowner` 不再被当他们转移到现有团队成员时的岛屿限制阻止。
    - 🐛 Vault 钩现在在附属启用后重试，修复取决于加载顺序的经济集成。

    [发布 v3.18.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.18.0)

??? note "v3.18.1 新内容"
    **发布于：** 2026-07-01

    维护发布。

    - 🐛 **多行 lore 与名称保持他们的颜色。** GUI 工具提示的第一行之后的文本不再回落到默认紫色——序列化器现在在每行后重新发送活跃的颜色（和装饰），修复整个附属的工具提示。

    [发布 v3.18.1](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.18.1)
