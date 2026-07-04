# 岛屿管理

每个 BentoBox 游戏模式的核心是**岛屿** — 世界的一个受保护区域，属于玩家或团队。BentoBox 处理岛屿的完整生命周期，因此你不必手动管理任何内容。

## 创建岛屿

当玩家首次加入游戏模式并运行主命令时（例如 BSkyBlock 的 `/island`、AOneBlock 的 `/oneblock`），BentoBox 自动：

1. 在世界中为他们找到一个空闲的地方。
2. 从蓝图（已保存的岛屿模板）粘贴他们的**初始岛屿**。
3. 将他们传送到他们新岛屿的生成点。
4. 在数据库中将岛屿注册为他们的。

玩家在每个游戏模式中获得一个岛屿。如果你的服务器运行多个游戏模式（例如 BSkyBlock 和 AcidIsland），每个玩家在每个世界中都会获得一个独立的岛屿。

## 岛屿名称

玩家可以使用 `/island setname <name>` 给他们的岛屿起一个自定义名称。名称显示在各个地方 — 排行榜、Warps 插件和由其他插件显示的占位符。管理员可以通过游戏模式的 `config.yml` 限制允许的名称。

## 家园位置

玩家可以使用 `/island sethome` 在岛屿上设置多个家园位置。当他们使用 `/island go` 或 `/island home` 时，他们传送到家园点。多个命名家园可以通过权限解锁：

```
[gamemode].island.home.maxhomes.<number>
```

## 重置岛屿

玩家可以使用 `/island reset` 重置岛屿来重新开始。这会**删除当前岛屿**并创建一个全新的岛屿。管理员可以：

- 限制玩家可以重置的次数（在 `config.yml` 中设置）。
- 通过权限 `[gamemode].island.reset.maxresets.<number>` 授予额外重置。
- 将重置设置为无限制，值为 `-1`。

!!! warning
    岛屿重置是永久的。旧岛屿和在其上构建的一切都会被删除。建议玩家在重置前备份任何重要内容。

## 岛屿删除（管理员）

管理员可以使用以下方式删除玩家的岛屿：
```
/[admin_command] delete <player>
```

这将从数据库中移除岛屿并标记该区域以进行清理。玩家之后可以立即创建新岛屿。

自 BentoBox 3.16.1 起，实际的区域文件会在下一次例行清理时被回收（默认：24 小时），而不是立即回收。如果该岛屿与其他在用岛屿共享区域文件，被删除的区域将保留在原地，直到该区域不再包含其他岛屿。要强制立即清理，请在删除后运行 `/bbox admin purge deleted` — 仅当区域文件不再包含任何在用岛屿时才会删除方块。对于共享区域中的精确方块删除，请使用 WorldEdit 或手动移除方块。

## 非活跃岛屿清理

如果玩家放弃服务器，他们的岛屿保留在世界中。BentoBox 不会自动删除非活跃岛屿，但**删除标志**和外部工具可以用来管理它。许多服务器管理员通过设置重置限制并定期审查非活跃玩家来处理这个问题。

## 玩家离开团队时会发生什么

如果玩家是成员（不是所有者）并离开团队或被踢出，他们失去对该岛屿的访问。之后他们可以创建自己的岛屿，受任何重置限制的约束。如果玩家*是*所有者，他们必须在离开前转让所有权 — 他们不能简单地离开他们拥有的岛屿。

## 多个岛屿（并发岛屿）

默认情况下，每个玩家在每个游戏模式中拥有一个岛屿。BentoBox 可选地支持**并发岛屿** — 允许单个玩家同时拥有多个岛屿。这是在游戏模式的 `config.yml` 中配置并由权限控制的高级功能。

### 配置示例

有两个位置可以配置并发岛屿：

**1. BentoBox `config.yml`** — 为所有游戏模式设置全局默认值：

```yaml
island:
  # 玩家可能拥有的并发岛屿的默认数量。
  # 这可能会被各个游戏模式配置设置覆盖。
  concurrent-islands: 1
```

**2. 游戏模式 `config.yml`**（例如 BSkyBlock） — 覆盖该游戏模式的全局默认值：

```yaml
world:
  # 玩家在世界中可以拥有的并发岛屿的数量。
  # 值为 0 将使用 BentoBox config.yml 默认值。
  concurrent-islands: 1
  # 如果玩家在团队中，则禁止他们拥有其他岛屿。
  disallow-team-member-islands: true
```

例如，要让 BSkyBlock 中的每个玩家最多拥有 **3** 个岛屿，请在 BSkyBlock `config.yml` 中设置 `concurrent-islands: 3`。如果你还想让团队成员能够创建自己的岛屿，请设置 `disallow-team-member-islands: false`。

### 权限

可以使用权限节点覆盖每个玩家的最大值：

```
[gamemode].island.number.<number>
```

用游戏模式前缀替换 `[gamemode]`，用允许的最大岛屿数替换 `<number>`。例如：

| 权限 | 效果 |
|---|---|
| `bskyblock.island.number.5` | 允许玩家在 BSkyBlock 中拥有最多 5 个岛屿 |
| `acidisland.island.number.3` | 允许玩家在 AcidIsland 中拥有最多 3 个岛屿 |
| `caveblock.island.number.2` | 允许玩家在 CaveBlock 中拥有最多 2 个岛屿 |

权限值会覆盖该玩家的 `concurrent-islands` 配置值。如果玩家没有该权限，则使用配置值作为默认值。

!!! tip
    有关完整指南（包括玩家如何创建、导航和管理多个岛屿），请参阅[并发岛屿](../../BentoBox/ConcurrentIslands.md)页面。

## 岛屿范围和间距

岛屿放在网格中。岛屿中心之间的间距在 `config.yml`（`distance-between-islands`）中设置一次，**世界创建后无法更改**。在玩家开始加入前选择此值。较大的值提供岛屿之间更多的构建空间；较小的值使世界更加紧凑。

玩家的**保护范围** — 他们实际拥有并可以保护的区域 — 总是小于或等于岛屿间距的一半。它可以由管理员或玩家权限扩大到该最大值。

## 查看岛屿信息

玩家可以使用 `/island info` 检查自己的岛屿信息。管理员可以使用以下方式检查任何岛屿：
```
/[admin_command] info <player>
```
这显示岛屿的位置、所有者、团队成员和当前保护范围。

??? note "v3.16.1 新功能"
    **发布日期：** 2026-05-17

    针对 `/bbox admin delete` 的针对性补丁。完整发布说明请参阅：[Release 3.16.1](https://github.com/BentoBoxWorld/BentoBox/releases/tag/3.16.1)

    - 🔺 `/bbox admin delete` 现在真的会删除岛屿。回收会在下一次例行清理时进行（默认：24 小时），而不是立即；如果区域文件仍然包含其他在用岛屿，被删除的岛屿将保持已删除状态，直到该区域被清空。如果你需要立即清理共享区域，请使用 WorldEdit 或手动移除方块。
    - 🔺 不再创建种子世界（`<world>/bentobox`）。种子世界相关代码（`createSeedWorlds`、`removeSeedWorlds`、内存副本、磁盘文件夹）已被移除。如果存在早期版本残留的 `<world>/bentobox` 文件夹，可以安全地手动删除。
    - 🔺 API：`GameModeAddon#isUsesNewChunkGeneration()` 已被弃用并将被移除。现有的覆盖实现仍然可以工作（该值被忽略）但会发出弃用警告——请在方便时移除该覆盖。

    **兼容性：** Paper Minecraft 1.21.5 – 26.1.2，Java 21+。
