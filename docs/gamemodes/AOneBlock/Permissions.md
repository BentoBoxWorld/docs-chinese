# AOneBlock 权限

AOneBlock 权限以 `aoneblock.` 开头。每个权限 列在 [Permissions reference](../../BentoBox/Permissions.md) with `[gamemode]` in place of `aoneblock`。有关 VIP 特权，如更大的团队、岛屿和更多家点，请参见[权限和 VIP 特权](../../BentoBox/Permissions-Guide.md)。

## 玩家命令：默认谁拥有它们

这些默认值来自 AOneBlock 的 `addon.yml`. **所有人** 表示所有玩家 都拥有该权限，除非你取消; **操作员** 表示你需要 通过权限插件授予玩家. 运行 `/bentobox perms` 在控制台查看服务器上的默认值.

| 权限 | 命令 | 默认 |
|---|---|---|
| `aoneblock.island` | 玩家命令本身 | 所有人 |
| `aoneblock.island.create` | `create` | 所有人 |
| `aoneblock.island.home` | `go` | 所有人 |
| `aoneblock.island.homes` | `homes` | 所有人 |
| `aoneblock.island.sethome` | `sethome` | 所有人 |
| `aoneblock.island.deletehome` | `deletehome` | 所有人 |
| `aoneblock.island.renamehome` | `renamehome` | 所有人 |
| `aoneblock.island.spawn` | `spawn` | 所有人 |
| `aoneblock.island.info` | `info` | 所有人 |
| `aoneblock.island.near` | `near` | 所有人 |
| `aoneblock.island.reset` | `reset` | 所有人 |
| `aoneblock.island.name` | `setname`, `resetname` | 所有人 |
| `aoneblock.island.language` | `language` | 所有人 |
| `aoneblock.island.settings` | `settings` | 所有人 |
| `aoneblock.island.lock` | `lock` | 所有人 |
| `aoneblock.island.ban` | `ban`, `unban`, `banlist` | 所有人 |
| `aoneblock.island.expel` | `expel` | 所有人 |
| `aoneblock.island.team` | `team` | 所有人 |
| `aoneblock.island.team.invite` | `team invite` | 所有人 |
| `aoneblock.island.team.accept` | `team accept` | 所有人 |
| `aoneblock.island.team.reject` | `team reject` | 所有人 |
| `aoneblock.island.team.leave` | `team leave` | 所有人 |
| `aoneblock.island.team.kick` | `team kick` | 所有人 |
| `aoneblock.island.team.promote` | `team promote`, `team demote` | 所有人 |
| `aoneblock.island.team.setowner` | `team setowner` | 所有人 |
| `aoneblock.island.team.trust` | `team trust`, `team untrust` | 所有人 |
| `aoneblock.island.team.coop` | `team coop`, `team uncoop` | 所有人 |

## Permissions only in AOneBlock

| Permission | Allows | Default |
|---|---|---|
| `aoneblock.count` | `/ob count` | 所有人 |
| `aoneblock.phases` | `/ob phases` | 操作员 |
| `aoneblock.island.setcount` | `/ob setCount` | 操作员 |
| `aoneblock.respawn-block` | `/ob respawnBlock` | 所有人 |
| `aoneblock.island.bossbar` | `/ob bossbar` | 所有人 |
| `aoneblock.island.actionbar` | `/ob actionbar` | 所有人 |
| `aoneblock.admin.setcount` | `/obadmin setcount` | 操作员 |
| `aoneblock.admin.setchest` | `/obadmin setchest` | 操作员 |
| `aoneblock.admin.sanity` | `/obadmin sanity` | 操作员 |
| `aoneblock.admin.phases` | `/obadmin phases` | 操作员 |

管理员和版主权限（`aoneblock.admin.*`、`aoneblock.mod.*`） 默认为操作员。请参见[工作人员权限](../../BentoBox/Permissions-Guide.md#staff-permissions).
