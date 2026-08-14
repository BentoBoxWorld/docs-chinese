# AOneBlock 权限

**注意** 这个列表还没有完成。

| 权限                                | 启用对象 | 描述                                       |
|-----------------------------------|------|------------------------------------------|
| aoneblock.count                   | true | 允许使用 aoneblock count 指令                  |
| aoneblock.phases                  | false| 允许使用 phases 指令                        |
| aoneblock.mod.info                | op   | 允许管理员查看玩家信息                            |
| aoneblock.mod.clearreset          | false| 允许清除岛屿重置限制                            |
| aoneblock.mod.bypasscooldowns     | op   | 允许管理员绕过冷却时间                           |
| aoneblock.mod.bypassdelays        | op   | 允许管理员绕过延迟                             |
| aoneblock.mod.bypassprotect       | op   | 允许管理员绕过岛屿保护                           |
| aoneblock.mod.bypassexpel         | op   | 允许管理员绕过岛屿驱逐                           |
| aoneblock.mod.switch              | op   | 允许管理员切换绕过保护                           |
| aoneblock.mod.lock                | op   | 锁定或解锁一个岛屿                             |
| aoneblock.mod.bypasslock          | op   | 绕过岛屿锁定                                 |
| aoneblock.mod.bypassban           | op   | 绕过岛屿禁止                                 |
| aoneblock.mod.team                | false| 通过踢出和添加指令修改团队                        |
| aoneblock.admin.tp                | op   | 允许传送到岛屿                                |
| aoneblock.admin.clearresetall     | op   | 允许清除所有玩家的岛屿重置限制                      |
| aoneblock.admin.reload            | op   | 重新加载 config.yml 文件                    |
| aoneblock.admin.delete            | op   | 允许玩家完全移除一个玩家（包括岛屿）                  |
| aoneblock.admin.register          | op   | 允许玩家为另一个玩家注册最近的岛屿                    |
| aoneblock.admin.unregister        | op   | 移除一个玩家出岛屿但不删除岛屿方块                    |
| aoneblock.admin.setspawn          | op   | 允许使用出生点工具                             |
| aoneblock.admin.setrange          | op   | 允许设置岛屿保护范围                           |
| aoneblock.admin.settingsreset     | op   | 重置所有岛屿为默认保护设置                        |
| aoneblock.admin.noban             | op   | 玩家不能被禁止进入岛屿                          |
| aoneblock.admin.noexpel           | op   | 玩家不能被驱逐出岛屿                          |
| aoneblock.admin.setlanguage       | op   | 重置所有玩家语言并设置默认语言                      |
| aoneblock.admin.getrank           | op   | 获取玩家排名                                 |
| aoneblock.admin.setrank           | op   | 设置玩家排名                                 |
| aoneblock.admin.setchest          | op   | 将看到的箱子放入具有给定稀有度的阶段                 |
| aoneblock.count                   | true | 允许使用 aoneblock count 指令                  |
| aoneblock.island                  | true | 允许岛屿指令的使用                             |
| aoneblock.island.create           | true | 允许创建岛屿                                 |
| aoneblock.island.home             | true | 允许传送到玩家岛屿                             |
| aoneblock.island.number.x         | false| x 设置玩家可以制作的岛屿数量。                     |
| aoneblock.island.sethome          | true | 允许玩家使用 sethome 指令                      |
| aoneblock.island.info             | true | 允许玩家使用 info 指令                         |
| aoneblock.island.lock             | true | 允许

锁定岛屿                                 |
| aoneblock.island.near             | true | 玩家可以看到附近岛屿的名称                         |
| aoneblock.island.expel            | true | 允许驱逐访客                                 |
| aoneblock.island.ban              | true | 允许禁止访客                                 |
| aoneblock.island.settings         | true | 玩家可以查看服务器设置                           |
| aoneblock.island.language         | true | 玩家可以选择语言                               |
| aoneblock.island.name             | true | 玩家可以设置他们岛屿的名称                        |
| aoneblock.island.spawn            | true | 如果存在出生点，玩家可以使用岛屿出生指令              |
| aoneblock.island.reset            | true | 玩家可以使用岛屿重置或重启指令                     |
| aoneblock.island.team             | true | 允许玩家使用团队指令                             |
| aoneblock.island.team.setowner    | true | 允许玩家更改团队所有者                           |
| aoneblock.island.team.invite      | true | 允许玩家邀请他人                               |
| aoneblock.island.team.reject      | true | 允许玩家拒绝邀请                               |
| aoneblock.island.team.leave       | true | 允许玩家离开团队                               |
| aoneblock.island.team.kick        | true | 允许玩家踢出团队成员                             |
| aoneblock.island.team.accept      | true | 允许玩家接受邀请                               |
| aoneblock.island.team.trust       | true | 允许玩家使用团队信任指令                          |
| aoneblock.island.team.coop        | true | 允许玩家使用团队合作指令                          |
| aoneblock.island.team.promote     | true | 允许玩家使用提升指令                             |
| aoneblock.settings.*              | true | 允许在岛屿上使用设置                             |