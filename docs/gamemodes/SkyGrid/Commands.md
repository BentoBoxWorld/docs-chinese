# SkyGrid 命令 { #skygrid-commands }

| | 命令 | 权限前缀 |
|---|---|---|
| 玩家 | `/skygrid` （也是 `/sg`）| `skygrid.` |
| 管理员 | `/sgadmin` （也是 `/sga`）| `skygrid.` |

可以在游戏模式的 `config.yml` 中重命名两条命令。

## 标准命令 { #standard-commands }

SkyGrid 使用 BentoBox 的标准玩家和管理员命令。所有命令及其权限都列在[命令参考](../../BentoBox/Commands.md)中：将 `/[player_command]` 替换为 `/skygrid`、`/[admin_command]` 替换为 `/sgadmin` 且 `[gamemode]` 替换为 `skygrid`。例如：

```
/skygrid              前往你的区域或创建一个
/skygrid team invite <player>
/skygrid settings
/sgadmin info <player>
/sgadmin why <player>
```

有关其功能，请参见[玩家指南](../../BentoBox/Player-Guide.md)和管理指南，如[团队和等级](../../BentoBox/About/Teams.md)和[岛屿](../../BentoBox/About/IslandManagement.md)。

SkyGrid 不添加任何其自己的命令。

## 附属命令 { #addon-commands }

附属为 `/skygrid` 和 `/sgadmin`，例如 `/skygrid level` 来自[Level](../../addons/Level/index.md)或 `/skygrid challenges` 来自[Challenges](../../addons/Challenges/index.md). 请参见每个附属页面。
