# 命令 { #commands }

BentoBox 及其游戏模式中的每个命令，从 BentoBox 源生成。关于如何使用它们，请参见[管理员指南](About/Teams.md)和[玩家指南](Player-Guide.md)。

## 游戏模式命令如何命名 { #how-game-mode-commands-are-named }

每个游戏模式都有自己的玩家和管理员命令。下面的表格将它们写为 `/[player_command]` 和 `/[admin_command]`。权限以游戏模式的前缀开头，写作 `[gamemode].`：

| 游戏模式 | `[player_command]` | `[admin_command]` | `[gamemode]` |
|---|---|---|---|
| BSkyBlock | `/island`、`/is` | `/bsbadmin`、`/bsb` | `bskyblock` |
| AOneBlock | `/ob`、`/oneblock` | `/oba`、`/obadmin` | `aoneblock` |
| AcidIsland | `/ai` | `/acid` | `acidisland` |
| CaveBlock | `/cave`、`/cb` | `/cbadmin`、`/cba` | `caveblock` |

其他游戏模式在他们自己的页面上列出他们的。所有标签可以在游戏模式的 `config.yml` 中改变。

输入没有子命令的命令运行默认值：对于玩家，`/[player_command]` 创建岛屿或传送回家（参见[岛屿](About/IslandManagement.md#creating-islands)）；`/[admin_command]` 和 `help` 列出玩家可以使用的命令。

附属添加他们自己的子命令到这些，例如 `/island level` 或 `/island challenges`。参见每个[附属的页面](../addons/Bank/index.md)。

## BentoBox 命令 { #bentobox-commands }

`/bentobox` 命令（别名 `/bbox`）管理 BentoBox 本身。

| 命令 | 描述 | 权限 |
|---|---|---|
| `/bentobox about` | 版权和许可信息 | `bentobox.about` |
| `/bentobox version` | BentoBox、附属和服务器版本。当你寻求帮助时包括这个 | `bentobox.version` |
| `/bentobox reload` | 重新加载 BentoBox 和所有附属、设置、地区和菜单模板 | `bentobox.admin.reload` |
| `/bentobox reload locales` | 仅重新加载地区文件 | `bentobox.admin.reload` |
| `/bentobox manage` | 打开管理面板 | `bentobox.admin.manage` |
| `/bentobox catalog` | 打开游戏模式和附属的目录 | `bentobox.admin.catalog` |
| `/bentobox locale` | 检查地区文件中缺失的翻译 | `bentobox.admin.locale` |
| `/bentobox migrate` | 将数据从一种数据库类型移动到另一种。参见[改变数据库](Database-transition.md) | `bentobox.admin.migrate` |
| `/bentobox perms` | 打印每个命令权限及其默认值（仅控制台） | `bentobox.admin.perms` |
| `/bentobox rank [list \| add \| remove] [rank reference] [rank value]` | 列出、添加或移除岛屿等级。参见[团队和等级](About/Teams.md#custom-ranks) | `bentobox.admin.rank` |
| `/bentobox placeholders` | 打开占位符浏览器 | `bentobox.admin.placeholders` |
| `/bentobox dump-placeholders` | 将每个已注册占位符写入 markdown 文件 | `bentobox.admin.dump-placeholders` |

## 玩家命令 { #player-commands }

| 命令 | 描述 | 权限 |
|---|---|---|
| `/[player_command] ban <player>` | 禁止玩家进入你的岛屿 | `[gamemode].island.ban` |
| `/[player_command] banlist` | 列出被禁止的玩家 | `[gamemode].island.ban` |
| `/[player_command] create <blueprint>` | 创建岛屿，使用可选蓝图（需要权限） | `[gamemode].island.create` |
| `/[player_command] deletehome [home name]` | 删除家点位置 | `[gamemode].island.deletehome` |
| `/[player_command] expel <player>` | 从你的岛屿逐出玩家 | `[gamemode].island.expel` |
| `/[player_command] go [home name]` | 传送你到你的岛屿 | `[gamemode].island.home` |
| `/[player_command] homes` | 列出你的家点 | `[gamemode].island.homes` |
| `/[player_command] info <player>` | 显示关于你的岛屿或玩家岛屿的信息 | `[gamemode].island.info` |
| `/[player_command] language [language]` | 选择语言 | `[gamemode].island.language` |
| `/[player_command] lock` | 锁定或解锁你的岛屿 | `[gamemode].island.lock` |
| `/[player_command] near` | 显示你周围邻近岛屿的名称 | `[gamemode].island.near` |
| `/[player_command] renamehome [home name]` | 重命名家点位置 | `[gamemode].island.renamehome` |
| `/[player_command] reset <blueprint>` | 重新开始你的岛屿并移除旧的 | `[gamemode].island.reset` |
| `/[player_command] resetname` | 重置你的岛屿名称 | `[gamemode].island.name` |
| `/[player_command] sethome` | 设置你的家传送点 | `[gamemode].island.sethome` |
| `/[player_command] setname <name>` | 为你的岛屿设置名称 | `[gamemode].island.name` |
| `/[player_command] settings` | 显示岛屿设置 | `[gamemode].island.settings` |
| `/[player_command] spawn` | 传送你到生成点 | `[gamemode].island.spawn` |
| `/[player_command] team` | 管理你的团队 | `[gamemode].island.team` |
| `/[player_command] team accept` | 接受邀请 | `[gamemode].island.team.accept` |
| `/[player_command] team coop <player>` | 在你的岛屿上给玩家合作等级 | `[gamemode].island.team.coop` |
| `/[player_command] team demote <player>` | 将玩家向下移动一个等级（永远不会低于成员） | `[gamemode].island.team.promote` |
| `/[player_command] team invite <player>` | 邀请玩家加入你的岛屿 | `[gamemode].island.team.invite` |
| `/[player_command] team kick <player>` | 从你的岛屿移除成员 | `[gamemode].island.team.kick` |
| `/[player_command] team leave` | 离开你的岛屿 | `[gamemode].island.team.leave` |
| `/[player_command] team promote <player>` | 在你的岛屿上提升玩家一个等级 | `[gamemode].island.team.promote` |
| `/[player_command] team reject` | 拒绝邀请 | `[gamemode].island.team.reject` |
| `/[player_command] team setowner <player>` | 将你的岛屿所有权转移给成员 | `[gamemode].island.team.setowner` |
| `/[player_command] team trust <player>` | 在你的岛屿上给玩家信任等级 | `[gamemode].island.team.trust` |
| `/[player_command] team uncoop <player>` | 从玩家移除合作等级 | `[gamemode].island.team.coop` |
| `/[player_command] team uninvite <player>` | 撤回待处理的团队、信任或合作邀请（BentoBox 3.24.0+） | `[gamemode].island.team.invite` |
| `/[player_command] team untrust <player>` | 从玩家移除信任等级 | `[gamemode].island.team.trust` |
| `/[player_command] unban <player>` | 从你的岛屿解除玩家禁止 | `[gamemode].island.ban` |

## 管理员命令 { #admin-commands }

管理员命令默认为操作员。带有 `mod.` 权限的命令用于不是完整管理员的版主；参见[权限和 VIP 特权](Permissions-Guide.md#staff-permissions)。

| 命令 | 描述 | 权限 |
|---|---|---|
| `/[admin_command] blueprint <load/copy/paste/pos1/pos2/save>` | 操纵蓝图 | `[gamemode].admin.blueprint` |
| `/[admin_command] blueprint copy [air] [biome] [nowater]` | 复制由 pos1 和 pos2 设置的剪贴板和可选的空气、生物群系和水方块 | `[gamemode].admin.blueprint.copy` |
| `/[admin_command] blueprint delete <name>` | 删除蓝图 | `[gamemode].admin.blueprint.delete` |
| `/[admin_command] blueprint list` | 列出可用蓝图 | `[gamemode].admin.blueprint.list` |
| `/[admin_command] blueprint load <name>` | 加载蓝图到剪贴板 | `[gamemode].admin.blueprint.load` |
| `/[admin_command] blueprint origin` | 设置蓝图原点到你的位置 | `[gamemode].admin.blueprint.origin` |
| `/[admin_command] blueprint paste` | 粘贴剪贴板到你的位置 | `[gamemode].admin.blueprint.paste` |
| `/[admin_command] blueprint pos1` | 设置立方体剪贴板的第一个角落 | `[gamemode].admin.blueprint.pos1` |
| `/[admin_command] blueprint pos2` | 设置立方体剪贴板的第二个角落 | `[gamemode].admin.blueprint.pos2` |
| `/[admin_command] blueprint rename <blueprint name> <new name>` | 重命名蓝图 | `[gamemode].admin.blueprint.rename` |
| `/[admin_command] blueprint save <blueprint name>` | 保存复制的剪贴板 | `[gamemode].admin.blueprint.save` |
| `/[admin_command] blueprint sink` | 将此蓝图设置为粘贴时沉到海底 | `[gamemode].admin.blueprint.sink` |
| `/[admin_command] deaths` | 编辑玩家死亡 | `[gamemode].admin.deaths` |
| `/[admin_command] deaths add <player> <deaths>` | 为玩家添加死亡 | `[gamemode].admin.deaths.add` |
| `/[admin_command] deaths remove <player> <deaths>` | 为玩家移除死亡 | `[gamemode].admin.deaths.remove` |
| `/[admin_command] deaths reset <player>` | 重置玩家死亡 | `[gamemode].admin.deaths.reset` |
| `/[admin_command] deaths set <player> <deaths>` | 设置玩家死亡 | `[gamemode].admin.deaths.set` |
| `/[admin_command] delete [player]` | 删除玩家的岛屿，或如果未给出玩家则删除你站着的岛屿 | `[gamemode].admin.delete` |
| `/[admin_command] deletehomes <player>` | 从岛屿删除所有命名的家点 | `[gamemode].mod.deletehomes` |
| `/[admin_command] getrank <player> [island owner]` | 获取玩家在他们的岛屿或所有者的岛屿上的等级 | `[gamemode].admin.getrank` |
| `/[admin_command] info <player> [island name]` | 获取你所在位置或玩家岛屿的信息 | `[gamemode].mod.info` |
| `/[admin_command] maxhomes <number / player> <number> [island name]` | 改变这个岛屿或玩家岛屿上允许的家点数量 | `[gamemode].mod.maxhomes` |
| `/[admin_command] purge [days]` | 删除超过 [days] 天未接触的岛屿的区域文件（释放磁盘） | `[gamemode].admin.purge` |
| `/[admin_command] purge age-regions [days]` | 调试/测试：重写区域文件时间戳以使其成为可清理 | `[gamemode].admin.purge.age-regions` |
| `/[admin_command] purge deleted` | 清理任何已标记为已删除的岛屿的区域文件 | `[gamemode].admin.purge.deleted` |
| `/[admin_command] purge protect` | 切换岛屿清理保护 | `[gamemode].admin.purge.protect` |
| `/[admin_command] purge unowned` | 标记无主岛屿为可删除以便可以被收割 | `[gamemode].admin.purge.unowned` |
| `/[admin_command] range` | 管理员岛屿范围命令 | `[gamemode].admin.range` |
| `/[admin_command] range add <player> <range> [island location]` | 增加岛屿保护范围 | `[gamemode].admin.range.add` |
| `/[admin_command] range display` | 显示/隐藏岛屿范围指示符 | `[gamemode].admin.range.display` |
| `/[admin_command] range purgebonus <id>` | 从每个岛屿移除奖励范围 id（例如移除添加它的附属后） | `[gamemode].admin.range.purgebonus` |
| `/[admin_command] range remove <player> <range> [island location]` | 减少岛屿保护范围 | `[gamemode].admin.range.remove` |
| `/[admin_command] range removebonus <player> [id]` | 从岛屿移除奖励范围（全部，或一个按 id） | `[gamemode].admin.range.removebonus` |
| `/[admin_command] range reset <player>` | 将岛屿保护范围重置为世界默认值 | `[gamemode].admin.range.reset` |
| `/[admin_command] range set <player> <range> [island location]` | 设置岛屿保护范围 | `[gamemode].admin.range.set` |
| `/[admin_command] register <player>` | 将玩家注册到你所在的无主岛屿 | `[gamemode].admin.register` |
| `/[admin_command] reload` | 重新加载 | `[gamemode].admin.reload` |
| `/[admin_command] resetflags [flag]` | 将所有岛屿重置为 config.yml 中的默认标志设置 | `[gamemode].admin.resetflags` |
| `/[admin_command] resethome <player> [island name]` | 将玩家的家重置为默认值 | `[gamemode].mod.resethome` |
| `/[admin_command] resetname` | 重置玩家岛屿名称 | `[gamemode].mod.resetname` |
| `/[admin_command] resets` | 编辑玩家重置值 | `[gamemode].admin.resets` |
| `/[admin_command] resets add <player> <resets>` | 为此玩家添加岛屿重置计数 | `[gamemode].admin.resets.add` |
| `/[admin_command] resets remove <player> <resets>` | 减少玩家的岛屿重置计数 | `[gamemode].admin.resets.remove` |
| `/[admin_command] resets reset <player>` | 将玩家的岛屿重置计数设置为 0 | `[gamemode].admin.resets.remove` |
| `/[admin_command] resets set <player> <resets>` | 设置此玩家重置他的岛屿的次数 | `[gamemode].admin.resets.set` |
| `/[admin_command] setprotectionlocation [x y z coords]` | 设置当前位置或 [x y z] 为岛屿保护区域的中心 | `[gamemode].admin.setprotectionlocation` |
| `/[admin_command] setrank <player> <rank> [island owner \| x,y,z]` | 在他们的团队岛屿上，或在由其所有者或 x,y,z 中心命名的岛屿上提升或降级玩家的等级 | `[gamemode].admin.setrank` |
| `/[admin_command] setspawn` | 将岛屿设置为此游戏模式的生成点 | `[gamemode].admin.setspawn` |
| `/[admin_command] setspawnpoint` | 将当前位置设置为此岛屿的生成点 | `[gamemode].admin.setspawnpoint` |
| `/[admin_command] settings [player]/[world flag]/spawn-island [flag/active/disable] [rank/active/disable]` | 打开设置 GUI 或设置设置 | `[gamemode].admin.settings` |
| `/[admin_command] switch` | 打开/关闭保护绕过 | `[gamemode].mod.switch` |
| `/[admin_command] team` | 管理团队 | `[gamemode].mod.team` |
| `/[admin_command] team add <owner> <player>` | 将玩家添加到所有者的团队 | `[gamemode].mod.team.add` |
| `/[admin_command] team disband <owner>` | 解散所有者的团队 | `[gamemode].mod.team.disband` |
| `/[admin_command] team disbandall` | 从这个世界的每个岛屿从每个成员和副所有者剥夺 | `[gamemode].mod.team.disbandall` |
| `/[admin_command] team kick <team player> [x,y,z]` | 从团队踢出玩家 | `[gamemode].mod.team.kick` |
| `/[admin_command] team maxsize <player> <size>` | 为玩家的岛屿设置最大团队大小（使用 0 重置为世界默认值） | `[gamemode].mod.team.maxsize` |
| `/[admin_command] team setowner <player> [island owner]` | 将岛屿所有权转移给玩家。命名当前岛屿所有者以从控制台运行它 | `[gamemode].mod.team.setowner` |
| `/[admin_command] tp <player> [player's island]` | 传送到玩家的岛屿 | `[gamemode].admin.tp` |
| `/[admin_command] tpend <player> [player's island]` | 传送到玩家在末地的岛屿 | `[gamemode].admin.tp` |
| `/[admin_command] tpnether <player> [player's island]` | 传送到玩家在地狱的岛屿 | `[gamemode].admin.tp` |
| `/[admin_command] tpuser <teleporting player> <island's player> [player's island]` | 将玩家传送到另一个玩家的岛屿 | `[gamemode].admin.tpuser` |
| `/[admin_command] tpuserend <teleporting player> <island's player> [player's island]` | 将玩家传送到末地的另一个玩家的岛屿 | `[gamemode].admin.tpuser` |
| `/[admin_command] tpusernether <teleporting player> <island's player> [player's island]` | 将玩家传送到地狱的另一个玩家的岛屿 | `[gamemode].admin.tpuser` |
| `/[admin_command] undelete` | 从你所在的无主岛屿移除待删除状态 | `[gamemode].admin.undelete` |
| `/[admin_command] unregister <owner> [x,y,z]` | 从岛屿注销所有者，但保留岛屿方块 | `[gamemode].admin.unregister` |
| `/[admin_command] version` | 显示 BentoBox 和附属版本 | `[gamemode].admin.version` |
| `/[admin_command] why <player>` | 切换控制台保护调试报告 | `[gamemode].admin.why` |

`/[admin_command] add`、`disband`、`kick` 和 `setowner` 也可以在没有 `team` 的情况下工作（例如 `/bsbadmin kick <player>`），以与较旧版本兼容。
