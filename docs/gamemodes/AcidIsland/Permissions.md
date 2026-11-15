# AcidIsland 权限 { #acidisland-permissions }

AcidIsland 权限以 `acidisland.` 开头。每个权限 列在 [Permissions reference](../../BentoBox/Permissions.md) with `[gamemode]` in place of `acidisland`。有关 VIP 特权，如更大的团队、岛屿和更多家点，请参见[权限和 VIP 特权](../../BentoBox/Permissions-Guide.md)。

## 玩家命令：默认谁拥有它们 { #player-commands-who-has-them-by-default }

这些默认值来自 AcidIsland 的 `addon.yml`. **所有人** 表示所有玩家 都拥有该权限，除非你取消; **操作员** 表示你需要 通过权限插件授予玩家. 运行 `/bentobox perms` 在控制台查看服务器上的默认值.

| 权限 | 命令 | 默认 |
|---|---|---|
| `acidisland.island` | 玩家命令本身 | 所有人 |
| `acidisland.island.create` | `create` | 所有人 |
| `acidisland.island.home` | `go` | 所有人 |
| `acidisland.island.homes` | `homes` | 所有人 |
| `acidisland.island.sethome` | `sethome` | 所有人 |
| `acidisland.island.deletehome` | `deletehome` | 所有人 |
| `acidisland.island.renamehome` | `renamehome` | 所有人 |
| `acidisland.island.spawn` | `spawn` | 所有人 |
| `acidisland.island.info` | `info` | 所有人 |
| `acidisland.island.near` | `near` | 所有人 |
| `acidisland.island.reset` | `reset` | 所有人 |
| `acidisland.island.name` | `setname`, `resetname` | 所有人 |
| `acidisland.island.language` | `language` | 所有人 |
| `acidisland.island.settings` | `settings` | 所有人 |
| `acidisland.island.lock` | `lock` | 所有人 |
| `acidisland.island.ban` | `ban`, `unban`, `banlist` | 所有人 |
| `acidisland.island.expel` | `expel` | 所有人 |
| `acidisland.island.team` | `team` | 所有人 |
| `acidisland.island.team.invite` | `team invite` | 所有人 |
| `acidisland.island.team.accept` | `team accept` | 所有人 |
| `acidisland.island.team.reject` | `team reject` | 所有人 |
| `acidisland.island.team.leave` | `team leave` | 所有人 |
| `acidisland.island.team.kick` | `team kick` | 所有人 |
| `acidisland.island.team.promote` | `team promote`, `team demote` | 所有人 |
| `acidisland.island.team.setowner` | `team setowner` | 所有人 |
| `acidisland.island.team.trust` | `team trust`, `team untrust` | 所有人 |
| `acidisland.island.team.coop` | `team coop`, `team uncoop` | 所有人 |

管理员和版主权限（`acidisland.admin.*`、`acidisland.mod.*`） 默认为操作员。请参见[工作人员权限](../../BentoBox/Permissions-Guide.md#staff-permissions).
