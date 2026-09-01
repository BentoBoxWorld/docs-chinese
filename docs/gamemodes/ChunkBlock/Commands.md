# ChunkBlock 命令

默认玩家命令是 **`/ch`**（别名 `/chunkblock`），默认管理员命令是 **`/chadmin`**（别名 `/chunkblockadmin`、`/cha`）。两者和一些子命令标签在 `config.yml` 中的 `chunkblock.command` 下配置：

```yaml
chunkblock:
  command:
    island: ch chunkblock
    admin: chadmin chunkblockadmin cha
    # 在玩家最初的 `/ch` 运行的子命令
    new-player-action: create
    # 在之后的每一个裸 `/ch` 运行的子命令
    default-action: go
    count-command: count
    phases-command: phases
    set-count-command: setCount
    bossbar-command: bossbar
    actionbar-command: actionbar
    respawn-block-command: respawnBlock check
```

裸 `/ch` 第一次创建岛屿和之后传送玩家回家。

!!! note "为什么 `/ch` 而不是 `/cb`"
    ChunkBlock 的默认值在 1.0.0 中是 `/cb` 和 `/cbadmin`，与 CaveBlock 碰撞。从 1.0.1 开始新安装获得 `/ch` 和 `/chadmin`。已经有一个 `config.yml` 的服务器保留它内部的任何别名。

## ChunkBlock 玩家命令

这些是 ChunkBlock 特有的子命令。其他一切——`go`、`create`、`reset`、`sethome`、`team`、`ban`、`expel`、`settings`、`language`、`info`、`near` 和其他——是标准 BentoBox 游戏模式集。

| 命令 | 描述 | 权限 |
|---------|-------------|------------|
| `/ch chunks` | 你的解锁区块数、最大值、可花费的等级信用，以及你领地的彩色聊天地图，显示你可以声称哪些区块。 | `chunkblock.island.chunks` |
| `/ch count` | 岛屿的当前魔法方块数和阶段。 | `chunkblock.count` |
| `/ch phases` | 打开阶段 GUI ——浏览阶段，使用权限，重放一个已经到达的。默认关闭。 | `chunkblock.phases` |
| `/ch setcount <number>` | 跳转方块数到一个以前完成的阶段的开始值。受 `set-count-cooldown`（默认 5 分钟）的限制。 | `chunkblock.island.setcount` |
| `/ch check`（别名 `respawnBlock`） | 显示魔法方块的粒子，或如果它消失了重生它。 | `chunkblock.respawn-block` |
| `/ch bossbar` | 切换阶段进度 BOSS 栏。需要配置中的 `bossbar: true`。 | `chunkblock.island.bossbar` |
| `/ch actionbar` | 切换阶段进度动作栏。需要配置中的 `actionbar: true`。 | `chunkblock.island.actionbar` |

## ChunkBlock 管理员命令

`/chadmin` 进行完整的标准 BentoBox 管理集（`version`、`tp`、`info`、`getrank`、`setrank`、`range`、`resets`、`deaths`、`purge`、`blueprint`、`register`、`delete`、`settings`、`reload`、`why`、`switch`、`team` 等等）加上下面的 ChunkBlock 特有命令。

| 命令 | 描述 | 权限 |
|---------|-------------|------------|
| `/chadmin chunks <player>` | 显示玩家的解锁区块数、他们的有效最大值、他们花费的等级和他们剩余的信用。 | `chunkblock.admin.chunks` |
| `/chadmin chunks <player> reset` | 重新锁定一切回到中心区块并清除花费记录。建筑完好无损——领地必须被重新赚取。 | `chunkblock.admin.chunks` |
| `/chadmin bypass` | 为自己切换区块锁定实施。当绕过时你可以移动通过被锁定的区块，边界幕布对你隐藏。 | `chunkblock.mod.bypasschunks` |
| `/chadmin setcount <player> <number> [lifetime]` | 设置玩家的魔法方块数，或他们的终身数。 | `chunkblock.admin.setcount` |
| `/chadmin setchest <phase> <rarity>` | 将你正在看的箱子保存到一个阶段的箱子文件带给定稀有性（`COMMON`、`UNCOMMON`、`RARE`、`EPIC`）。箱子必须是一个填充的单个箱子。 | `chunkblock.admin.setchest` |
| `/chadmin sanity [<phase>]` | 打印阶段概率的清理检查到控制台。 | `chunkblock.admin.sanity` |
| `/chadmin phases` | 打开阶段顺序编辑器——重新排序、调整大小、启用和禁用阶段。 | `chunkblock.admin.phases` |

!!! tip "` /chadmin bypass` 需要运维人员没有的权限"
    `chunkblock.mod.bypasschunks` 默认为 `false`，所以即使一个 op 在命令工作前必须明确授予它。那是故意的：员工在他们选择加入前遵循同样的规则。旁观者模式不管怎样总是豁免的。

!!! tip "使用阶段顺序编辑器"
    `/chadmin phases` 按顺序列出每个阶段有它的计算开始方块、长度和状态，并写 `phases_index.yml`。

    - **左键单击** 拿起一个阶段；点击它应该去或放在结束插槽来放置它。点击其他地方或关闭面板来不保存就放它回去。
    - **右键单击** 切换一个阶段打开或关闭。
    - **Shift-左键单击** 通过聊天提示设置一个阶段的长度。第一次长度编辑写 `adminLengths: true` 到索引所以你的长度永不被重新计算。

    禁用的阶段显示为灰色玻璃，版本锁定的为屏障；两者仍然可以被重新排序。见 [阶段](Phases.md) 对于完整的图景。

## 读取 `/ch chunks`

```
区块：9/441。信用：3 等级(s) ——一个区块花费 1。
你的岛屿领地（9/441 个区块）：
□ □ □ □ □
□ ▣ ▣ ▣ □
□ ▣ ■ ■ ▣
□ ▣ ■ ◆ ▣
□ □ ▣ ▣ □
■ 你的  ▣ 可声称（每个 1 等级(s)）  □ 被锁定
```

| 字形 | 含义 |
|---|---|
| `■` 绿色 | 一个你拥有的区块 |
| `▣` 黄色 | 现在可声称——相邻、在范围内、在限制之下 |
| `□` 灰色 | 被锁定，还不可声称 |
| `◆` 蓝色 | 你站在的区块 |

地图随着岛屿增长宽，到一个 15 × 15 视图。
