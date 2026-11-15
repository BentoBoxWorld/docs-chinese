# 管理工具

BentoBox 有游戏内工具来查询岛屿、找出为什么某些东西被阻止，以及管理服务器，所以你很少需要手动编辑数据文件。这个页面涵盖你将最经常使用的工具；每个命令都在[命令参考](../Commands.md)中。

!!! info "这个页面中的命令"
    游戏模式管理员命令显示为 `/bsbadmin`（BSkyBlock）。改用你的游戏模式的管理员命令，例如 `/oba`（AOneBlock）、`/acid`（AcidIsland）或 `/cbadmin`（CaveBlock）。他们默认为仅操作员；参见[权限和 VIP 特权](../Permissions-Guide.md#staff-permissions)了解如何给予员工。

## 查询一个岛屿

| 我想要… | 命令 |
|---|---|
| 查看玩家岛屿的一切：所有者、团队、范围、家点、重置、死亡、禁止 | `/bsbadmin info <player>` |
| 查看我所站的岛屿 | `/bsbadmin info` |
| 查看玩家拥有的几个岛屿中的一个 | `/bsbadmin info <player> <island name>` |
| 去玩家的岛屿（或其地狱/末地岛屿） | `/bsbadmin tp <player>`、`tpnether`、`tpend` |
| 将玩家发送到别人的岛屿 | `/bsbadmin tpuser <player> <island owner>` |
| 查看玩家在岛屿上的等级 | `/bsbadmin getrank <player>` |
| 在游戏中显示岛屿的受保护区域 | `/bsbadmin range display` |

## 找出为什么某东西被阻止

当玩家说他们不能做某事（或能做他们不应该做的），打开 **why** 工具：

```
/bsbadmin why <player>
```

然后要求玩家再试一次。控制台记录该玩家的每个保护检查：他们尝试做什么、在哪里、是否被允许、以及哪个标志或等级决定了它。再次运行同一命令来关闭它。玩家必须在线。

大多数问题原来是一个标志为不同的等级而不是预期，或玩家在别人的岛屿上。参见[保护、标志与等级](../Island-Protection,-Flags-&-Ranks.md)。

## 作为普通玩家行动

具有绕过权限的操作员和版主忽略岛屿保护，这使测试混淆。**`/bsbadmin switch`** 关闭你的绕过，所以你像普通玩家一样受保护；再次运行以打开它。操作员状态本身不受影响。参见[绕过保护](../Island-Protection,-Flags-&-Ranks.md#bypass-the-protection)。

## 修复一个岛屿

| 我想要… | 命令 | 更多 |
|---|---|---|
| 改变玩家在岛屿上的等级 | `/bsbadmin setrank <player> <rank>` | [团队与等级](Teams.md) |
| 添加或移除团队成员、改变所有者 | `/bsbadmin team add`、`team kick`、`team setowner` | [团队与等级](Teams.md#common-admin-tasks) |
| 改变岛屿的设置 | `/bsbadmin settings <player>` | [保护、标志与等级](../Island-Protection,-Flags-&-Ranks.md) |
| 使岛屿更大或更小 | `/bsbadmin range set <player> <range>` | [岛屿](IslandManagement.md#island-size-protection-range) |
| 重置玩家的家点，或删除他们的家点 | `/bsbadmin resethome <player>`、`deletehomes <player>` | [岛屿](IslandManagement.md#homes) |
| 清除岛屿的名称 | 站在其上，`/bsbadmin resetname` | [岛屿](IslandManagement.md#island-names) |
| 给玩家重置回来 | `/bsbadmin resets reset <player>` | [岛屿](IslandManagement.md#resetting-islands) |
| 删除、取消删除或重新分配岛屿 | `/bsbadmin delete`、`undelete`、`register` | [岛屿](IslandManagement.md#deleting-islands) |
| 移动岛屿受保护区域的中心 | 站在那里，`/bsbadmin setprotectionlocation` | |
| 重置每个岛屿的设置到配置默认值 | `/bsbadmin resetflags` | |
| 使岛屿成为游戏模式的生成点 | 站在其上，`/bsbadmin setspawn` | |

## 世界设置

**`/bsbadmin settings`** 打开游戏模式的世界的管理员设置菜单：世界设置（如爬行者伤害或访客保留物品栏）、岛屿外的保护规则、新岛屿的默认值，以及玩家可以看到的岛屿设置。参见[管理员设置面板](../Island-Protection,-Flags-&-Ranks.md#admin-settings-panel)。

## 管理 BentoBox

| 命令 | 作用 |
|---|---|
| `/bentobox version` | BentoBox、游戏模式和附属版本、服务器版本和数据库。**当你寻求帮助或报告 bug 时包括此内容。** |
| `/bentobox manage` | 管理面板：你的游戏模式、附属和钩子（BentoBox 配合的其他插件）的选项卡，加上附属目录 |
| `/bentobox catalog` | 浏览你可以下载的游戏模式和附属 |
| `/bentobox reload` | 重新加载 BentoBox 的和附属的设置、语言文件和菜单模板 |
| `/bsbadmin reload` | 重新加载一个游戏模式的设置 |
| `/bentobox perms` | 打印每个命令权限及其默认值（控制台） |
| `/bentobox locale` | 检查语言文件中缺失的翻译 |
| `/bentobox placeholders` | 浏览占位符并打开或关闭他们。参见[占位符](../Placeholders.md) |

一些设置，如世界生成和 `distance-between-islands`，仅在完全重启后生效。

## 数据库

BentoBox 在 BentoBox 的 `config.yml` 中设置的数据库中存储岛屿和玩家。默认是 BentoBox 文件夹中的 **JSON** 文件，不需要设置。对于较大的服务器，或多个共享数据的服务器，你可以使用 **MySQL**（5.7+）、**MariaDB**（10.2.3+）、**PostgreSQL**（9.4+）、**SQLite**（3.28+）或 **MongoDB**（3.6+）。

要改变数据库类型而不丢失数据，参见[改变数据库](../Database-transition.md)。始终先备份。

## 另请参见

- [命令参考](../Commands.md)
- [权限和 VIP 特权](../Permissions-Guide.md)
- [BentoBox 发布说明](../Release-Notes.md)
