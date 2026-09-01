# 死亡箱

**死亡箱** 在玩家死亡时将其物品放入箱子，而不是将其丢掉——并且不像通用死亡箱插件，它知道岛屿在哪里。

由 [tastybento](https://github.com/tastybento) 创建和维护。

{{ addon_description("DeathChest") }}

## 为什么需要一个岛屿特定的死亡箱附属

一个常规死亡箱插件假设两件事：玩家在一个可以放置箱子的地方死亡，并且他们之后能回到它。在岛屿服务器上这两个假设都不成立。

- **虚空。** 一个从岛屿掉下来的玩家在空荡荡的空间死亡，通常在世界地板下面。没有块来建造墓碑，所以通常插件要么将箱子掉进虚空，要么放弃，要么将其放在基岩层，没人能到达。
- **海洋。** 在酸岛上，岛屿周围的空间是海洋。地面存在，但它在一百块下面，在水下——技术上有效的点，实际上一个丢失的箱子。
- **其他玩家的岛屿。** 一个访客死亡时无法在那里建造，通常无法破坏箱子，往往也无法打开它。
- **野生。** 岛屿之间的空间既没有保护也无法在不飞行的情况下到达。

这就是为什么通常的建议最终是"只打开 `keepInventory`"——有了那个，死亡停止重要。

死亡箱改为解决放置问题，所以死亡仍然可以付出代价而不付出一切。

## 箱子位置如何被选择

该附属通过三个阶段工作并在第一个成功时停止。

1. **玩家死亡的地方** ——但仅当他们死在他们是成员的岛屿的*受保护*部分，**并且** 有可到达的地面：一个自由块有扎根的东西，在 `chest.search-depth` 块之内，并且没有浸入水中。这是通常情况。你在你的岛屿上死亡，你的东西就在你死亡的地方。

2. **在他们自己的岛屿上** ——在他们的岛屿家点旁边。虚空死亡、海上死亡、岩浆死亡、访问他人时的死亡和野生死亡都在这里，也是玩家重生的地方。

3. **由附属持有** ——如果玩家根本没有岛屿，物品进入附属的数据库并通过 `/[player command] deathchest claim 1` 恢复。

!!! info "为什么'可到达的地面'是重要部分"
    需要可到达范围内的扎根地面，而不是任何扎根地面，是什么阻止箱子最后无用的地方。一个掉进虚空的玩家仍在他们岛屿的列内，所以无界下行搜索会很乐意找到基岩并将箱子留在那里。在海洋游戏模式中它会找到海床。未通过此检查不是错误——它是表示将箱子发送到第 2 阶段的信号，玩家可以实际走到那里。

## 安装

1. 将附属 jar 放入 `plugins/BentoBox/addons` 文件夹
2. 重启服务器（启用附属并生成 `config.yml` 文件）
3. 在 `config.yml` 中自定义设置（可选）
4. 运行 `/bentobox reload` 或重启服务器以应用新设置

!!! warning "当 `keepInventory` 开启时死亡箱不做任何事"
    如果 `keepInventory` 游戏规则保持玩家的库存，就没有掉落物品来存储，附属会让步。在你的游戏模式世界中关闭 `keepInventory` 如果你想要死亡箱来拯救玩家的物品。

## 指令

!!! tip
    `[player command]` 和 `[admin command]` 取决于你运行的游戏模式。
    游戏模式的 `config.yml` 包含设置让你改变它们。
    作为例子，在 BSkyBlock 上默认 `[player command]` 是 `island`，默认 `[admin command]` 是 `bsbadmin`。

### deathchest
**指令**：`/[player command] deathchest`
**别名**：`deaths`、`grave`
**描述**：列出你的死亡箱，最新优先，显示每个在哪里及它还剩多久。
**权限**：`[gamemode].deathchest`。默认：`true`。

由附属持有的箱子而不是在世界中放置的被显示为持有而不是坐标。

### deathchest claim {number}
**指令**：`/[player command] deathchest claim {number}`
**描述**：交出附属为那个箱子持有的物品，加上任何储存的经验。不适合玩家库存的物品被丢在他们的脚下。
**权限**：`[gamemode].deathchest`。默认：`true`。
**例子**：`/[player command] deathchest claim 1`

这是玩家恢复一个无法在世界中放置的箱子的方式。它也收集任何溢出——见 [物品如何被储存](#物品如何被储存)。

### deathchest tp {number}
**指令**：`/[player command] deathchest tp {number}`
**描述**：将玩家传送到那个死亡箱。
**权限**：`[gamemode].deathchest.teleport`。默认：`true`。
**例子**：`/[player command] deathchest tp 1`

需要 `commands.allow-teleport` 在 `config.yml` 中为 `true`。一个在世界中没有块的箱子无法被访问——声明它代替。

### admin deathchest
**指令**：`/[admin command] deathchest`
**描述**：报告服务器上存储了多少死亡箱。
**权限**：`[gamemode].admin.deathchest`。默认：`op`。

### admin deathchest {player}
**指令**：`/[admin command] deathchest {player}`
**别名**：`deathchests`
**描述**：列出玩家的死亡箱，显示箱子在哪里和他们在哪里死亡。那两个每当箱子被迁移到岛屿时不同，这使得很容易看到虚空或海上死亡一眼。
**权限**：`[gamemode].admin.deathchest`。默认：`op`。
**例子**：`/[admin command] deathchest tastybento`

### admin deathchest purge
**指令**：`/[admin command] deathchest purge`
**描述**：立即过期每个已经逾期的箱子，而不是等待下一个检查。
**权限**：`[gamemode].admin.deathchest`。默认：`op`。

!!! tip
    `[gamemode]` 是一个前缀，取决于你运行的游戏模式。
    前缀是游戏模式的小写名称，即如果你使用 BSkyBlock，前缀是 `bskyblock`。
    类似地，如果你使用酸岛，前缀是 `acidisland`。

## 权限

| 权限 | 默认 | 描述 |
|------|------|------|
| `[gamemode].deathchest` | `true` | 使用 `/[player command] deathchest` 列出箱子和声明持有的物品 |
| `[gamemode].deathchest.teleport` | `true` | 使用 `/[player command] deathchest tp {number}` |
| `[gamemode].admin.deathchest` | `op` | 使用管理指令 |

## 物品如何被储存

箱子块持有物品。玩家库存是 41 个格子包括盔甲和副手，箱子是 27，所以**溢出是正常的而不是罕见**。

任何不适合的被附属保持并在玩家每次关闭箱子时自动移入箱子。所以玩家清空箱子，关闭它，下一个物品出现——直到什么都没有剩下。一旦箱子和附属的储存都是空的，箱子块消失及其记录。

如果箱子块消失是为了附属没有导致的原因——一个世界编辑、一个回滚、手动 `/setblock`——记录存活并变成一个持有的箱子，可以通过 `deathchest claim` 恢复。

## 保护

只有所有者可以打开或破坏他们自己的死亡箱。任何其他人被拒绝并被告知它是谁的箱子。

- `chest.team-access` 将那扩展到岛屿团队成员，但仅当箱子坐在一个所有者和其他玩家都属于的岛屿上。
- `chest.protect-from-explosions` 让死亡箱远离爬虫、TNT 和床炸药块列表。
- 记录被删除当岛屿被重置或删除时，因为块即将被擦除及其一起。

!!! warning "漏斗没有被阻止"
    一个死亡箱下面的漏斗会排干它。箱子在所有者自己的岛屿上，所以这是自我造成的而不是骚扰，但如果你的玩家在他们岛屿家点附近建造分类系统值得知道。追踪为 [问题 #5](https://github.com/BentoBoxWorld/DeathChest/issues/5)。

## 配置

`config.yml` 文件包含下面的设置。显示的值是默认值。

### 禁用游戏模式
死亡箱在 BentoBox 服务器上的所有游戏模式世界中默认运行。
你可以通过在以 `-` 开始的新行上写其名称来禁用一个游戏模式。

禁用 BSkyBlock 的例子：

```yml
disabled-gamemodes:
  - BSkyBlock
```

默认值：

```yml
disabled-gamemodes: []
```

### 箱子材料
用于死亡箱的块。

`CHEST` 是经典外观。`BARREL` 对拥挤的岛屿是一个好选择，因为即使有一个块直接在其上面也可以打开。

材料必须是一个容器。如果不是——或如果名称不是一个真实的材料——附属记录一个错误并回到为玩家持有物品。

```yml
chest:
  material: CHEST
```

### 在死亡位置放置
如果那是一个他们可以到达并在其中建造的地方，在玩家死亡的地方放置箱子。

设置为 `false` 以总是将箱子发送到岛屿家点代替。

虚空死亡、在建造允许区域外、或在不可到达的地点的死亡无论此设置如何都回到岛屿家点。

```yml
chest:
  place-at-death-location: true
```

### 搜索半径
有多远要**横向**看，以块为单位，找一个自由地点来放置箱子。范围 1 到 32。

```yml
chest:
  search-radius: 8
```

### 搜索深度
有多远要**向下**看，以块为单位，找地面来站箱子。范围 1 到 64。

这是什么阻止箱子最后玩家远下方——在一个海洋世界的海床，或埋在地形中。如果在这个距离内没有地面找到箱子进入玩家的岛屿代替，这通常是你想要的。

提升它让箱子跟随长下降到地面；降低它发送更多死亡到岛屿。

```yml
chest:
  search-depth: 16
```

### 过期分钟
死亡箱在过期前持续多少分钟。`0` 表示永不。

```yml
chest:
  expiry-minutes: 60
```

### 过期操作
当死亡箱过期时会发生什么。

- `DROP`——破坏箱子并让物品掉在地上。他们会像任何其他掉落物品一样消失。
- `DELETE`——删除箱子及其内容。

```yml
chest:
  expiry-action: DROP
```

### 过期检查秒数
多久（以秒为单位）检查一次过期的箱子。最小 5。

```yml
chest:
  expiry-check-seconds: 60
```

### 每个玩家最大
一个玩家一次可能拥有的最大死亡箱数。当超过时，玩家最旧的箱子被早期过期，遵循上面的 `expiry-action`。`0` 表示无限。

这阻止一个一直死亡的玩家用箱子乱扔他们的岛屿。

```yml
chest:
  max-per-player: 3
```

### 团队访问
让岛屿团队成员打开彼此的死亡箱。

设置为 `false` 如果只有所有者应该打开他们自己的箱子。

```yml
chest:
  team-access: true
```

### 保护免于爆炸
阻止死亡箱被爬虫、TNT 等炸飞。

```yml
chest:
  protect-from-explosions: true
```

### 储存经验
与箱子一起储存玩家的掉落经验并在它被打开时交还。

```yml
experience:
  store: true
```

### 经验百分比
玩家掉落经验的百分比来储存，0 到 100。剩余的丢失，这让死亡保持一些成本。

仅适用当 `experience.store` 是 `true`。

```yml
experience:
  percent: 100
```

### 死亡时通知
告诉玩家他们的死亡箱在哪里当他们死亡时，及它会持续多久。

消息使用游戏模式的友好名称来命名世界，在死亡不在主世界时添加 `Nether` 或 `The End`。

```yml
notify:
  on-death: true
```

### 允许传送
允许 `/[player command] deathchest tp {number}` 将玩家传送到他们的箱子。

玩家仍然需要 `[gamemode].deathchest.teleport` 权限。

```yml
commands:
  allow-teleport: true
```

## 翻译

{{ translations("DeathChest") }}

## 来源
想要贡献？见此文档的源代码在 [GitHub](https://github.com/BentoBoxWorld/docs/blob/master/docs/addons/DeathChest/)。
