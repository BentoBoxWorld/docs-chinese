# SkyGrid 指令

# SkyGrid 管理员指令（别名：/sga）

| 指令 | 描述 | 权限 |
| --- | --- | --- |
| `/sgadmin` | 显示所有 SkyGrid 管理员指令 | `skygrid.admin` |
| `/sgadmin deaths` | 编辑玩家的死亡次数 | `skygrid.admin.deaths` |
| `/sgadmin delete` | 删除玩家并再生其区域 | `skygrid.admin.delete` |
| `/sgadmin getrank <player>` | 获取玩家在其区域上的等级 | `skygrid.admin.getrank` |
| `/sgadmin info <player>` | 获取你所在位置或玩家区域的信息 | `skygrid.mod.info` |
| `/sgadmin kick <player>` | 将玩家从团队中踢出 | `skygrid.mod.team` |
| `/sgadmin range` | 管理员区域范围指令 | `skygrid.admin.setrange` |
| `/sgadmin register <player>` | 将你所在的无主区域注册给玩家 | `skygrid.admin.register` |
| `/sgadmin reload` | 重新加载插件 | `skygrid.admin.reload` |
| `/sgadmin resetflags` | 将所有区域重置为 config.yml 中的默认标志设置 | `skygrid.admin.settingsreset` |
| `/sgadmin bp` | 操纵蓝图 | `skygrid.admin.blueprint` |
| `/sgadmin bp copy [air]` | 复制由 pos1 和 pos2 设置的剪贴板，可选包括空气块 | `skygrid.admin.blueprint` |
| `/sgadmin bp load <bp name>` | 将蓝图加载到剪贴板 | `skygrid.admin.blueprint` |
| `/sgadmin bp origin` | 将蓝图的原点设置为你的位置 | `skygrid.admin.blueprint` |
| `/sgadmin bp paste` | 将剪贴板粘贴到你的位置 | `skygrid.admin.blueprint` |
| `/sgadmin bp pos1` | 设置立方体剪贴板的第一个角落 | `skygrid.admin.blueprint` |
| `/sgadmin bp pos2` | 设置立方体剪贴板的第二个角落 | `skygrid.admin.blueprint` |
| `/sgadmin bp save <bp name>` | 保存复制的剪贴板 | `skygrid.admin.blueprint` |
| `/sgadmin setowner <player> [area owner]` | 将区域所有权转移给该玩家；指定当前所有者即可从控制台运行 | `skygrid.mod.team` |
| `/sgadmin setrank <player> <rank>` | 设置玩家在其区域上的等级 | `skygrid.admin.setrank` |
| `/sgadmin setspawn` | 将某个区域设置为此游戏模式的出生点 | `skygrid.admin.setspawn` |
| `/sgadmin tp <player>` | 传送到玩家的区域 | `skygrid.mod.tp` |
| `/sgadmin tpend <player>` | 传送到玩家的末地区域 | `skygrid.mod.tp` |
| `/sgadmin tpnether <player>` | 传送到玩家的下界区域 | `skygrid.mod.tp` |
| `/sgadmin unregister <owner>` | 注销所有者的区域，但保留区域方块 | `skygrid.admin.unregister` |
| `/sgadmin version` | 显示 BentoBox 和插件的版本 | `skygrid.admin.version` |
| `/sgadmin why <player>` | 切换控制台保护调试报告 | `skygrid.admin.why` |

# SkyGrid 玩家指令（别名：/sg）

| 指令 | 描述 | 权限 |
| --- | --- | --- |
| `/skygrid` | 主要玩家指令 | `skygrid.island` |
| `/skygrid ban <player>` | 将玩家从你的区域中禁止 | `skygrid.island.ban` |
| `/skygrid banlist` | 列出被禁止的玩家 | `skygrid.island.ban` |
| `/skygrid create` | 创建一个新区域 | `skygrid.island.create` |
| `/skygrid expel <player>` | 将玩家从你的区域中驱逐 | `skygrid.island.expel` |
| `/skygrid go` | 传送到你的区域家 | `skygrid.island.home` |
| `/skygrid info <player>` | 显示你的区域或玩家区域的信息 | `skygrid.island.info` |
| `/skygrid language` | 选择语言 | `skygrid.island.language` |
| `/skygrid reset` | 重新开始你的区域并移除旧区域 | `skygrid.island.reset` |
| `/skygrid sethome` | 设置你的家传送点 | `skygrid.island.sethome` |
| `/skygrid setname <name>` | 为你的区域设置一个名称 | `skygrid.island.name` |
| `/skygrid settings` | 显示区域设置 | `skygrid.island.settings` |
| `/skygrid spawn` | 传送到出生点 | `skygrid.island.spawn` |
| `/skygrid resetname` | 重置你的区域名称 | `skygrid.mod.resetname` |
| `/skygrid unban <player>` | 解除对玩家的禁止 | `skygrid.island.ban` |
| `/skygrid team` | 管理你的团队 | `skygrid.island.team` |
| `/skygrid team accept` | 接受邀请 | `skygrid.island.team` |
| `/skygrid team coop <player>` | 使玩家在你的区域上获得合作等级 | `skygrid.island.team.coop` |
| `/skygrid team demote <player>` | 将玩家在你的区域上降低一个等级 | `skygrid.island.team` |
| `/skygrid team invite <player>` | 邀请玩家加入你的区域 | `skygrid.island.team` |
| `/skygrid team kick <player>` | 从你的区域中移除一名成员 | `skygrid.island.team` |
| `/skygrid team leave` | 离开你的区域 | `skygrid.island.team` |
| `/skygrid team promote <player>` | 将玩家在你的区域上提升一个等级 | `skygrid.island.team` |
| `/skygrid team reject` | 拒绝邀请 | `skygrid.island.team` |
| `/skygrid team setowner <player>` | 将你的区域所有权转移给一名成员 | `skygrid.island.team` |
| `/skygrid team trust <player>` | 给予玩家在你的区域上的信任等级 | `skygrid.island.team.trust` |
| `/skygrid team uncoop <player>` | 移除玩家的合作等级 | `skygrid.island.team.coop` |
| `/skygrid team untrust <player>` | 移除玩家的信任等级 | `skygrid.island.team.trust` |
