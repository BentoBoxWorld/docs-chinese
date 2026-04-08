# BSkyBlock 岛屿管理员命令 (别名: /bsb)

| 命令 | 描述 | 权限 |
| --- | --- | --- |
| `/bsbadmin` | 显示所有 BSkyBlock 命令 | `bskyblock.island` |
| `/bsbadmin add <owner> <player>` | 将玩家添加到所有者的团队 | `bskyblock.mod.team` |
| `/bsbadmin biomes` | 主要生物群系插件管理员命令。为玩家打开管理员 GUI | `bskyblock.admin.biomes` |
| `/bsbadmin challenges` | 访问 /bsbadmin 挑战管理员命令 | `bskyblock.admin.challenges` |
| `/bsbadmin deaths` | 编辑玩家的死亡次数 | `bskyblock.admin.deaths` |
| `/bsbadmin delete` | 删除玩家的岛屿 | `bskyblock.admin.delete` |
| `/bsbadmin disband <owner>` | 解散所有者的团队 | `bskyblock.mod.team` |
| `/bsbadmin getrank <player>` | 获取玩家在其岛屿上的等级 | `bskyblock.admin.getrank` |
| `/bsbadmin info <player>` | 获取你所在位置或玩家岛屿的信息 | `bskyblock.mod.info` |
| `/bsbadmin kick <team player>` | 将玩家从团队中踢出 | `bskyblock.mod.team` |
| `/bsbadmin level <player>` | 计算玩家的岛屿等级 - 需要等级插件 | `bskyblock.admin.level` |
| `/bsbadmin range` | 管理员岛屿范围命令 | `bskyblock.admin.range` |
| `/bsbadmin register <player>` | 注册玩家到你所在的无主岛屿 | `bskyblock.admin.register` |
| `/bsbadmin reload` | 重新加载插件 | `bskyblock.admin.reload` |
| `/bsbadmin reset` | 重置命令管理员设置 | `bskyblock.admin.settingsreset` |
| `/bsbadmin bp` | 操纵蓝图 | `bskyblock.admin.blueprint` |
| `/bsbadmin bp copy [air]` | 复制由 pos1 和 pos2 设置的剪贴板，可选包括空气块 | `bskyblock.admin.blueprint` |
| `/bsbadmin bp load <schem name>` | 将蓝图加载到剪贴板 | `bskyblock.admin.blueprint` |
| `/bsbadmin bp origin` | 将蓝图的原点设置为你的位置 | `bskyblock.admin.blueprint` |
| `/bsbadmin bp paste` | 将剪贴板粘贴到你的位置 | `bskyblock.admin.blueprint` |
| `/bsbadmin bp pos1` | 设置立方体剪贴板的第一个角落 | `bskyblock.admin.blueprint` |
| `/bsbadmin bp pos2` | 设置立方体剪贴板的第二个角落 | `bskyblock.admin.blueprint` |
| `/bsbadmin bp save <blueprint name>` | 保存复制的剪贴板 | `bskyblock.admin.blueprint` |
| `/bsbadmin bp rename <blueprint name>` | 重命名蓝图 | `bskyblock.admin.blueprint` |
| `/bsbadmin setowner <player>` | 将岛屿所有权转移给玩家 | `bskyblock.mod.team` |
| `/bsbadmin setrank <player> <rank>` | 设置玩家在其岛屿上的等级 | `bskyblock.admin.setrank` |
| `/bsbadmin setspawn` | 将世界生成位置设置为此位置 | `bskyblock.admin.setspawn` |
| `/bsbadmin top` | 显示前十名列表 - 需要等级插件 | `bskyblock.admin.top` |
| `/bsbadmin tp <player>` | 传送到玩家的岛屿 | `bskyblock.mod.tp` |
| `/bsbadmin tpend <player>` | 传送到玩家的末地岛屿 | `bskyblock.mod.tp` |
| `/bsbadmin tpnether <player>` | 传送到玩家的下界岛屿 | `bskyblock.mod.tp` |
| `/bsbadmin unregister <owner>` | 注销所有者的岛屿，但保留岛屿方块 | `bskyblock.admin.unregister` |
| `/bsbadmin version` | 显示 BentoBox 和插件的版本 | `bskyblock.admin.version` |
| `/bsbadmin why <player>` | 切换控制台保护调试报告 | `bskyblock.admin.why` |

# BSkyBlock 岛屿玩家命令 (别名: /is)

