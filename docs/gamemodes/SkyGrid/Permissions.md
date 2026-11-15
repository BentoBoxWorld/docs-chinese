# SkyGrid 权限 { #skygrid-permissions }

SkyGrid 权限以 `skygrid.` 开头。每个权限 列在 [Permissions reference](../../BentoBox/Permissions.md) with `[gamemode]` in place of `skygrid`。有关 VIP 特权，如更大的团队、岛屿和更多家点，请参见[权限和 VIP 特权](../../BentoBox/Permissions-Guide.md)。

## 玩家命令：默认谁拥有它们 { #player-commands-who-has-them-by-default }

这些默认值来自 SkyGrid 的 `addon.yml`. **所有人** 表示所有玩家 都拥有该权限，除非你取消; **操作员** 表示你需要 通过权限插件授予玩家. 运行 `/bentobox perms` 在控制台查看服务器上的默认值.

| 权限 | 命令 | 默认 |
|---|---|---|
| `skygrid.island` | 玩家命令本身 | 所有人 |
| `skygrid.island.create` | `create` | 所有人 |
| `skygrid.island.home` | `go` | 所有人 |
| `skygrid.island.homes` | `homes` | 所有人 |
| `skygrid.island.sethome` | `sethome` | 所有人 |
| `skygrid.island.deletehome` | `deletehome` | 所有人 |
| `skygrid.island.renamehome` | `renamehome` | 所有人 |
| `skygrid.island.spawn` | `spawn` | 所有人 |
| `skygrid.island.info` | `info` | 所有人 |
| `skygrid.island.near` | `near` | 所有人 |
| `skygrid.island.reset` | `reset` | 所有人 |
| `skygrid.island.name` | `setname`, `resetname` | 所有人 |
| `skygrid.island.language` | `language` | 所有人 |
| `skygrid.island.settings` | `settings` | 所有人 |
| `skygrid.island.lock` | `lock` | Nobody |
| `skygrid.island.ban` | `ban`, `unban`, `banlist` | 所有人 |
| `skygrid.island.expel` | `expel` | 所有人 |
| `skygrid.island.team` | `team` | 所有人 |
| `skygrid.island.team.invite` | `team invite` | 所有人 |
| `skygrid.island.team.accept` | `team accept` | 所有人 |
| `skygrid.island.team.reject` | `team reject` | 所有人 |
| `skygrid.island.team.leave` | `team leave` | 所有人 |
| `skygrid.island.team.kick` | `team kick` | 所有人 |
| `skygrid.island.team.promote` | `team promote`, `team demote` | 所有人 |
| `skygrid.island.team.setowner` | `team setowner` | 所有人 |
| `skygrid.island.team.trust` | `team trust`, `team untrust` | 所有人 |
| `skygrid.island.team.coop` | `team coop`, `team uncoop` | 所有人 |

管理员和版主权限（`skygrid.admin.*`、`skygrid.mod.*`） 默认为操作员。请参见[工作人员权限](../../BentoBox/Permissions-Guide.md#staff-permissions).
