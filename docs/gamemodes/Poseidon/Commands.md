# Poseidon 命令 { #poseidon-commands }

| | 命令 | 权限前缀 |
|---|---|---|
| 玩家 | `/po` | `poseidon.` |
| 管理员 | `/padmin` | `poseidon.` |

可以在游戏模式的 `config.yml` 中重命名两条命令。

## 标准命令 { #standard-commands }

Poseidon 使用 BentoBox 的标准玩家和管理员命令。所有命令及其权限都列在[命令参考](../../BentoBox/Commands.md)中：将 `/[player_command]` 替换为 `/po`、`/[admin_command]` 替换为 `/padmin` 且 `[gamemode]` 替换为 `poseidon`。例如：

```
/po              前往你的岛屿或创建一个
/po team invite <player>
/po settings
/padmin info <player>
/padmin why <player>
```

有关其功能，请参见[玩家指南](../../BentoBox/Player-Guide.md)和管理指南，如[团队和等级](../../BentoBox/About/Teams.md)和[岛屿](../../BentoBox/About/IslandManagement.md)。

## 仅在 Poseidon 中的命令 { #commands-only-in-poseidon }

| 命令 | 功能 | 权限 | 默认 |
|---|---|---|---|
| `/po about` | 显示版权和许可证信息 | `poseidon.island` | 所有人 |

## 附属命令 { #addon-commands }

附属为 `/po` 和 `/padmin`，例如 `/po level` 来自[Level](../../addons/Level/index.md)或 `/po challenges` 来自[Challenges](../../addons/Challenges/index.md). 请参见每个附属页面。
