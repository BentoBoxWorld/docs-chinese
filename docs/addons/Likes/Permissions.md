#### LikesAddon 权限（截至1.7.0版本）

| 权限                              | 父权限                         | 默认值        | 描述                                                    |
|---------------------------------|-------------------------------|--------------|---------------------------------------------------------|
| [gamemode].likes                |                               | true         | 允许使用 `/[gamemode_user] likes` 指令                    |
| [gamemode].likes.top            | [gamemode].likes              | true         | 允许使用 `/[gamemode_user] likes top` 指令                |
| [gamemode].likes.view           | [gamemode].likes              | true         | 允许使用 `/[gamemode_user] likes view` 指令               |
| [gamemode].likes.view.others    | [gamemode].likes.view         | op           | 允许使用 `/[gamemode_user] likes view <player>` 指令       |
| [gamemode].likes.bypass-cost    | [gamemode].likes              | op           | 允许绕过点赞和点踩的支付                                  |
| [gamemode].likes.admin          |                               | op           | 允许使用 `/[gamemode_admin] likes` 指令                   |
| [gamemode].likes.admin.settings | [gamemode].likes.admin        | op           | 允许使用 `/[gamemode_admin] likes settings` 指令          |
| [gamemode].likes.icon.X         |                               |              | 允许为玩家设置自定义图标（X是材料）                        |