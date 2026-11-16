# 团队和等级 { #teams-ranks }

团队让多个玩家共享一个岛屿。每个岛屿都有一个**所有者**，所有者可以邀请其他玩家作为**成员**加入。只需要帮忙一段时间的玩家可以被**信任**或**合作**而不是加入。

这个页面解释团队如何工作、作为管理员你可以配置什么，以及如何处理你从玩家那里得到的常见请求。

!!! info "这个页面中的命令"
    命令以 BSkyBlock（`/island`、`/bsbadmin`）显示。其他游戏模式使用他们自己的命令名称，例如 AOneBlock 中的 `/ob` 或 AcidIsland 中的 `/acid`。权限以游戏模式的前缀开头，例如 `bskyblock.` 或 `aoneblock.`。

## 团队如何工作 { #how-teams-work }

- 玩家通过用 `/island team invite <player>` 邀请某人来开始一个团队。被邀请的玩家接受，放弃他们自己的岛屿（默认情况下），并被传送到团队岛屿。
- 岛屿上的每个人都有一个**等级**。等级决定了他们可以做什么：破坏方块、打开箱子、邀请玩家、踢出玩家等等。
- 所有者在岛屿设置菜单（`/island settings`）中决定每个等级可以做什么。参见[保护、标志和等级](../Island-Protection,-Flags-&-Ranks.md)。
- 只有一个所有者。所有者可以将岛屿交给另一个成员，但必须在离开之前这样做。

### 等级 { #the-ranks }

| 等级 | 值 | 谁拥有 | 计入团队大小？ |
|---|---|---|---|
| 所有者 | 1000 | 拥有岛屿的玩家 | 是 |
| 副所有者 | 900 | 由所有者提升的成员 | 是 |
| 成员 | 500 | 接受了团队邀请的玩家 | 是 |
| 信任的 | 400 | 用 `/island team trust` 信任的玩家 | 否（单独限制） |
| 合作的 | 200 | 用 `/island team coop` 合作的玩家 | 否（单独限制） |
| 访客 | 0 | 岛屿上的其他所有人 | 否 |
| 被禁止 | -1 | 用 `/island ban` 禁止的玩家 | 否 |

