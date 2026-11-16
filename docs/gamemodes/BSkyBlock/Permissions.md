# BSkyBlock 权限 { #bskyblock-permissions }

BSkyBlock 权限以 `bskyblock.` 开头。每个权限 列在 [Permissions reference](../../BentoBox/Permissions.md) with `[gamemode]` in place of `bskyblock`。有关 VIP 特权，如更大的团队、岛屿和更多家点，请参见[权限和 VIP 特权](../../BentoBox/Permissions-Guide.md)。

## 玩家命令：默认谁拥有它们 { #player-commands-who-has-them-by-default }

这些默认值来自 BSkyBlock 的 `addon.yml`. **所有人** 表示所有玩家 都拥有该权限，除非你取消; **操作员** 表示你需要 通过权限插件授予玩家. 运行 `/bentobox perms` 在控制台查看服务器上的默认值.

| 权限 | 命令 | 默认 |
|---|---|---|
| `bskyblock.island` | 玩家命令本身 | 所有人 |
| `bskyblock.island.create` | `create` | 所有人 |
| `bskyblock.island.home` | `go` | 所有人 |
| `bskyblock.island.homes` | `homes` | 所有人 |
| `bskyblock.island.sethome` | `sethome` | 所有人 |
| `bskyblock.island.deletehome` | `deletehome` | 所有人 |
| `bskyblock.island.renamehome` | `renamehome` | 所有人 |
| `bskyblock.island.spawn` | `spawn` | 所有人 |
| `bskyblock.island.info` | `info` | 所有人 |
| `bskyblock.island.near` | `near` | 所有人 |
| `bskyblock.island.reset` | `reset` | 所有人 |
| `bskyblock.island.name` | `setname`, `resetname` | 所有人 |
| `bskyblock.island.language` | `language` | 所有人 |
| `bskyblock.island.settings` | `settings` | 所有人 |
| `bskyblock.island.lock` | `lock` | 所有人 |
| `bskyblock.island.ban` | `ban`, `unban`, `banlist` | 所有人 |
| `bskyblock.island.expel` | `expel` | 所有人 |
| `bskyblock.island.team` | `team` | 所有人 |
| `bskyblock.island.team.invite` | `team invite` | 所有人 |
| `bskyblock.island.team.accept` | `team accept` | 所有人 |
| `bskyblock.island.team.reject` | `team reject` | 所有人 |
| `bskyblock.island.team.leave` | `team leave` | 所有人 |
| `bskyblock.island.team.kick` | `team kick` | 所有人 |
| `bskyblock.island.team.promote` | `team promote`, `team demote` | 所有人 |
| `bskyblock.island.team.setowner` | `team setowner` | 所有人 |
| `bskyblock.island.team.trust` | `team trust`, `team untrust` | 所有人 |
| `bskyblock.island.team.coop` | `team coop`, `team uncoop` | 所有人 |

管理员和版主权限（`bskyblock.admin.*`、`bskyblock.mod.*`） 默认为操作员。请参见[工作人员权限](../../BentoBox/Permissions-Guide.md#staff-permissions).
