# StrangerRealms 权限 { #strangerrealms-permissions }

StrangerRealms 权限以 `strangerrealms.` 开头。每个权限 列在 [Permissions reference](../../BentoBox/Permissions.md) with `[gamemode]` in place of `strangerrealms`。有关 VIP 特权，如更大的团队、岛屿和更多家点，请参见[权限和 VIP 特权](../../BentoBox/Permissions-Guide.md)。

## 玩家命令：默认谁拥有它们 { #player-commands-who-has-them-by-default }

这些默认值来自 StrangerRealms 的 `addon.yml`. **所有人** 表示所有玩家 都拥有该权限，除非你取消; **操作员** 表示你需要 通过权限插件授予玩家. 运行 `/bentobox perms` 在控制台查看服务器上的默认值.

| 权限 | 命令 | 默认 |
|---|---|---|
| `strangerrealms.island` | 玩家命令本身 | 所有人 |
| `strangerrealms.island.create` | `create` | 操作员（未声明） |
| `strangerrealms.island.home` | `go` | 所有人 |
| `strangerrealms.island.homes` | `homes` | 所有人 |
| `strangerrealms.island.sethome` | `sethome` | 所有人 |
| `strangerrealms.island.deletehome` | `deletehome` | 所有人 |
| `strangerrealms.island.renamehome` | `renamehome` | 所有人 |
| `strangerrealms.island.info` | `info` | 所有人 |
| `strangerrealms.island.near` | `near` | 所有人 |
| `strangerrealms.island.reset` | `reset` | Nobody |
| `strangerrealms.island.name` | `setname`, `resetname` | 所有人 |
| `strangerrealms.island.language` | `language` | 所有人 |
| `strangerrealms.island.settings` | `settings` | 所有人 |
| `strangerrealms.island.lock` | `lock` | 所有人 |
| `strangerrealms.island.ban` | `ban`, `unban`, `banlist` | 所有人 |
| `strangerrealms.island.expel` | `expel` | 所有人 |
| `strangerrealms.island.team` | `team` | 所有人 |
| `strangerrealms.island.team.invite` | `team invite` | 所有人 |
| `strangerrealms.island.team.accept` | `team accept` | 所有人 |
| `strangerrealms.island.team.reject` | `team reject` | 所有人 |
| `strangerrealms.island.team.leave` | `team leave` | 所有人 |
| `strangerrealms.island.team.kick` | `team kick` | 所有人 |
| `strangerrealms.island.team.promote` | `team promote`, `team demote` | 所有人 |
| `strangerrealms.island.team.setowner` | `team setowner` | 所有人 |
| `strangerrealms.island.team.trust` | `team trust`, `team untrust` | 所有人 |
| `strangerrealms.island.team.coop` | `team coop`, `team uncoop` | 所有人 |

## Permissions only in StrangerRealms { #permissions-only-in-strangerrealms }

| Permission | Allows | Default |
|---|---|---|
| `strangerrealms.claim` | `/st claim` | 所有人 |
| `strangerrealms.unclaim` | `/st unclaim` | 所有人 |
| `strangerrealms.spawn` | `/st spawn` | 所有人 |
| `strangerrealms.admin.worldborder` | `/stranger worldborder` | 操作员（未声明） |

管理员和版主权限（`strangerrealms.admin.*`、`strangerrealms.mod.*`） 默认为操作员。请参见[工作人员权限](../../BentoBox/Permissions-Guide.md#staff-permissions).
