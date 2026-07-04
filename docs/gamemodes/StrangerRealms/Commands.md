# StrangerRealms 玩家命令（别名：/st）

| 命令 | 描述 | 权限 |
| --- | --- | --- |
| `/strange` | 主命令 | `strangerrealms.island` |
| `/strange claim` | 在世界中声称一块土地 | `strangerrealms.claim` |
| `/strange unclaim` | 放弃声称 | `strangerrealms.unclaim` |
| `/strange ban <player>` | 从您的领域中封禁一个玩家 | `strangerrealms.island.ban` |
| `/strange banlist` | 列出被封禁的玩家 | `strangerrealms.island.ban` |
| `/strange challenges [Level]` | 让玩家使用 /strange challenges 命令。需要 Challenges 附属 | `strangerrealms.challenges` |
| `/strange go [home name]` | 将您传送到您的声称或特定的家名称（如果启用） | `strangerrealms.island.home` |
| `/strange info <player>` | 显示您的声称或玩家声称的相关信息 | `strangerrealms.island.info` |
| `/strange language` | 选择语言 | `strangerrealms.island.language` |
| `/strange near` | 显示您周围相邻领域的名称（如果有） | `strangerrealms.island.near` |
| `/strange homes` | 列出您设置的家 | `strangerrealms.island.homes` |
| `/strange sethome [home name]` | 设置您的家传送点并可选地命名 | `strangerrealms.island.sethome` |
| `/strange deletehome [home name]` | 删除一个家传送点 | `strangerrealms.island.deletehome` |
| `/strange rename [home name]` | 重命名一个家传送点 | `strangerrealms.island.renamehome` |
| `/strange settings` | 显示声称设置 | `strangerrealms.island.settings` |
| `/strange spawn` | 将您传送到世界出生点 | `strangerrealms.island.spawn` |
| `/strange setname` | 设置您的声称名称 | `strangerrealms.island.name` |
| `/strange resetname` | 重置您的声称名称 | `strangerrealms.island.name` |
| `/strange unban <player>` | 从您的声称中解除玩家的禁用 | `strangerrealms.island.ban` |
| `/strange team` | 管理您的团队 | `strangerrealms.island.team` |
| `/strange team accept` | 接受邀请 | `strangerrealms.island.team` |
| `/strange team coop <player>` | 使玩家在您的声称中获得合作者级别 | `strangerrealms.island.team.coop` |
| `/strange team demote <player>` | 将声称上的玩家降级 | `strangerrealms.island.team` |
| `/strange team leave` | 离开团队 | `strangerrealms.island.team` |
| `/strange team invite` | 邀请玩家加入您的声称 | `strangerrealms.island.team` |
| `/strange team kick <player>` | 从您的声称中移除成员 | `strangerrealms.island.expel` |
| `/strange team promote <player>` | 提升声称上的玩家 | `strangerrealms.island.team` |
| `/strange team reject` | 拒绝邀请 | `strangerrealms.island.team` |
| `/strange team setowner <player>` | 将您的声称所有权转让给成员 | `strangerrealms.island.team` |
| `/strange team trust <player>` | 给予玩家在您声称上的受信任级别 | `strangerrealms.island.team.trust` |
| `/strange team uncoop <player>` | 从玩家中移除合作者级别 | `strangerrealms.island.team.coop` |
| `/strange team untrust <player>` | 从玩家中移除受信任的玩家级别 | `strangerrealms.island.team.trust` |
| `/strange warp <name>` | 传送到玩家的传送标记 - 需要 Warp 附属 | `strangerrealms.island.warp` |
| `/strange warps` | 打开传送面板 - 需要 Warp 附属 | `strangerrealms.island.warp` |

# StrangerRealms 管理员命令（别名：/stranger）

| 命令 | 描述 | 权限 |
| --- | --- | --- |
| `/stranger add <owner> <player>` | 将玩家添加到所有者的团队 | `strangerrealms.mod.team` |
| `/stranger challenges` | 访问 /stranger challenges 管理员命令。需要 Challenges 附属。 | `strangerrealms.admin.challenges` |
| `/stranger deaths` | 编辑玩家的死亡次数 | `strangerrealms.admin.deaths` |
| `/stranger disband <owner>` | 解散所有者的团队 | `strangerrealms.mod.team` |
| `/stranger getrank <player>` | 获取玩家在其声称中的等级 | `strangerrealms.admin.getrank` |
| `/stranger info <player>` | 获取您所在位置或玩家声称的信息 | `strangerrealms.mod.info` |
| `/stranger kick <team player>` | 将玩家从团队中踢出 | `strangerrealms.mod.team` |
| `/stranger range` | 管理员领域范围命令 - 临时更改声称的范围 | `strangerrealms.admin.range` |
| `/stranger bp` | 操纵蓝图 - 默认只是在 y = -64 处放置的基岩块 | `strangerrealms.admin.blueprint` |
| `/stranger bp copy [air]` | 复制由 pos1 和 pos2 设置的剪贴板，可选地包括空气块 | `strangerrealms.admin.blueprint` |
| `/stranger bp load <schem name>` | 将蓝图加载到剪贴板 | `strangerrealms.admin.blueprint` |
| `/stranger bp origin` | 将蓝图的原点设置为您的位置 | `strangerrealms.admin.blueprint` |
| `/stranger bp paste` | 将剪贴板粘贴到您的位置 | `strangerrealms.admin.blueprint` |
| `/stranger bp pos1` | 设置长方体剪贴板的第 1 个角 | `strangerrealms.admin.blueprint` |
| `/stranger bp pos2` | 设置长方体剪贴板的第 2 个角 | `strangerrealms.admin.blueprint` |
| `/stranger bp save <blueprint name>` | 保存复制的剪贴板 | `strangerrealms.admin.blueprint` |
| `/stranger bp rename <blueprint name>` | 重命名蓝图 | `strangerrealms.admin.blueprint` |
| `/stranger setowner <player> [claim owner]` | 将声称所有权转让给玩家；命名当前所有者以从控制台运行 | `strangerrealms.mod.team` |
| `/stranger setrank <player> <rank>` | 设置玩家在其声称上的等级 | `strangerrealms.admin.setrank` |
| `/stranger setspawn` | 将世界出生点位置设置到此位置 | `strangerrealms.admin.setspawn` |
| `/stranger tp <player> [claim]` | 传送到玩家的声称 | `strangerrealms.mod.tp` |
| `/stranger tpend <player> [claim]` | 传送到玩家的末地声称 | `strangerrealms.mod.tp` |
| `/stranger tpnether <player> [claim]` | 传送到玩家的下界声称 | `strangerrealms.mod.tp` |
| `/stranger unregister <owner>` | 从领域注销所有者，但保留声称方块 | `strangerrealms.admin.unregister` |
| `/stranger version` | 显示 BentoBox 和附属版本 | `strangerrealms.admin.version` |
| `/stranger why <player>` | 切换控制台保护调试报告 | `strangerrealms.admin.why` |