| 命令 | 描述 | 权限 |
| --- | --- | --- |
| `/island` | 主岛屿命令 | `bskyblock.island` |
| `/island about` | 关于此插件 | `bskyblock.island` |
| `/island ban <player>` | 将玩家从你的岛屿中禁止 | `bskyblock.island.ban` |
| `/island banlist` | 列出被禁止的玩家 | `bskyblock.island.ban` |
| `/island biomes` | 主要生物群系插件命令，打开生物群系更改 GUI。需要生物群系插件。 | `bskyblock.admin.biomes` |
| `/island challenges [Level]` | 让玩家使用 /island challenges 命令。需要挑战插件 | `bskyblock.challenges` |
| `/island create <blueprint>` | 使用可选蓝图创建岛屿。（通常不直接由玩家使用） | `bskyblock.island.create` |
| `/island go [home name]` | 传送到你的岛屿或指定的家名称（如果启用） | `bskyblock.island.home` |
| `/island info <player>` | 显示关于你的岛屿或玩家岛屿的信息 | `bskyblock.island.info` |
| `/island language` | 选择语言 | `bskyblock.island.language` |
| `/island level [player]` | 计算你的岛屿等级或显示 [player] 的等级 - 需要等级插件 | `bskyblock.island.level` |
| `/island near` | 显示你周围相邻岛屿的名称（如有） | `bskyblock.island.near` |
| `/island reset` | 重新开始你的岛屿并删除旧岛屿 | `bskyblock.island.reset` |
| `/island homes` | 列出你设置的家 | `bskyblock.island.homes` |
| `/island sethome [home name]` | 设置你的家传送点并可选地命名它 | `bskyblock.island.sethome` |
| `/island deletehome [home name]` | 删除家传送点 | `bskyblock.island.deletehome` |
| `/island rename [home name]` | 重命名家传送点 | `bskyblock.island.renamehome` |
| `/island settings` | 显示岛屿设置 | `bskyblock.island.settings` |
| `/island spawn` | 传送到生成点 | `bskyblock.island.home` |
| `/island setname` | 设置你的岛屿名称 | `bskyblock.mod.setname` |
| `/island resetname` | 重置你的岛屿名称 | `bskyblock.mod.resetname` |
| `/island unban <player>` | 从你的岛屿中解除玩家的禁止 | `bskyblock.island.ban` |
| `/island team` | 管理你的团队 | `bskyblock.island.team` |
| `/island team accept` | 接受邀请 | `bskyblock.island.team` |
| `/island team coop <player>` | 让玩家获得你岛屿上的合作等级 | `bskyblock.island.team.coop` |
| `/island team demote <player>` | 将岛屿上的玩家降级 | `bskyblock.island.team` |
| `/island team leave` | 离开你的岛屿 | `bskyblock.island.team` |
| `/island team invite` | 邀请玩家加入你的岛屿 | `bskyblock.island.team` |
| `/island team kick <player>` | 从你的岛屿中删除成员 | `bskyblock.island.expel` |
| `/island team promote <player>` | 将岛屿上的玩家升级 | `bskyblock.island.team` |
| `/island team reject` | 拒绝邀请 | `bskyblock.island.team` |
| `/island team setowner <player>` | 将你的岛屿所有权转移给成员 | `bskyblock.island.team` |
| `/island team trust <player>` | 给玩家你岛屿上的信任等级 | `bskyblock.island.team.trust` |
| `/island top` | 显示前十名 - 需要等级插件 | `bskyblock.island.level` |
| `/island team uncoop <player>` | 从玩家中移除合作等级 | `bskyblock.island.team.coop` |
| `/island team untrust <player>` | 从玩家中移除信任等级 | `bskyblock.island.team.trust` |
| `/island warp <name>` | 传送到玩家的传送点标记 - 需要传送点插件 | `bskyblock.island.warp` |
| `/island warps` | 打开传送点面板 - 需要传送点插件 | `bskyblock.island.warp` |

## 岛屿设置 (/is settings)

有保护设置、通用设置和 BSkyBlock 岛屿设置可以应用于 BSkyBlock 岛屿。每一项都可以为以下一种或多种玩家类型启用或禁用：访客、合作、信任、成员、副所有者和所有者。下表提供了与每种类型相关的标记，可以通过多次单击来获取所需的一个或所有玩家类型的设置。

| 设置 | 可启用或禁用的标记 |
| --- | --- |
| 保护设置 | 动物骑乘、铁砧、盔甲架、信标、床、破坏方块、繁殖动物、酿造台、桶、按钮、紫颂果、收集熔岩、收集水、投掷鸡蛋、附魔台、末地传送门、末影珍珠、经验获取、火、灭火、鱼类捞取、冰霜行者、熔炉、栅栏门、伤害动物、伤害怪物、伤害村民、掉落物品、拾取物品、唱片机使用、牵引绳使用、拉杆使用、锁定岛屿、挤奶、骑乘库存、名字标签、下界传送门、音符盒、放置方块、压力板、红石物品、剪毛、刷怪蛋、下一页（标记）、TNT 伤害、踩踏农作物、活板门、海龟蛋、使用门、村民交易、工作台、使用容器、使用发射器、使用投掷器、使用漏斗、使用物品框、投掷药水、上一页（标记） |
| 通用设置 | 动物生成、末地 PVP、火焰蔓延、怪物生成、下界 PVP、主世界 PVP |
| BSkyBlock 设置 | 箱子伤害、清洁超平坦、粗泥土耕作、爬行者伤害、爬行者破坏、末地箱子、末影人破坏、进入/退出消息、岛屿重生、离线红石、活塞推动、移除怪物、黑曜石捞取、羽落缓冲传送、命令等级、无敌访客、限制怪物到岛屿 |
