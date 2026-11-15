# CaveBlock 命令

| | 命令 | 权限前缀 |
|---|---|---|
| 玩家 | `/cave` （也是 `/cb`）| `caveblock.` |
| 管理员 | `/cbadmin` （也是 `/cba`）| `caveblock.` |

可以在游戏模式的 `config.yml` 中重命名两条命令。

## 标准命令

CaveBlock 使用 BentoBox 的标准玩家和管理员命令。所有命令及其权限都列在[命令参考](../../BentoBox/Commands.md)中：将 `/[player_command]` 替换为 `/cave`、`/[admin_command]` 替换为 `/cbadmin` 且 `[gamemode]` 替换为 `caveblock`。例如：

```
/cave              go to your cave, or create one
/cave team invite <player>
/cave settings
/cbadmin info <player>
/cbadmin why <player>
```

有关其功能，请参见[玩家指南](../../BentoBox/Player-Guide.md)和管理指南，如[团队和等级](../../BentoBox/About/Teams.md)和[岛屿](../../BentoBox/About/IslandManagement.md)。

## 仅在 CaveBlock 中的命令

| 命令 | 功能 | 权限 | 默认 |
|---|---|---|---|
| `/cave about` | 显示版权和许可证信息 | `caveblock.island` | 所有人 |

## 附属命令

附属为 `/cave` 和 `/cbadmin`，例如 `/cave level` 来自[Level](../../addons/Level/index.md)或 `/cave challenges` 来自[Challenges](../../addons/Challenges/index.md). 请参见每个附属页面。
