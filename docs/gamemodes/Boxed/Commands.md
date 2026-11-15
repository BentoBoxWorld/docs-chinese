# Boxed 命令

| | 命令 | 权限前缀 |
|---|---|---|
| 玩家 | `/boxed` （也是 `/bx`, `/box`）| `boxed.` |
| 管理员 | `/boxadmin` | `boxed.` |

可以在游戏模式的 `config.yml` 中重命名两条命令。

## 标准命令

Boxed 使用 BentoBox 的标准玩家和管理员命令。所有命令及其权限都列在[命令参考](../../BentoBox/Commands.md)中：将 `/[player_command]` 替换为 `/boxed`、`/[admin_command]` 替换为 `/boxadmin` 且 `[gamemode]` 替换为 `boxed`。例如：

```
/boxed              go to your box, or create one
/boxed team invite <player>
/boxed settings
/boxadmin info <player>
/boxadmin why <player>
```

有关其功能，请参见[玩家指南](../../BentoBox/Player-Guide.md)和管理指南，如[团队和等级](../../BentoBox/About/Teams.md)和[岛屿](../../BentoBox/About/IslandManagement.md)。

## 仅在 Boxed 中的命令

| 命令 | 功能 | 权限 | 默认 |
|---|---|---|---|
| `/boxadmin place <x> <y> <z> <rotation> <mirror> <no mobs>` | Place a structure at a location | `boxed.admin.place` | 操作员 |

## 附属命令

附属为 `/boxed` 和 `/boxadmin`，例如 `/boxed level` 来自[Level](../../addons/Level/index.md)或 `/boxed challenges` 来自[Challenges](../../addons/Challenges/index.md). 请参见每个附属页面。
