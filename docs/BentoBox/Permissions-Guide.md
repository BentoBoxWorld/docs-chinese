# 权限和 VIP 特权 { #permissions-vip-perks }

BentoBox 可与任何权限插件配合使用（LuckPerms 是最常见的）。这个页面解释了 BentoBox 的权限如何命名、玩家默认拥有哪些权限，以及如何给予等级或 VIP 更大的团队、更大的岛屿、更多家点和其他特权。

!!! info "这个页面中的例子"
    例子使用 BSkyBlock，其权限以 `bskyblock.` 开头，以及 LuckPerms 命令。每个游戏模式都有其自己的前缀，例如 `aoneblock.`、`acidisland.` 或 `caveblock.`，所以必须为每个游戏模式分别给予一次特权。

## 权限如何命名 { #how-the-permissions-are-named }

| 权限以什么开头 | 用于 | 谁默认拥有 |
|---|---|---|
| `bentobox.` | `/bentobox` 命令 | 操作员（`bentobox.about` 面向所有人） |
| `<gamemode>.island.` | 玩家命令，如 `bskyblock.island.team.invite` | 主要是玩家。参见[下方](#check-what-players-have-by-default) |
| `<gamemode>.admin.` | 管理员命令，如 `bskyblock.admin.delete` | 操作员 |
| `<gamemode>.mod.` | 版主命令和保护绕过，如 `bskyblock.mod.info` | 操作员 |
| `<gamemode>.settings.` | 在 `/island settings` 中改变岛屿设置 | 玩家 |
| `<gamemode>.<thing>.<number>` | 限制，如 `bskyblock.team.maxsize.8` | 无：使用配置值 |

附属添加他们自己的权限。它们列在每个[附属的页面](../addons/Bank/index.md)上。

### 检查玩家默认拥有什么 { #check-what-players-have-by-default }

在控制台中运行 **`/bentobox perms`**。它打印每个 BentoBox 和游戏模式命令权限及其默认值（`TRUE` 表示所有人，`OP` 表示操作员，`FALSE` 表示无人），格式为你可以粘贴到权限插件中的。

!!! warning "某些玩家命令默认为仅操作员"
    在 BSkyBlock 和 AcidIsland 中，`island.deletehome` 和 `island.renamehome` 默认为仅操作员。在 AcidIsland 中，`island.homes` 也是。如果你给玩家多于一个家点，也要给他们这些：

    ```
    /lp group default permission set bskyblock.island.homes true
    /lp group default permission set bskyblock.island.deletehome true
    /lp group default permission set bskyblock.island.renamehome true
    ```

## 带有数字的特权 { #perks-with-a-number }

这些权限以一个数字结尾。该数字替换游戏模式的 `config.yml` 中该玩家的值。

| 特权 | 权限 | 配置默认值 | 检查对象 |
|---|---|---|---|
| 团队大小（包括所有者） | `bskyblock.team.maxsize.<n>` | `island.max-team-size` | 岛屿所有者 |
| 合作玩家 | `bskyblock.coop.maxsize.<n>` | `island.max-coop-size` | 岛屿所有者 |
| 信任的玩家 | `bskyblock.trust.maxsize.<n>` | `island.max-trusted-size` | 岛屿所有者 |
| 岛屿大小（保护范围） | `bskyblock.island.range.<n>` | `world.protection-range` | 岛屿所有者 |
| 家点数量 | `bskyblock.island.maxhomes.<n>` | `island.max-homes` | 岛屿所有者 |
| 岛屿数量 | `bskyblock.island.number.<n>` | `world.concurrent-islands` | 玩家 |
| 他们可以禁止的玩家数 | `bskyblock.ban.maxlimit.<n>` | `world.ban-limit`（`-1` = 无限制） | 玩家 |

数字如何计算：

- **最高数字获胜。** 同时拥有 `team.maxsize.6` 和 `team.maxsize.10` 的玩家得到 10。等级可以堆叠而不冲突。
- **数字替换配置值，即使它更低。** `team.maxsize.2` 给一个 2 人的团队，即使配置说 4。仅授予这些权限来提高限制。
- **`.*` 被忽略。** 通过通配符或操作员插件拥有 `bskyblock.team.maxsize.*` 的玩家得到配置值，而不是无限制。改用一个大数字。
- **岛屿特权跟随所有者。** 团队大小、范围和家点来自岛屿**所有者**的权限，而不是每个成员的。它们在所有者登录时更新，范围也在岛屿创建时设置。
- **岛屿大小被限制**在 `distance-between-islands`；要求更多没有效果。参见[岛屿](About/IslandManagement.md#island-size-protection-range)。

## 其他特权 { #other-perks }

| 特权 | 权限 |
|---|---|
| 创建岛屿菜单中的 VIP 初始岛屿 | `bskyblock.island.create.<bundle-name>`，在 `/bsbadmin blueprint` 中将该包设置为需要权限后。参见[岛屿](About/IslandManagement.md#creating-islands) |
| 岛屿名称中的颜色代码 | `bskyblock.island.name.format` |
| 跳过命令冷却（重置、邀请） | `bskyblock.mod.bypasscooldowns` |
| 跳过传送延迟 | `bskyblock.mod.bypassdelays` |
| 不能被禁止或从岛屿中逐出 | `bskyblock.admin.noban`、`bskyblock.admin.noexpel` |
| 不能改变特定的岛屿设置 | 移除 `bskyblock.settings.<FLAG_ID>`。参见[保护、标志与等级](Island-Protection,-Flags-&-Ranks.md#settings-tab) |

**不是**权限的东西：额外的岛屿重置（使用 `/bsbadmin resets`，参见[岛屿](About/IslandManagement.md#resetting-islands)），以及在别人的岛屿上邀请、踢出或禁止的权利（岛屿所有者通过等级控制，参见[团队与等级](About/Teams.md#letting-members-manage-the-team)）。

## 例子：VIP 等级 { #example-a-vip-rank }

BSkyBlock 中的一个 VIP 组，拥有 8 人团队、更大的岛屿、三个家点和一个 VIP 初始岛屿：

```
/lp creategroup vip
/lp group vip permission set bskyblock.team.maxsize.8 true
/lp group vip permission set bskyblock.island.range.100 true
/lp group vip permission set bskyblock.island.maxhomes.3 true
/lp group vip permission set bskyblock.island.homes true
/lp group vip permission set bskyblock.island.deletehome true
/lp group vip permission set bskyblock.island.renamehome true
/lp group vip permission set bskyblock.island.create.vip true
/lp user <player> parent add vip
```

玩家必须**登出并重新登入**以对他们已经拥有的岛屿应用团队大小、范围和家点。

要通过游戏内货币分步出售升级（更大的岛屿、更多团队槽位、更多家点），请参见[升级](../addons/Upgrades/index.md)附属。

## 员工权限 { #staff-permissions }

| 角色 | 授予 |
|---|---|
| 一个游戏模式的完整管理员 | `bskyblock.admin.*` 和 `bskyblock.mod.*` |
| 可以查看但不能改变岛屿的版主 | `bskyblock.mod.info`、`bskyblock.admin.tp`、`bskyblock.mod.bypasslock`、`bskyblock.mod.bypassban` |
| 可以在任何地方建造的版主 | 添加 `bskyblock.mod.bypassprotect` 和 `bskyblock.mod.switch`（让他们用 `/bsbadmin switch` 关闭绕过） |
| BentoBox 管理员（重新加载、管理、迁移） | `bentobox.admin` 及其子权限 |

所有的保护绕过权限在[保护、标志与等级](Island-Protection,-Flags-&-Ranks.md#bypass-the-protection)中解释。

## 故障排除 { #troubleshooting }

**特权不适用。**
岛屿特权来自岛屿所有者并在他们登入时更新。让所有者登出再登入。对于范围，检查 `distance-between-islands` 不低于这个数字。

**VIP 获得的团队比普通玩家小。**
另一个组中的较低数字替换了配置值。移除它；使用玩家拥有的最高数字。

**玩家不能使用命令。**
运行 `/bentobox perms` 并检查该命令的默认值。如果是 `OP` 或 `FALSE`，给它给你的默认组。

**特权在一个游戏模式中有效，但在另一个中无效。**
每个游戏模式都有其自己的前缀。为 `aoneblock.`、`acidisland.` 等再次给予权限。

## 另请参见 { #see-also }

- [权限参考](Permissions.md)：每个 BentoBox 和游戏模式权限
- [命令参考](Commands.md)
- [团队与等级](About/Teams.md)、[岛屿](About/IslandManagement.md)、[保护、标志与等级](Island-Protection,-Flags-&-Ranks.md)
