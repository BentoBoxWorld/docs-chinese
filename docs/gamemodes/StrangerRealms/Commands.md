# StrangerRealms 命令

| | 命令 | 权限前缀 |
|---|---|---|
| 玩家 | `/st` （也是 `/strange`）| `strangerrealms.` |
| 管理员 | `/stranger` | `strangerrealms.` |

可以在游戏模式的 `config.yml` 中重命名两条命令。

## 标准命令

StrangerRealms 使用 BentoBox 的标准玩家和管理员命令。所有命令及其权限都列在[命令参考](../../BentoBox/Commands.md)中：将 `/[player_command]` 替换为 `/st`、`/[admin_command]` 替换为 `/stranger` 且 `[gamemode]` 替换为 `strangerrealms`。例如：

```
/st              前往你的领地或创建一个
/st team invite <player>
/st settings
/stranger info <player>
/stranger why <player>
```

有关其功能，请参见[玩家指南](../../BentoBox/Player-Guide.md)和管理指南，如[团队和等级](../../BentoBox/About/Teams.md)和[岛屿](../../BentoBox/About/IslandManagement.md)。

## 仅在 StrangerRealms 中的命令

| 命令 | 功能 | 权限 | 默认 |
|---|---|---|---|
| `/st claim` | 声称你所站立的土地 | `strangerrealms.claim` | 所有人 |
| `/st unclaim` | 移除你的声称 | `strangerrealms.unclaim` | 所有人 |
| `/st spawn` | 传送到生成点（替换标准生成命令） | `strangerrealms.spawn` | 所有人 |
| `/stranger worldborder [on\|off\|set\|auto\|info]` | 更改世界边界设置 | `strangerrealms.admin.worldborder` | 操作员（未声明） |

StrangerRealms 玩家使用 `/st claim` 声称土地而不是创建岛屿，所以玩家不能使用 `/st create`（`strangerrealms.island.create` 未声明，这使其仅限操作员），且没有子命令的 `/st` 会将新玩家发送到生成点。

## 附属命令

附属为 `/st` 和 `/stranger`，例如 `/st level` 来自[Level](../../addons/Level/index.md)或 `/st challenges` 来自[Challenges](../../addons/Challenges/index.md). 请参见每个附属页面。
