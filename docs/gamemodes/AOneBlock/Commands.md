# AOneBlock 命令

| | 命令 | 权限前缀 |
|---|---|---|
| 玩家 | `/ob` （也是 `/oneblock`）| `aoneblock.` |
| 管理员 | `/obadmin` （也是 `/oneblockadmin`, `/oba`）| `aoneblock.` |

可以在游戏模式的 `config.yml` 中重命名两条命令。

## 标准命令

AOneBlock 使用 BentoBox 的标准玩家和管理员命令。所有命令及其权限都列在[命令参考](../../BentoBox/Commands.md)中：将 `/[player_command]` 替换为 `/ob`、`/[admin_command]` 替换为 `/obadmin` 且 `[gamemode]` 替换为 `aoneblock`。例如：

```
/ob              前往你的岛屿或创建一个
/ob team invite <player>
/ob settings
/obadmin info <player>
/obadmin why <player>
```

有关其功能，请参见[玩家指南](../../BentoBox/Player-Guide.md)和管理指南，如[团队和等级](../../BentoBox/About/Teams.md)和[岛屿](../../BentoBox/About/IslandManagement.md)。

## 仅在 AOneBlock 中的命令

| 命令 | 功能 | 权限 | 默认 |
|---|---|---|---|
| `/ob count` | 显示你的方块计数和阶段 | `aoneblock.count` | 所有人 |
| `/ob phases` | 显示所有阶段的列表 | `aoneblock.phases` | 操作员 |
| `/ob setCount <count>` | 将你的方块计数设置回你已经达到的值 | `aoneblock.island.setcount` | 操作员 |
| `/ob respawnBlock` | 重新生成魔法方块（如果它消失了）（别名：check） | `aoneblock.respawn-block` | 所有人 |
| `/ob bossbar` | 打开或关闭阶段 Boss 栏 | `aoneblock.island.bossbar` | 所有人 |
| `/ob actionbar` | 打开或关闭阶段操作栏 | `aoneblock.island.actionbar` | 所有人 |
| `/obadmin setcount <name> <count> [lifetime]` | 设置玩家的方块计数 | `aoneblock.admin.setcount` | 操作员 |
| `/obadmin setchest <phase> <rarity>` | 将你正在看的箱子添加到一个阶段，并指定稀有度 | `aoneblock.admin.setchest` | 操作员 |
| `/obadmin sanity <phase>` | 将阶段的方块概率检查打印到控制台 | `aoneblock.admin.sanity` | 操作员 |
| `/obadmin phases` | 打开阶段顺序编辑器 | `aoneblock.admin.phases` | 操作员 |

AOneBlock 玩家命令标签（`count`、`phases`、`setCount`、`respawnBlock`、`bossbar`、`actionbar`）可以在 `config.yml` 的 `aoneblock.command` 下重命名。Boss 栏和操作栏命令只在启用这些功能时存在。

## 附属命令

附属为 `/ob` 和 `/obadmin`，例如 `/ob level` 来自[Level](../../addons/Level/index.md)或 `/ob challenges` 来自[Challenges](../../addons/Challenges/index.md). 请参见每个附属页面。
