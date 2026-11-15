# BSkyBlock 命令 { #bskyblock-commands }

| | 命令 | 权限前缀 |
|---|---|---|
| 玩家 | `/island` （也是 `/is`, `/skyblock`, `/sb`）| `bskyblock.` |
| 管理员 | `/bsbadmin` （也是 `/bsb`, `/skyblockadmin`, `/sbadmin`, `/sba`）| `bskyblock.` |

可以在游戏模式的 `config.yml` 中重命名两条命令。

## 标准命令 { #standard-commands }

BSkyBlock 使用 BentoBox 的标准玩家和管理员命令。所有命令及其权限都列在[命令参考](../../BentoBox/Commands.md)中：将 `/[player_command]` 替换为 `/island`、`/[admin_command]` 替换为 `/bsbadmin` 且 `[gamemode]` 替换为 `bskyblock`。例如：

```
/island              前往你的岛屿或创建一个
/island team invite <player>
/island settings
/bsbadmin info <player>
/bsbadmin why <player>
```

有关其功能，请参见[玩家指南](../../BentoBox/Player-Guide.md)和管理指南，如[团队和等级](../../BentoBox/About/Teams.md)和[岛屿](../../BentoBox/About/IslandManagement.md)。

## 仅在 BSkyBlock 中的命令 { #commands-only-in-bskyblock }

| 命令 | 功能 | 权限 | 默认 |
|---|---|---|---|
| `/island about` | 显示版权和许可证信息 | `bskyblock.island` | 所有人 |

## 附属命令 { #addon-commands }

附属为 `/island` 和 `/bsbadmin`，例如 `/island level` 来自[Level](../../addons/Level/index.md)或 `/island challenges` 来自[Challenges](../../addons/Challenges/index.md). 请参见每个附属页面。
