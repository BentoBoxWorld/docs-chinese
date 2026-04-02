# 命令

所有的命令与其他游戏模式（如 BSkyBlock）相同。

# Boxed 管理员命令（别名：/boxadmin）

| 命令 | 描述 | 权限 |
| --- | --- | --- |
| `/boxadmin` | 显示所有 Boxed 命令 | `boxed.island` |
| `/boxadmin add <owner> <player>` | 将玩家添加到所有者的团队 | |
| `/boxadmin biomes` | 主要生物群系插件管理员命令。为玩家打开管理员 GUI | |
| `/boxadmin challenges` | 访问 /boxadmin 挑战管理员命令 | `boxed.admin.challenges` |
| `/boxadmin deaths` | 编辑玩家的死亡次数 | |
| `/boxadmin delete` | 删除玩家的岛屿 | `boxed.admin.delete` |
| `/boxadmin disband <owner>` | 解散所有者的团队 | `boxed.mod.bypassprotect` |
| `/boxadmin getrank <player>` | 获取玩家在其岛屿上的等级 | |
| `/boxadmin info <player>` | 获取你所在位置或玩家岛屿的信息 | `boxed.mod.info` |
| `/boxadmin kick <team player>` | 将玩家从团队中踢出 | `boxed.mod.bypassexpel` |
| `/boxadmin level <player>` | 计算玩家的岛屿等级 | |
| `/boxadmin range` | 管理员岛屿范围命令 | |
| `/boxadmin register <player>` | 注册玩家到你所在的无主岛屿 | `boxed.admin.register` |
| `/boxadmin reload` | 重新加载插件 | `boxed.admin.reload` |
| `/boxadmin reset` | 重置命令管理员设置 | `boxed.admin.settingsreset` |
| `/boxadmin bp` | 操纵蓝图 | |
| `/boxadmin bp copy [air]` | 复制由 pos1 和 pos2 设置的剪贴板，可选包括空气块 | |
| `/boxadmin bp load <bp name>` | 将蓝图加载到剪贴板 | |
| `/boxadmin bp origin` | 将蓝图的原点设置为你的位置 | |
| `/boxadmin bp paste` | 将剪贴板粘贴到你的位置 | |
| `/boxadmin bp pos1` | 设置立方体剪贴板的第一个角落 | |
| `/boxadmin bp pos2` | 设置立方体剪贴板的第二个角落 | |
| `/boxadmin bp save <bp name>` | 保存复制的剪贴板 | |
| `/boxadmin setowner <player>` | 将岛屿所有权转移给玩家 | `boxed.admin.register` |
| `/boxadmin setrank <player> <rank>` | 设置玩家在其岛屿上的等级 | |
| `/boxadmin setspawn` | 设置生成点 | `boxed.admin.setspawn` |
| `/boxadmin top` | 显示前十名列表 | |
| `/boxadmin tp <player>` | 传送到玩家的岛屿 | `boxed.mod.tp` |
| `/boxadmin tpend <player>` | 传送到玩家的岛屿 | `boxed.mod.tp` |
| `/boxadmin tpnether <player>` | 传送到玩家的岛屿 | `boxed.mod.tp` |
| `/boxadmin unregister <owner>` | 注销所有者的岛屿，但保留岛屿方块 | `boxed.admin.unregister` |
| `/boxadmin why <player>` | 切换控制台保护调试报告 | |

# Boxed 岛屿玩家命令（别名：/box 或 /boxed）

| 命令 | 描述 | 权限 |
| --- | --- | --- |
| `/box` | 主玩家命令 | `boxed.island` |
| `/box ban <player>` | 将玩家从你的岛屿中禁止 | `boxed.island.ban` |
| `/box banlist` | 列出被禁止的玩家 | `boxed.island.ban` |
| `/box biomes` | 主要生物群系插件命令，打开生物群系更改 GUI | |
| `/box challenges [Level]` | 让玩家使用 /box challenges 命令 | `boxed.challenges` |
| `/box create` | 创建岛屿 | `boxed.island.create` |
| `/box go` | 传送到你的岛屿 | `boxed.island` |
| `/box info <player>` | 显示关于你的岛屿或玩家岛屿的信息 | `boxed.island.info` |
| `/box language` | 选择语言 | `boxed.island.language` |
| `/box level [player]` | 计算你的岛屿等级或显示 [player] 的等级 | |
| `/box reset` | 重新开始你的岛屿并删除旧岛屿 | `boxed.island.reset` |
| `/box sethome` | 设置你的家传送点 | `boxed.island.sethome` |
| `/box setname <name>` | 为你的岛屿设置名称 | `boxed.island.name` |
| `/box settings` | 显示岛屿设置 | `boxed.island.settings` |
| `/box spawn` | 传送到生成点 | `boxed.island.home` |
| `/box resetname` | 重置你的岛屿名称 | `boxed.mod.resetname` |
| `/box unban <player>` | 从你的岛屿中解除玩家的禁止 | `boxed.island.ban` |
| `/box team` | 管理你的团队 | `boxed.island.team` |
| `/box team accept` | 接受邀请 | `boxed.island.team` |
| `/box team coop <player>` | 让玩家获得你岛屿上的合作等级 | `boxed.island.team.coop` |
| `/box team demote <player>` | 将岛屿上的玩家降级 | `boxed.island.team` |
| `/box team leave` | 离开你的岛屿 | `boxed.island.team` |
| `/box team invite` | 邀请玩家加入你的岛屿 | `boxed.island.team` |
| `/box team kick <player>` | 从你的岛屿中删除成员 | `boxed.island.expel` |
| `/box team promote <player>` | 将岛屿上的玩家升级 | `boxed.island.team` |
| `/box team reject` | 拒绝邀请 | `boxed.island.team` |
| `/box team setowner <player>` | 将你的岛屿所有权转移给成员 | `boxed.island.team` |
| `/box team trust <player>` | 给玩家你岛屿上的信任等级 | `boxed.island.team.trust` |
| `/box top` | 显示前十名 | |
| `/box team uncoop <player>` | 从玩家中移除合作等级 | `boxed.island.team.coop` |
| `/box team untrust <player>` | 从玩家中移除信任等级 | `boxed.island.team.trust` |
| `/box warp <name>` | 传送到玩家的传送点标记 | |
| `/box warps` | 打开传送点面板 | |

## 岛屿设置 (/box settings)

Boxed 的独特设置是确定谁可以通过投掷末影珍珠来移动该方块。默认情况下，只有所有者。图标是堆肥桶。
