# 权限 { #permissions }

每个 BentoBox 权限，从 BentoBox 源生成。关于如何使用它们（VIP 等级、工作人员角色、常见错误），参见[权限和 VIP 特权](Permissions-Guide.md)。

游戏模式权限以游戏模式的前缀开头，写作 `[gamemode].` 这里：`bskyblock.`、`aoneblock.`、`acidisland.`、`caveblock.` 等。附属权限列在每个[附属的页面](../addons/Bank/index.md)中。

!!! tip "在你的服务器上查看默认值"
    默认值（所有人、仅操作员或没人）由每个游戏模式设置，它们之间有所不同。在控制台运行 `/bentobox perms` 来打印每个命令权限及其在你的服务器上的默认值。

## BentoBox { #bentobox }

| 权限 | 默认 | 允许 |
|---|---|---|
| `bentobox.about` | 所有人 | `/bentobox about` |
| `bentobox.version` | 操作员 | `/bentobox version` |
| `bentobox.admin` | 操作员 | `/bentobox` 及其管理员子命令 |
| `bentobox.admin.reload` | 操作员 | `/bentobox reload` 和 `reload locales` |
| `bentobox.admin.manage` | 操作员 | `/bentobox manage` |
| `bentobox.admin.catalog` | 操作员 | `/bentobox catalog` |
| `bentobox.admin.locale` | 操作员 | `/bentobox locale` |
| `bentobox.admin.migrate` | 操作员 | `/bentobox migrate` |
| `bentobox.admin.perms` | 操作员 | `/bentobox perms` |
| `bentobox.admin.rank` | 操作员 | `/bentobox rank` |
| `bentobox.admin.placeholders` | 操作员 | `/bentobox placeholders` |
| `bentobox.admin.dump-placeholders` | 操作员 | `/bentobox dump-placeholders` |

## 游戏模式：玩家命令 { #game-mode-player-commands }

大多数这些由游戏模式提供给所有人。用 `/bentobox perms` 检查；在某些游戏模式中 `island.homes`、`island.deletehome` 和 `island.renamehome` 默认为仅操作员。

| 权限 | 允许 |
|---|---|
| `[gamemode].island` | 玩家命令本身和 `help` |
| `[gamemode].island.ban` | `ban`、`banlist`、`unban` |
| `[gamemode].island.create` | `create` |
| `[gamemode].island.deletehome` | `deletehome` |
| `[gamemode].island.expel` | `expel` |
| `[gamemode].island.home` | `go` |
| `[gamemode].island.homes` | `homes` |
| `[gamemode].island.info` | `info` |
| `[gamemode].island.language` | `language` |
| `[gamemode].island.lock` | `lock` |
| `[gamemode].island.name` | `resetname`、`setname` |
| `[gamemode].island.near` | `near` |
| `[gamemode].island.renamehome` | `renamehome` |
| `[gamemode].island.reset` | `reset` |
| `[gamemode].island.sethome` | `sethome` |
| `[gamemode].island.settings` | `settings` |
| `[gamemode].island.spawn` | `spawn` |
| `[gamemode].island.team` | `team` |
| `[gamemode].island.team.accept` | `team accept` |
| `[gamemode].island.team.coop` | `team coop`、`team uncoop` |
| `[gamemode].island.team.invite` | `team invite`、`team uninvite` |
| `[gamemode].island.team.kick` | `team kick` |
| `[gamemode].island.team.leave` | `team leave` |
| `[gamemode].island.team.promote` | `team demote`、`team promote` |
| `[gamemode].island.team.reject` | `team reject` |
| `[gamemode].island.team.setowner` | `team setowner` |
| `[gamemode].island.team.trust` | `team trust`、`team untrust` |

## 游戏模式：管理员和版主命令 { #game-mode-admin-and-moderator-commands }

默认为仅操作员。

