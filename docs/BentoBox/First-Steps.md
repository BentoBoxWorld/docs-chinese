# BentoBox 前 30 分钟

你已经安装了 BentoBox 和游戏模式插件，接下来该做什么？本指南将带你逐步检查并完成向玩家开放服务器前的所有准备工作。

---

## 第 1 步 — 确认所有内容已加载

启动你的服务器并查看控制台中是否有任何错误消息。然后运行：

```
/bentobox version
```

你应该看到 BentoBox 的版本号，然后是每个已加载的插件及其版本的列表。如果你的游戏模式插件出现在此列表中，BentoBox 已找到并正确加载它。

!!! warning "如果列表中缺少插件"
    检查 `.jar` 文件是否在 `plugins/BentoBox/addons/` 中，**而不是**在 `plugins/` 中。然后检查控制台是否有启动期间的任何错误消息。常见原因是版本不匹配或缺少依赖项。

---

## 第 2 步 — 以玩家身份测试岛屿创建

以普通玩家身份加入你的服务器（使用备用账户或请朋友帮忙），运行游戏模式的主玩家命令。以 BSkyBlock 为例：

```
/island
```

系统应该自动创建一个新岛屿并将你传送过去。如果成功，说明核心配置没有问题。

在岛屿上试试以下操作：

- 破坏一个方块 ✅ （应该有效 — 它是你的岛屿）
- 放置一个方块 ✅
- 检查你的岛屿信息：`/island info`

---

## 第 3 步 — 测试保护

在你的岛屿上，邀请另一个玩家（或使用备用账户）前来访问。作为访客，他们应该**无法**：

- 破坏方块
- 打开箱子
- 与大多数对象交互

如果访客可以破坏方块，请检查岛屿的保护标志。岛屿所有者使用以下方式打开设置 GUI：
```
/island settings
```

作为管理员，你可以使用以下方式打开世界设置：
```
/[admin_command] settings
```

---

## 第 4 步 — 审查关键配置设置

在玩家进入前，打开游戏模式的 `config.yml`（位于 `plugins/BentoBox/addons/[GameMode]/`）并检查以下设置：

| 设置 | 控制内容 | 建议 |
|---|---|---|
| `distance-between-islands` | 岛屿中心之间的间距 | 在创建任何岛屿**前**设置此值 — 之后无法更改 |
| `island-protection-range` | 默认保护半径 | 应该小于上面距离的一半 |
| `reset-limit` | 玩家可以重置岛屿的次数 | `-1` 为无限制，或像 `3` 这样的数字 |
| `max-team-size` | 每个岛屿团队的最大玩家数 | `4` 是默认值；增加以实现更多合作游戏 |
| `allow-new-islands` | 玩家是否可以创建新岛屿 | 应该是 `true` |

!!! warning "岛屿距离之后无法更改"
    一旦创建了任何岛屿，更改 `distance-between-islands` 将导致 BentoBox 拒绝启动。选择你的值并在向玩家开放前设置它。默认值（400 个方块半径 = 800 个方块中心间距）对大多数服务器都有效。

---

## 第 5 步 — 设置权限

BentoBox 使用你服务器的权限插件（如 LuckPerms）来控制玩家可以做什么。至少，请确保你的默认玩家组拥有：

```
[gamemode].island.create       # 创建岛屿
[gamemode].island.home         # 传送到他们的岛屿
[gamemode].island.settings     # 打开岛屿设置 GUI
[gamemode].island.team         # 使用团队命令
```

用游戏模式的前缀替换 `[gamemode]`（例如 `bskyblock`、`acidisland`、`oneblock`）。

要查看完整的权限列表，请运行：
```
/bentobox perms
```

---

## 第 6 步 — 安装推荐的插件

裸露的 BentoBox 游戏模式有效，但玩家会期望一些额外功能。在打开前考虑添加这些：

- **Warps** — 玩家可以在他们的岛屿上创建传送点标志，以便其他人可以轻松访问
- **Level** — 计算岛屿分数并显示排行榜；给玩家一些要努力的目标
- **Challenges** — 为玩家提供任务和奖励；显著改善保留率
- **InvSwitcher** — 如果你运行多个游戏模式，是必需的；保持库存分离

从 [github.com/BentoBoxWorld](https://github.com/BentoBoxWorld) 下载插件，将 `.jar` 放在 `plugins/BentoBox/addons/`，并重启服务器。

---

## 第 7 步 — 自定义你的初始岛屿（可选）

默认初始岛屿可以正常使用，但比较通用。如果想让服务器更有特色，可以构建一个自定义初始岛屿并保存为蓝图。

快速步骤：
1. 在世界某处建造你想要的岛屿
2. 用 `/[admin_command] blueprint pos1` 和 `pos2` 框选范围
3. 执行 `/[admin_command] blueprint copy`，然后 `save myisland`
4. 用 `/[admin_command] blueprint` 管理蓝图包

有关完整演示，请参阅[蓝图](About/BlueprintsSummary.md)。

---

## 第 8 步 — 向玩家开放

一切就绪！正式公开前，最后确认以下几点：

- [ ] 测试新玩家可以无错误地创建岛屿
- [ ] 确认保护有效（访客不能破坏）
- [ ] 确认游戏模式出现在 `/bentobox version`
- [ ] 阅读[常见问题解答](../FAQ.md)了解常见陷阱

---

## 获取帮助

如果有些东西不起作用：

1. 运行 `/bentobox version` 并复制输出
2. 检查控制台是否有错误消息
3. 搜索[常见问题解答](../FAQ.md)
4. 在[BentoBox Discord](https://discord.bentobox.world) 上提问 — 包括你的 `/bentobox version` 输出和控制台错误
5. 在[github.com/BentoBoxWorld/BentoBox/issues](https://github.com/BentoBoxWorld/BentoBox/issues) 报告 bug
