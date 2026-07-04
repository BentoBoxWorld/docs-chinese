# SkyGrid 权限

| 权限                                  | 启用对象 | 描述                                       |
|-------------------------------------|------|------------------------------------------|
| skygrid.admin.clearresetall         | op   | 允许清除所有玩家的区域重置限制                          |
| skygrid.admin.delete                | op   | 允许玩家完全移除一个玩家（再生区域）                    |
| skygrid.admin.deleteisland          | op   | 允许玩家完全再生玩家所在区域                          |
| skygrid.admin.noban                 | op   | 玩家不能被禁止进入某个区域                           |
| skygrid.admin.register              | op   | 允许玩家将最近的区域注册给另一个玩家                     |
| skygrid.admin.reload                | op   | 重载config.yml文件                            |
| skygrid.admin.reserve               | op   | 为玩家的下一个区域预留一个空位                          |
| skygrid.admin.setlanguage           | op   | 重置所有玩家语言并设置默认语言                         |
| skygrid.admin.setspawn              | op   | 允许使用出生点工具                               |
| skygrid.admin.setrange              | op   | 允许设置区域保护范围                               |
| skygrid.admin.settingsreset         | op   | 将所有区域重置为默认保护设置                           |
| skygrid.admin.unregister            | op   | 从某个区域移除一个玩家，不再生区域方块                     |
| skygrid.mod.bypasscooldowns         | op   | 允许管理员绕过冷却时间                             |
| skygrid.mod.bypassdelays            | op   | 允许管理员绕过延迟                                |
| skygrid.mod.bypassexpel             | op   | 允许管理员绕过区域驱逐                             |
| skygrid.mod.bypasslock              | op   | 绕过区域锁定                                   |
| skygrid.mod.bypassprotect           | op   | 允许管理员绕过区域保护                             |
| skygrid.mod.clearreset              | false| 允许清除区域重置限制                               |
| skygrid.mod.info                    | op   | 允许管理员查看玩家信息                             |
| skygrid.mod.lock                    | op   | 锁定或解锁一个区域                                |
| skygrid.mod.name                    | false| 允许为玩家的区域命名                               |
| skygrid.mod.resethome               | op   | 允许设置或重置玩家的家位置                          |
| skygrid.mod.resetname               | false| 允许重置玩家区域名                                |
| skygrid.mod.team                    | false| 允许通过踢出和添加命令修改团队                       |
| skygrid.mod.tp                      | op   | 允许传送到一个区域                                |
| skygrid.island.ban                  | true | 允许禁止访客                                   |
| skygrid.island.expel                | true | 允许驱逐访客                                   |
| skygrid.island.home                 | true | 允许传送到玩家区域                                |
| skygrid.island.go                   | true | 使用 skygrid go 命令                             |
| skygrid.island.language             | true | 玩家可以选择语言                                 |
| skygrid.island.lock                 | false| 允许区域锁定                                   |
| skygrid.island.name                 | true | 玩家可以设置其区域的名称                            |
| skygrid.island.number               | false| x 设置玩家可以制作的区域数量。                       |
| skygrid.island.reset                | true | 玩家可以使用区域重置或重启命令                         |
| skygrid.island.sethome              | true | 允许玩家使用sethome命令                          |
| skygrid.island.settings             | true | 玩家可以查看设置                                 |
| skygrid.island.spawn                | true | 如果存在出生点，玩家可以使用区域出生命令                  |
| skygrid.island.team                 | true | 允许玩家使用团队命令                               |
| skygrid.island.team.coop            | true | 允许玩家使用团队合作命令                            |
| skygrid.island.team.trust           | true | 允许玩家使用团队信任命令                            |
| skygrid.settings.*                  | true | 允许在区域上使用设置                               |
| skygrid.island                      | true | 使用 **/skygrid** 命令                          |
| skygrid.team.maxsize.[NUMBER]       | false| 允许玩家拥有默认值以上的更大团队尺寸。                  |
| skygrid.island.maxhomes.[NUMBER]    | false| 允许玩家拥有默认值以上的更多家。                      |
| skygrid.island.range.[NUMBER]       | false| 允许玩家拥有默认值以上的更大保护范围。                  |