更高的等级可以做更低等级可以做的一切。你可以用 `/bentobox rank add` 在这些之间添加你自己的等级（参见[自定义等级](#custom-ranks)）。

### 信任和合作：帮助而不加入 { #trusted-and-coop-helping-without-joining }

信任和合作的玩家可以在岛屿上工作而不成为团队成员。他们保留自己的岛屿。

- **信任的**玩家保留他们的等级直到有人用 `/island team untrust <player>` 移除它。
- **合作的**玩家只在岛屿有团队成员在线时保留他们的等级。当最后一个团队成员下线时，该岛屿上的每个合作玩家都会失去等级。一个合作玩家下线也会失去他们的合作等级。

信任和合作的工作方式与团队邀请相同：另一个玩家得到一个邀请并且必须接受它。

## 玩家可以做什么 { #what-players-can-do }

玩家用 `/island team` 打开团队菜单。从菜单中他们可以看到他们的团队、邀请玩家和改变等级而不需要输入命令。所有相同的操作也可以作为命令使用：

| 命令 | 作用 |
|---|---|
| `/island team` | 打开团队菜单 |
| `/island team invite <player>` | 邀请在线玩家加入团队 |
| `/island team accept` | 接受待处理邀请（团队、信任或合作） |
| `/island team reject` | 拒绝待处理邀请 |
| `/island team leave` | 离开团队。所有者不能离开；他们必须先将岛屿交给别人 |
| `/island team kick <player>` | 从团队中移除成员。在玩家离线时有效 |
| `/island team promote <player>` | 将成员向上移动一个等级（永远不会到所有者） |
| `/island team demote <player>` | 将成员向下移动一个等级（永远不会低于成员） |
| `/island team setowner <player>` | 将岛屿交给另一个成员。旧所有者变成副所有者 |
| `/island team trust <player>` | 给玩家信任等级 |
| `/island team untrust <player>` | 移除信任等级 |
| `/island team coop <player>` | 给在线玩家合作等级 |
| `/island team uncoop <player>` | 移除合作等级 |

玩家在同一时间只能有**一个**待处理邀请。一个新邀请替换旧的。

在 Minecraft 26 及更高版本上，接收团队邀请的玩家看到**接受/拒绝**对话框，所以他们不需要输入命令。敏感命令如 `kick` 和 `leave` 也在对话框中询问确认。两者都可以在 BentoBox 的 `config.yml` 中关闭（`island.dialogs.team-invites` 和 `island.dialogs.confirmations`）。

### 让成员管理团队 { #letting-members-manage-the-team }

默认情况下，只有所有者可以邀请、踢出、提升、降级、信任和合作。所有者可以让从设置菜单的**命令等级**页面使用这些命令的较低等级。例如，所有者可以让副所有者邀请和踢出。

同一页面也控制岛屿命令如 `ban`、`unban`、`expel`、`lock`、`setname` 和 `sethome`。家点命令（`sethome`、`renamehome`、`deletehome`）默认为成员；其他的默认为所有者。

玩家永远不能踢出、提升或降级与自己等级相同或更高的人。

## 设置团队（管理员） { #setting-up-teams-admins }

### 团队大小 { #team-size }

团队大小在游戏模式的 `config.yml` 中设置。**限制包括所有者**，所以 `max-team-size: 4` 表示所有者加三个成员。

```yaml
island:
  # Owner + members
  max-team-size: 4
  # Separate limits for coop and trusted players
  max-coop-size: 4
  max-trusted-size: 4
```

### 更大的团队为 VIP 或等级 { #bigger-teams-for-vips-or-ranks }

给**岛屿所有者**一个权限，末尾带上大小：

| 权限 | 效果 |
|---|---|
| `bskyblock.team.maxsize.<number>` | 此玩家拥有的岛屿的团队大小 |
| `bskyblock.coop.maxsize.<number>` | 合作限制 |
| `bskyblock.trust.maxsize.<number>` | 信任限制 |

例如，使用 LuckPerms：

```
/lp group vip permission set bskyblock.team.maxsize.8 true
```

权限在所有者在线时被检查，岛屿记住结果。只有所有者的权限重要；成员的权限被忽略。

要改变一个岛屿的限制而不使用权限，使用 `/bsbadmin team maxsize <player> <size>`。

### 玩家加入或离开时物品和金钱会发生什么 { #what-happens-to-items-and-money-when-players-join-or-leave }

当玩家接受团队邀请时，他们通常**失去他们自己的岛屿**。在他们接受之前，他们会被警告并要求确认。

BentoBox 也可以在玩家加入或离开团队时清除玩家的物品栏、末地箱、金钱、生命值、饥饿值和经验值。这阻止了玩家从一个岛屿携带物品到另一个岛屿。在游戏模式的 `config.yml` 中设置它：

```yaml
island:
  reset:
    # Leaving or being kicked uses up one of the player's island resets
    leavers-lose-reset: false
    # Kicked players keep their inventory even if on-leave inventory is true
    kicked-keep-inventory: false
    on-join:      # when a player joins a team or makes an island
      inventory: false
      ender-chest: false
      money: false
      exp: false
      health: true
      hunger: true
    on-leave:     # when a player leaves or is kicked
      inventory: false
      ender-chest: false
      money: false
      # ... same options as on-join
```

!!! warning "建议用于大多数服务器"
    默认值保留物品栏，所以你在测试时不会丢失物品。在真实服务器上，考虑设置 `on-join` 和 `on-leave` 的 `inventory` 和 `ender-chest` 为 `true`，以及 `leavers-lose-reset: true`。否则玩家可以填满他们的物品栏，加入朋友的岛屿，离开，然后重复。

你也可以在玩家加入或离开时运行命令，例如重置他们的挑战或给一个工具包：

```yaml
island:
  commands:
    on-join:
      - 'bsbadmin deaths set [name] 0'
    on-leave: []
```

这些从控制台运行，除非命令以 `[SUDO]` 开头，这会以玩家身份运行它。

### 邀请冷却和确认 { #invite-cooldowns-and-confirmations }

这些在 **BentoBox 的** `config.yml`（在 `plugins/BentoBox/` 中），并应用于所有游戏模式：

```yaml
island:
  cooldown:
    time:
      invite: 60   # minutes before a kicked or leaving player can be invited back to that island
      coop: 5      # minutes before an uncooped player can be cooped again
      trust: 5     # minutes before an untrusted player can be trusted again
  confirmation:
    time: 10       # seconds players have to confirm
    commands:
      kick: true
      leave: true
    invites: false # also ask trust/coop invitees to confirm (team invites always confirm)
```

邀请冷却阻止玩家反复加入、完成挑战、离开和重新加入。

### 关闭团队 { #turning-teams-off }

某些游戏模式是为单人游戏设计的。一个游戏模式可以为其世界禁用团队。然后邀请、踢出、离开、提升、降级和 setowner 命令拒绝运行，但信任和合作仍然有效所以玩家仍然可以相互帮助。如果你为已经有团队的世界打开这个，运行 `/bsbadmin team disbandall` 一次来解散现有团队。

### 拥有多个岛屿的玩家 { #players-with-more-than-one-island }

如果你允许每个玩家多个岛屿（`concurrent-islands` 高于 1），`disallow-team-member-islands: true` 阻止团队成员也创建他们自己的岛屿。参见[多个岛屿](../ConcurrentIslands.md)。

## 常见管理任务 { #common-admin-tasks }

| 我想要… | 做这个 |
|---|---|
| 查看玩家团队上的人 | `/bsbadmin info <player>` |
| 将玩家添加到团队 | `/bsbadmin team add <owner> <player>` |
| 从团队中移除玩家 | `/bsbadmin team kick <player>` |
| 将岛屿交给另一个成员（所有者离开了服务器） | `/bsbadmin team setowner <player>` |
| 解散团队 | `/bsbadmin team disband <owner>` |
| 解散这个世界的每个团队 | `/bsbadmin team disbandall` |
| 让一个岛屿有更大的团队 | `/bsbadmin team maxsize <player> <size>` |
| 让一组玩家有更大的团队 | 给他们 `bskyblock.team.maxsize.<number>` |
| 让成员邀请其他玩家 | 所有者打开 `/island settings` → 命令等级 |
| 改变成员在岛屿上可以做什么 | 所有者打开 `/island settings`；管理员在游戏模式配置中设置默认值。参见[保护、标志和等级](../Island-Protection,-Flags-&-Ranks.md) |

## 自定义等级 { #custom-ranks }

你可以用 `/bentobox rank` 命令在内置等级之间添加等级：

```
/bentobox rank list
/bentobox rank add ranks.veteran 700
/bentobox rank remove ranks.veteran
```

该值决定了等级所处的位置。`700` 在成员（500）和副所有者（900）之间，所以提升成员会使他们变成老兵，再次提升会使他们变成副所有者。添加等级的显示名称到你的地区文件中你使用的引用下（这里是 `ranks.veteran`）。

## 故障排除 { #troubleshooting }

**"岛屿已满"但团队看起来很小。**
限制包括所有者。检查 `max-team-size`，以及所有者是否有 `team.maxsize` 权限。所有者必须登录一次以应用新权限。

**玩家无法被邀请。**
他们可能已经在一个团队中（他们必须首先离开），已经有待处理邀请，或在从该岛屿离开或被踢后处于邀请冷却中。

**合作玩家不断失去他们的等级。**
这就是合作的工作方式：当没有团队成员在线时结束。对于应该保留访问权限的玩家，改用信任。

**所有者想要离开。**
所有者不能离开。他们必须先用 `/island team setowner <player>` 将岛屿交给某人，或者管理员可以用 `/bsbadmin team setowner` 这样做。

**玩家利用团队加入/离开来复制物品或奖励。**
打开 `on-join` 和 `on-leave` 重置，设置 `leavers-lose-reset: true`，并保持邀请冷却。

## 另请参见 { #see-also }

- [保护、标志和等级](../Island-Protection,-Flags-&-Ranks.md)：每个等级在岛屿上可以做什么
- [岛屿](IslandManagement.md)：创建、重置和删除岛屿
- [多个岛屿](../ConcurrentIslands.md)
- [自定义菜单](../../Tutorials/generic/Customizable-GUI.md)：团队菜单是 `plugins/BentoBox/panels/team_panel.yml`