| 权限 | 允许 `/[admin_command]` |
|---|---|
| `[gamemode].admin` | 管理员命令本身和 `help` |
| `[gamemode].admin.blueprint` | `blueprint` |
| `[gamemode].admin.blueprint.copy` | `blueprint copy` |
| `[gamemode].admin.blueprint.delete` | `blueprint delete` |
| `[gamemode].admin.blueprint.list` | `blueprint list` |
| `[gamemode].admin.blueprint.load` | `blueprint load` |
| `[gamemode].admin.blueprint.origin` | `blueprint origin` |
| `[gamemode].admin.blueprint.paste` | `blueprint paste` |
| `[gamemode].admin.blueprint.pos1` | `blueprint pos1` |
| `[gamemode].admin.blueprint.pos2` | `blueprint pos2` |
| `[gamemode].admin.blueprint.rename` | `blueprint rename` |
| `[gamemode].admin.blueprint.save` | `blueprint save` |
| `[gamemode].admin.blueprint.sink` | `blueprint sink` |
| `[gamemode].admin.deaths` | `deaths` |
| `[gamemode].admin.deaths.add` | `deaths add` |
| `[gamemode].admin.deaths.remove` | `deaths remove` |
| `[gamemode].admin.deaths.reset` | `deaths reset` |
| `[gamemode].admin.deaths.set` | `deaths set` |
| `[gamemode].admin.delete` | `delete` |
| `[gamemode].admin.getrank` | `getrank` |
| `[gamemode].admin.purge` | `purge` |
| `[gamemode].admin.purge.age-regions` | `purge age-regions` |
| `[gamemode].admin.purge.deleted` | `purge deleted` |
| `[gamemode].admin.purge.protect` | `purge protect` |
| `[gamemode].admin.purge.unowned` | `purge unowned` |
| `[gamemode].admin.range` | `range` |
| `[gamemode].admin.range.add` | `range add` |
| `[gamemode].admin.range.display` | `range display` |
| `[gamemode].admin.range.purgebonus` | `range purgebonus` |
| `[gamemode].admin.range.remove` | `range remove` |
| `[gamemode].admin.range.removebonus` | `range removebonus` |
| `[gamemode].admin.range.reset` | `range reset` |
| `[gamemode].admin.range.set` | `range set` |
| `[gamemode].admin.register` | `register` |
| `[gamemode].admin.reload` | `reload` |
| `[gamemode].admin.resetflags` | `resetflags` |
| `[gamemode].admin.resets` | `resets` |
| `[gamemode].admin.resets.add` | `resets add` |
| `[gamemode].admin.resets.remove` | `resets remove`、`resets reset` |
| `[gamemode].admin.resets.set` | `resets set` |
| `[gamemode].admin.setprotectionlocation` | `setprotectionlocation` |
| `[gamemode].admin.setrank` | `setrank` |
| `[gamemode].admin.setspawn` | `setspawn` |
| `[gamemode].admin.setspawnpoint` | `setspawnpoint` |
| `[gamemode].admin.settings` | `settings` |
| `[gamemode].admin.tp` | `tp`、`tpend`、`tpnether` |
| `[gamemode].admin.tpuser` | `tpuser`、`tpuserend`、`tpusernether` |
| `[gamemode].admin.undelete` | `undelete` |
| `[gamemode].admin.unregister` | `unregister` |
| `[gamemode].admin.version` | `version` |
| `[gamemode].admin.why` | `why` |
| `[gamemode].mod.deletehomes` | `deletehomes` |
| `[gamemode].mod.info` | `info` |
| `[gamemode].mod.maxhomes` | `maxhomes` |
| `[gamemode].mod.resethome` | `resethome` |
| `[gamemode].mod.resetname` | `resetname` |
| `[gamemode].mod.switch` | `switch` |
| `[gamemode].mod.team` | `team` |
| `[gamemode].mod.team.add` | `team add` |
| `[gamemode].mod.team.disband` | `team disband` |
| `[gamemode].mod.team.disbandall` | `team disbandall` |
| `[gamemode].mod.team.kick` | `team kick` |
| `[gamemode].mod.team.maxsize` | `team maxsize` |
| `[gamemode].mod.team.setowner` | `team setowner` |

## 游戏模式：限制和特权 { #game-mode-limits-and-perks }

这些以数字结尾，它为该玩家替换配置值。玩家拥有的最高数字获胜。参见[权限和 VIP 特权](Permissions-Guide.md#perks-with-a-number)了解规则。

| 权限 | 设置 | 它替换的配置值 |
|---|---|---|
| `[gamemode].team.maxsize.<n>` | 团队大小，包括所有者（岛屿所有者的权限） | `island.max-team-size` |
| `[gamemode].coop.maxsize.<n>` | 合作玩家（岛屿所有者的权限） | `island.max-coop-size` |
| `[gamemode].trust.maxsize.<n>` | 信任的玩家（岛屿所有者的权限） | `island.max-trusted-size` |
| `[gamemode].island.range.<n>` | 岛屿保护范围（岛屿所有者的权限） | `world.protection-range` |
| `[gamemode].island.maxhomes.<n>` | 家点数量（岛屿所有者的权限） | `island.max-homes` |
| `[gamemode].island.number.<n>` | 玩家可以拥有的岛屿数量 | `world.concurrent-islands` |
| `[gamemode].ban.maxlimit.<n>` | 他们一次可以禁止的玩家 | `world.ban-limit` |

| 权限 | 允许 |
|---|---|
| `[gamemode].island.create.<bundle>` | 选择需要权限的启动岛屿（蓝图包） |
| `[gamemode].island.name.format` | 岛屿名称中的颜色代码 |

## 游戏模式：岛屿设置 { #game-mode-island-settings }

| 权限 | 允许 |
|---|---|
| `[gamemode].settings.<FLAG_ID>` | 在 `/[player_command] settings` 中更改该设置 |
| `[gamemode].settings.*` | 更改所有设置 |
| `[gamemode].admin.settings.<FLAG_ID>` | 在 `/[admin_command] settings` 中更改该标志 |
| `[gamemode].admin.world.settings.<FLAG_ID>` | 更改该世界设置或世界保护 |
| `[gamemode].admin.set-world-defaults` | 管理员设置中的“世界保护”标签页 |

标志 ID 参见[岛屿保护、标志和等级](Island-Protection,-Flags-&-Ranks.md)。

## 游戏模式：版主绕过 { #game-mode-moderator-bypasses }

| 权限 | 效果 |
|---|---|
| `[gamemode].mod.bypassprotect` | 在任何地方忽略所有保护标志 |
| `[gamemode].mod.bypass.<FLAG_ID>.everywhere` | 在任何地方忽略某一个保护标志 |
| `[gamemode].mod.bypass.<FLAG_ID>.island` | 在岛屿上忽略某一个保护标志 |
| `[gamemode].mod.bypasslock` | 进入已锁定的岛屿 |
| `[gamemode].mod.bypassban` | 进入自己被封禁的岛屿 |
| `[gamemode].mod.bypassexpel` | 不会被驱逐 |
| `[gamemode].mod.bypasscooldowns` | 跳过命令冷却 |
| `[gamemode].mod.bypassdelays` | 跳过传送延迟 |
| `[gamemode].admin.noban` | 不能被岛屿封禁 |
| `[gamemode].admin.noexpel` | 不能被驱逐出岛屿 |

`/[admin_command] switch` 可以关闭和重新开启版主的绕过权限。参见[绕过保护](Island-Protection,-Flags-&-Ranks.md#bypass-the-protection)。
