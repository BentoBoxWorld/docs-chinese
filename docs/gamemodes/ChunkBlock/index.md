# ChunkBlock

一个魔法方块。一个区块。一堵你无法穿过的墙。

**ChunkBlock** 采用了每个人都知道的 OneBlock 循环——挖魔法方块，它会变成其他东西，阶段不断推进——并在 16 个方块之外设置了一个硬边界。你的起始区块之外的一切都是禁区：你不能行走、飞行、滑翔、珍珠、骑乘或挖掘进入其中。唯一的出路是变得 *更富有*。

岛屿等级是货币。提升你的等级，走到那面墙，然后 **朝你想要扩张的方向击打它**。另一侧的区块打开，边界向外移动一步。失去等级，墙就会重新出现——最新的区块先——直到你重新赚回那些等级。

由 [tastybento](https://github.com/tastybento) 创建和维护。魔法方块引擎来自 [AOneBlock](../AOneBlock/index.md)，所以阶段文件是可互换的；区块管制是 ChunkBlock 特有的。

{{ addon_description("ChunkBlock") }}

## 为什么玩家会上瘾

- 🔒 **一堵你真的无法穿过的边界。** 行走、冲刺跳跃、鞘翅、三叉戟撤退、末影珍珠（退款）、唱诗台果实、马匹、船、矿车和创意模式飞行都被限制——在 *每一个* 高度，从虚空到建筑高度以上。没有飞过的走廊，也没有挖下去的通道。
- 💰 **等级就是领地。** 不是商店，不是排名，不是计时器。你的玩家已经优化的东西——岛屿等级——正是购买空间的东西。每放置的方块都是下一个区块的首付。
- 👊 **扩张是一个物理的姿态。** 没有 GUI，没有 `/buy chunk`。岛屿所有者站在墙边，挥一拳，世界就会伴随着声音和绿色粒子扫过打开。他们选择方向，所以没有两个岛屿以相同方式生长。
- ⚠️ **失去有代价——但不是残忍的。** 等级下降会按照完全相反的顺序重新锁定最近声称的区块。内部没有任何东西被触及：建筑、箱子、生物都在等级回来时还在那里。想要更温和的游戏？一行配置就能让领地成为从不收缩的棘轮。
- 🗺️ **你能看到前沿。** 每个玩家都能在靠近你的每个被锁定的面上看到粒子幕布（可选的客户端屏障方块），`/ch chunks` 会打印你拥有什么、你下一步能声称什么、以及要花多少费用的彩色地图。
- 🧱 **没有什么会跨越边界泄露。** 活塞、流动液体、发射器、树木生长、火焰和草蔓延、爆炸和自然生物生成都会停在那条线上，掉落的物品会反弹而不是丢失到禁区。
- ⛏️ **下面是完整的 OneBlock 游戏。** 20 个主题阶段，15,500 个方块的内容，加权方块和生物群系，稀有宝箱，全息图，BOSS 栏和动作栏进度——所有的一切，都在一个会长大的盒子里。

## 一次会话的感受

你出生在荒芜虚空中间的草块上，四面八方都是红墙。挖。再挖。圆石、泥土、一只立即走到边缘的鸡。在第五十个方块左右，聊天会说你有信用，所以你转身面向日出方向，挥拳攻击墙，它就 *消失了*——你一秒钟前拥有的世界的两倍大，现在你实际上可以建造小麦农场而不用敲到自己的塔。

五十个等级后，你的岛屿是一个 3×3 的区块方块，你在有意选择方向：海洋阶段即将到来，你想在东侧有空间，那里有落差。然后你在地牢阶段死得很惨，失去了一个区块价值的等级，最新的区块随着你的熔炉银行一起关闭。它没有消失。它只是 *在墙后面*，直到你重新赚回那些等级。

## 设置

!!! warning "需要 Level 附属插件"
    岛屿等级是唯一的区块货币，所以 ChunkBlock 没有 Level 是无法运行的。如果 Level 缺失，ChunkBlock 会自己禁用，并在控制台中显示清晰的消息而不是半启动。

0. 安装 BentoBox 并运行一次服务器以创建其文件夹。
1. 将 **Level** 附属插件安装到 `plugins/BentoBox/addons/`。
2. 将 **ChunkBlock** jar 放入 `plugins/BentoBox/addons/` 并重启。
3. ChunkBlock 创建 `chunkblock_world`、数据文件夹、`config.yml`、`phases` 文件夹和 `phases_index.yml`。
4. 停止服务器，编辑 `config.yml` 满足你的需要，并删除它创建的任何世界（如果你的更改影响生成）。
5. 重启。

ChunkBlock 与 AOneBlock、CaveBlock 和其他的并行运行得很好——自己的世界、命令（`/ch`、`/chadmin`）、权限（`chunkblock.*`）、标志和数据库表。

!!! tip "推荐的伴侣"
    - **Level** ——必需的，值得调整：它的死亡惩罚和方块值，在 ChunkBlock 中，是 *领地* 设置。
    - **Border** ——兼容。它绘制岛屿的整体保护限制；内部区块前沿是 ChunkBlock 自己的幕布。
    - **InvSwitcher** ——让库存与其他游戏模式分开。
    - 挑战、传送点、好评、生物群落、温室和朋友都在解锁的区块内照常工作。

## 兼容性

| 特性 | 支持 |
|---|---|
| 服务器 | ✅ Paper / Spigot，Minecraft 1.21+ |
| BentoBox 版本 | ✅ 3.13.0 或更高版本 |
| Java 版本 | ✅ Java 21 |
| Level 附属插件 | ⚠️ 必需——岛屿等级是区块货币 |
| 下界 / 末地 | ⚪ 默认关闭生成；见下文 |

## 配置

`config.yml` 是标准的 BentoBox 游戏模式文件加上一个仅限 ChunkBlock 的块。每个选项都在文件本身中有注释；最新的副本位于 [config.yml](https://github.com/BentoBoxWorld/ChunkBlock/blob/develop/src/main/resources/config.yml)。

### 区块设置

```yaml
chunkblock:
  # 一个区块要花多少岛屿等级来声称。最小值 1。
  levels-per-chunk: 1
  # 一个岛屿可以声称的最大区块数，包括中心区块。
  # 441 是一个完整的 21 x 21 区块方形。-1 表示"保护范围内的任何东西"。
  max-chunks: 441
  # 失去等级低于已花费的等级会重新锁定区块，最新的在前。
  # false = '棘轮模式'：区块一旦声称就永不重新锁定。
  relock-on-level-loss: true
  # 在重新锁定它们脚下的玩家移出一个区块。
  eject-players-on-relock: true
  # 在被锁定的区块内取消自然生物生成。
  deny-mob-spawns-in-locked: true
  # 在边界处反弹掉落的物品而不是丢失它们。
  bounce-back-items: true
  border:
    # 在被锁定区块面上的每个玩家粒子幕布。
    show-particles: true
    particle-color:
      ==: Color
      ALPHA: 255
      RED: 255
      GREEN: 0
      BLUE: 0
    # 也发送客户端屏障方块。纯粹视觉效果；世界永远不会被修改。
    client-side-barrier-blocks: false
```

!!! abstract "完整指南：[声称区块](Chunks.md)"
    每个设置对游戏感觉的影响，工作的信用示例，重新锁定规则，以及如何调整一个休闲或硬核服务器的节奏。

### 世界设置更加重要

=== "distance-between-islands"
    !!! summary "必须是 8 的倍数"
        岛屿中心必须位于区块中心（x ≡ 8, z ≡ 8），否则魔法方块会坐在区块接缝上。ChunkBlock 在加载时将此值捕捉到最近的 8 的倍数，所以手工编辑的 `250` 悄悄变成 `248`。默认值是 `256`。

=== "protection-range"
    !!! summary "第二个硬大小上限"
        声称的区块必须完全适应岛屿的保护范围内，所以范围对领地有上限，不管 `max-chunks` 说什么。最大的环半径是 `(protection-range − 8) ÷ 16`，向下舍入，给出 `(2r + 1)²` 个区块。

        使用默认值——`protection-range: 240`——这是一个半径 14 或 841 个区块的，所以 `max-chunks: 441` 是实际限制的设置。如果你提高 `max-chunks`，检查范围是否容纳它，并记住范围永远不能超过 `distance-between-islands`。

=== "offset-x / offset-z"
    !!! summary "故意缺失"
        其他游戏模式暴露世界偏移量。ChunkBlock 从 `start-x`/`start-z` 内部计算它们，所以魔法方块总是区块中心，并根本不提供设置。

=== "nether and end"
    !!! summary "默认关闭"
        `nether.generate` 和 `end.generate` 都默认为 `false`。打开其中任何一个，该维度就会获得自己的中心区块和相同的声称规则，由同一个岛屿等级驱动。魔法方块只存在于主世界。

### 阶段

魔法方块、阶段文件和 `phases_index.yml` 的行为与 AOneBlock 中的完全相同——格式是字节级兼容的，所以社区阶段包直接放入即可。

!!! abstract "完整指南：[魔法方块和阶段](Phases.md)"
    发货的 20 个阶段进度、阶段索引、管理阶段编辑器，以及在哪里找到完整的字段参考。

### 可定制的 GUI

ChunkBlock 使用 BentoBox 模板化面板 API 来处理其阶段 GUI。首次运行时，它会在 `plugins/BentoBox/addons/ChunkBlock` 下创建一个 `panels` 文件夹，其中包含 `phases_panel.yml`。有关机制，请参阅 [可定制的 GUI](../../Tutorials/generic/Customizable-GUI.md)；`PREVIOUS`、`NEXT` 和 `PHASE` 按钮类型按照 [AOneBlock 文档](../AOneBlock/index.md#customizable-guis) 中的描述工作。

## 命令

!!! tip
    默认玩家命令是 `/ch`（别名 `/chunkblock`），默认管理员命令是 `/chadmin`（别名 `/chunkblockadmin`、`/cha`）。两者都可在 `config.yml` 中的 `chunkblock.command` 下配置。

=== "ChunkBlock 特有的玩家命令"
    - `/ch chunks` ——你的区块数、可花费的信用和你领地的聊天地图。
    - `/ch count` ——当前魔法方块数和阶段。
    - `/ch phases` ——阶段 GUI。
    - `/ch setcount <number>` ——重放你已经到达的阶段。
    - `/ch check` ——重生魔法方块或显示其粒子。
    - `/ch bossbar` / `/ch actionbar` ——切换阶段进度显示。

=== "ChunkBlock 特有的管理员命令"
    - `/chadmin chunks <player> [reset]` ——检查玩家的区块、花费和信用，或将其重新锁定回中心区块。
    - `/chadmin bypass` ——为自己切换区块锁定实施。
    - `/chadmin setcount <player> <number> [lifetime]` ——设置玩家的方块数。
    - `/chadmin setchest <phase> <rarity>` ——将你正在看的箱子保存到一个阶段。
    - `/chadmin sanity [<phase>]` ——检查控制台中的阶段概率。
    - `/chadmin phases` ——阶段顺序编辑器。

[完整 ChunkBlock 命令列表](Commands.md)

## 权限

!!! tip
    每个 ChunkBlock 权限都有前缀 `chunkblock.`。

!!! warning "`chunkblock.mod.bypasschunks` 不会授予运维人员"
    区块锁定绕过默认为 `false` ——**不是** `op` ——所以员工在你明确授予它之前遵循与每个人相同的规则。这是故意与 BentoBox 的 `chunkblock.mod.bypasslock` 分开的，后者绕过岛屿 *lock* 并且是一个不同的特性。

=== "玩家权限"
    - `chunkblock.island.chunks` ——使用 `/ch chunks`。默认 `true`。
    - `chunkblock.count` ——使用 `/ch count`。默认 `true`。
    - `chunkblock.phases` ——使用 `/ch phases`。默认 `false`。
    - `chunkblock.island.setcount` ——使用 `/ch setcount`。默认 OP。
    - `chunkblock.respawn-block` ——使用 `/ch check`。默认 `true`。
    - `chunkblock.island.bossbar` / `chunkblock.island.actionbar` ——切换进度显示。默认 `true`。

=== "管理员权限"
    - `chunkblock.admin.chunks` ——使用 `/chadmin chunks`。默认 OP。
    - `chunkblock.mod.bypasschunks` ——豁免区块锁定，并使用 `/chadmin bypass`。**默认 `false`。**
    - `chunkblock.admin.setcount`、`chunkblock.admin.setchest`、`chunkblock.admin.sanity`、`chunkblock.admin.phases` ——默认 OP。

[完整 ChunkBlock 权限列表](Permissions.md)

## 标志

ChunkBlock 注册自己的标志 ID，所以它可以与 AOneBlock 并行运行，而两个附属插件都不会因为重复注册而失去标志。

| 标志 | 类型 | 描述 | 默认 |
|---|---|---|---|
| `CHUNKBLOCK_START_SAFETY` | 世界设置 | 玩家在创建岛屿后短时间内不能移动，所以他们不能立即掉下去。持续时间是配置中的 `starting-safety-duration`。 | false |
| `CHUNKBLOCK_BOSSBAR` | 岛屿设置 | 显示阶段进度 BOSS 栏。仅在配置中 `bossbar: true` 时可用。 | true |
| `CHUNKBLOCK_ACTIONBAR` | 岛屿设置 | 显示阶段进度动作栏。仅在配置中 `actionbar: true` 时可用。 | true |
| `MAGIC_BLOCK` | 保护 | 破坏魔法方块所需的最低岛屿排名。 | COOP |

!!! warning "从 1.0.0 升级"
    这些标志在 1.0.0 中被称为 `START_SAFETY`、`ONEBLOCK_BOSSBAR` 和 `ONEBLOCK_ACTIONBAR`。如果你从默认值改变了任何标志，升级后重新应用一次设置——旧值不再被读取。

## 占位符

除了从魔法方块引擎继承的阶段占位符外，ChunkBlock 还添加了五个领地占位符：

| 占位符 | 描述 |
|---|---|
| `%chunkblock_island_chunks%` | 解锁区块数，包括中心区块 |
| `%chunkblock_island_max_chunks%` | 此岛屿最多可声称的区块 |
| `%chunkblock_island_chunk_credit%` | 现在可花费的等级信用 |
| `%chunkblock_island_next_chunk_level%` | 满足下一个区块所需的总岛屿等级 |
| `%chunkblock_island_ring%` | 最远声称区块的环号 |

[完整 ChunkBlock 占位符列表](Placeholders.md)

## 常见问题

??? question "为什么我不能走过发光的红墙？"
    那个区块仍然被锁定。如果你是岛屿所有者并且你有等级信用，击打墙，它就会打开。`/ch chunks` 显示你的信用和什么是可以声称的。

??? question "团队成员可以声称区块吗？"
    不——声称是岛屿所有者的决定。团队中的每个人都会从空间中受益，看到信用公告并可以使用 `/ch chunks`，但只有所有者对边界的挥拳花费等级。

??? question "我失去了等级，现在我的农场在墙后面。它消失了吗？"
    不。重新锁定的区块内没有任何东西被触及——方块、箱子和生物完全在你离开它们的地方。重新获得等级并再次声称它；重新锁定总是最先取走最新的区块，所以你按照你失去它们的顺序把它们夺回来。管理员可以使用 `relock-on-level-loss: false` 完全禁用重新锁定。

??? question "当我站在一个区块中时，它重新锁定了。我会发生什么？"
    你被移至自己岛屿内最近的解锁点——飞行状态保留，摔伤取消，如果该点不安全，则在你下方创建一个落地块。没有人会被搁浅或坠入虚空。不属于该岛屿的玩家被送到自己的岛屿家代替。

??? question "我如何更快地获得更多区块？"
    提高你的岛屿等级：放置更多、更有价值的方块。如果你想让扩张感觉慷慨，降低 `levels-per-chunk`，或如果你想让地图打开缓慢，提高它。

??? question "我可以对角线声称吗？"
    不直接。新区块必须与你已经拥有的领地分享一个 **面**，所以一个角区块需要其两个邻近中的一个先被声称。

??? question "一个岛屿能有多大？"
    较小的：`max-chunks`（默认 441，一个 21×21 的方形）或最大的区块方形适应岛屿的保护范围。`/ch chunks` 显示有效的最大值。

??? question "为什么我一直摔倒死亡？"
    一个区块在开始时不是很多空间。在向上建造之前向外建造——并记住死亡可以花费等级，等级是领地。

??? question "有哪些阶段？"
    与 AOneBlock 相同的进度：平原、地下、冬天、海洋、丛林、沼泽、地牢、沙漠、下界、plenty、荒凉、深黑、末地、郁郁葱葱的洞穴、滴石洞穴、红树林沼泽、草地、樱桃林、崎岖的山峰和硫磺洞穴。见 [阶段](Phases.md)。

??? question "有下界或末地吗？"
    两者默认关闭。在 `config.yml` 中启用它们，每个都会获得自己的中心区块和相同的声称规则。魔法方块只存在于主世界。

??? question "我需要 Border 附属插件吗？"
    不，你也不需要删除它。Border 绘制岛屿的外部保护限制；ChunkBlock 在它内部绘制区块前沿。它们显示不同的东西并共存得很好。

??? question "我有一个 bug 或一个特性想法。我把它放在哪里？"
    在 [issue tracker](https://github.com/BentoBoxWorld/ChunkBlock/issues)。

## 翻译

{{ translations("ChunkBlock") }}

## API

ChunkBlock 将其数据存储在自己的数据库表 `ChunkBlockIslands` 中，并通过事件、请求处理程序和附属插件类公开其领地状态。

将其添加到你的项目作为提供的依赖项：

```xml
<dependency>
    <groupId>world.bentobox</groupId>
    <artifactId>chunkblock</artifactId>
    <version>1.0.1</version>
    <scope>provided</scope>
</dependency>
```

### 数据对象

=== "OneBlockIslands"
    !!! summary "描述"
        每岛屿状态：从 AOneBlock 引擎继承的魔法方块进度，加上区块领地。

        源代码链接：[OneBlockIslands](https://github.com/BentoBoxWorld/ChunkBlock/blob/develop/src/main/java/world/bentobox/chunkblock/dataobjects/OneBlockIslands.java)

    !!! question "变量"
        - `uniqueId` ——岛屿唯一 ID，等于岛屿的 `uniqueId`。
        - `blockNumber` ——当前破坏的方块数。
        - `lifetime` ——曾破坏的总方块数。
        - `phaseName` ——当前阶段名称。
        - `hologram` ——正在显示的全息图文本。
        - `unlockedChunks` ——有序的 `"dx,dz"` 声称列表，相对于中心区块。`"0,0"` 总是第一个，永远不能被移除。
        - `lastKnownLevel` ——最后计算时的岛屿等级，用于检测增益和损失。

    !!! example "代码示例"
        ```java
        public void accessChunkBlockData(@NonNull Island island) {
            BentoBox.getInstance().getAddonsManager().<ChunkBlock>getAddonByName("ChunkBlock")
                .ifPresent(chunkBlock -> {
                    OneBlockIslands data = chunkBlock.getOneBlocksIsland(island);
                    int chunks = data.getUnlockedChunkCount();
                    List<String> claimOrder = data.getUnlockedChunks();

                    ChunkManager cm = chunkBlock.getChunkManager();
                    long credit = cm.getCredit(island);
                    long spent = cm.getSpentLevels(island);
                    int max = cm.getMaxChunks(island);
                    boolean here = cm.isUnlocked(island, someLocation);
                });
        }
        ```

### 事件

ChunkBlock 触发 AOneBlock 魔法方块事件（`BlockClearEvent`、`MagicBlockEntityEvent`、`MagicBlockEvent`、`MagicBlockPhaseEvent` ——见 [AOneBlock API 章节](../AOneBlock/index.md#events)，同样的字段，在 `world.bentobox.chunkblock.events` 包中）加上它自己的两个。

=== "ChunkUnlockEvent"
    !!! summary "描述"
        为岛屿声称的每个区块各触发一次。**不可取消** ——声称已经被决定和支付了；这是一个通知。

        链接到类：[ChunkUnlockEvent](https://github.com/BentoBoxWorld/ChunkBlock/blob/develop/src/main/java/world/bentobox/chunkblock/events/ChunkUnlockEvent.java)

    !!! question "变量"
        - `@NonNull Island island` ——声称区块的岛屿。
        - `@NonNull Vector chunkOffset` ——相对于岛屿中心区块的区块偏移（x 和 z；y 总是 0）。
        - `int unlockIndex` ——区块在岛屿声称顺序中的位置。中心区块是 0。

    !!! example "代码示例"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onChunkUnlock(ChunkUnlockEvent event) {
            Island island = event.getIsland();
            Vector offset = event.getChunkOffset();
            int index = event.getUnlockIndex();
        }
        ```

=== "ChunkRelockEvent"
    !!! summary "描述"
        为岛屿在其等级下降时失去的每个区块各触发一次。**不可取消。** 事件最先到达最近声称的，匹配区块实际被夺回的顺序。

        链接到类：[ChunkRelockEvent](https://github.com/BentoBoxWorld/ChunkBlock/blob/develop/src/main/java/world/bentobox/chunkblock/events/ChunkRelockEvent.java)

    !!! question "变量"
        - `@NonNull Island island` ——失去区块的岛屿。
        - `@NonNull Vector chunkOffset` ——相对于岛屿中心区块的区块偏移。
        - `int unlockIndex` ——区块在声称顺序中保持的位置。

    !!! example "代码示例"
        ```java
        @EventHandler(priority = EventPriority.MONITOR)
        public void onChunkRelock(ChunkRelockEvent event) {
            Island island = event.getIsland();
            Vector offset = event.getChunkOffset();
            int index = event.getUnlockIndex();
        }
        ```

### 请求处理程序

不想要编译时依赖的插件可以使用 [附属插件请求 API](../../BentoBox/Request-Handler-API---How-plugins-can-get-data-from-addons.md)。ChunkBlock 从魔法方块引擎注册 `island-stats` 和 `location-stats`，加上：

=== "unlocked-chunks"
    !!! summary "描述"
        玩家岛屿的领地信息。提交 `"player"` → `UUID`。如果玩家在 ChunkBlock 世界中没有岛屿，返回空地图。

    !!! question "返回的地图"
        - `count` ——`Integer`，解锁区块包括中心。
        - `max` ——`Integer`，此岛屿最多可以解锁。
        - `ring` ——`Integer`，最远解锁区块的环号。
        - `spent` ——`Long`，已花费在区块上的等级。
        - `credit` ——`Long`，可花费的等级信用。
        - `chunks` ——`List<String>`，声称顺序中的 `"dx,dz"` 偏移。

    !!! example "代码示例"
        ```java
        Map<String, Object> request = Map.of("player", player.getUniqueId());
        @SuppressWarnings("unchecked")
        Map<String, Object> result = (Map<String, Object>) new AddonRequestBuilder()
                .addonName("ChunkBlock")
                .label("unlocked-chunks")
                .addMetaData(request)
                .request();
        int chunks = (int) result.getOrDefault("count", 0);
        ```

## 更新日志

??? note "v1.0.0 中的新增功能"
    **发布于：** 2026-07-28

    第一个发布。OneBlock 循环，在一个当你为它付出代价时会长大的区块。

    - **通过击打边界声称区块。** 岛屿等级是可花费的信用（`levels-per-chunk` 每个声称，默认 1）。所有者瞄准墙并挥拳或右键单击以打开下一个区块，在任何方向。
    - **领地有后果。** 每个声称都被记录顺序；如果岛屿等级低于已花费的，最近声称的区块重新锁定，最新的在前。内部建筑完好无损。`relock-on-level-loss: false` 给出棘轮模式。
    - **一堵你真的无法穿过的边界。** 行走、冲刺跳跃、鞘翅、撤退、末影珍珠（退款）、唱诗台果实、坐骑、船和飞行都在任何高度受到限制。活塞、液体、发射器、树木生长、蔓延和爆炸不能到达，掉落物反弹。
    - **一条你能看到的前沿。** 每个玩家粒子幕布标记被锁定的区块面，可选的客户端屏障方块，加上当信用被赚取和区块被声称时的庆祝效果。世界本身永远不会被修改。
    - **`/ch chunks`** ——你领地的彩色聊天地图、你能声称什么以及你的信用。
    - **按设计安全。** 被重新锁定区块捕获的玩家被移至最近的解锁点，飞行保留，无摔伤。
    - **需要 Level 附属插件** ——岛屿等级是唯一且唯一的区块货币。

    [发布 1.0.0](https://github.com/BentoBoxWorld/ChunkBlock/releases/tag/1.0.0)

!!! warning "v1.0.1 中的新增功能——标志 ID 和默认命令已更改"
    **发布于：** 2026-07-30

    补丁版本修复了针对 1.0.0 报告的每个 bug，加上两个兼容性问题，只在运行 ChunkBlock 与其他游戏模式一起时出现。

    - 🐛 **在边界附近采矿不再垃圾邮件声称消息。** 声称检测忽略了你实际单击的方块并通过墙传递，所以在距离被锁定区块几个方块的生成器中采矿在每次摇摆都会唠叨 *"你需要 X 更多等级(s)的信用"*。声称现在只在对边界的真正目标上触发，失败反馈是速率限制的。修复 [#14](https://github.com/BentoBoxWorld/ChunkBlock/issues/14)。
    - 🐛 **重生不再能将玩家搁浅在陌生人的岛屿上。** 重生降落在旧的或被遗弃的岛屿的被锁定区块中用来在 *那个岛屿内* 重新定位玩家，生成一个着陆块。不属于该岛屿的玩家现在被送到他们自己的岛屿家代替。修复 [#13](https://github.com/BentoBoxWorld/ChunkBlock/issues/13)。
    - 🔡 **阶段 GUI 尊重 setcount 权限。** *"点击更改"* 不再向没有 `chunkblock.island.setcount` 的玩家提供，GUI 标题说 *ChunkBlock* 阶段。修复 [#11](https://github.com/BentoBoxWorld/ChunkBlock/issues/11)。
    - 🔺 ⚙️ **拥有标志 ID，不再 AOneBlock 冲突。** BOSS 栏、动作栏和启动安全标志现在是 `CHUNKBLOCK_BOSSBAR`、`CHUNKBLOCK_ACTIONBAR` 和 `CHUNKBLOCK_START_SAFETY`。它们之前共享 AOneBlock 的 ID，BentoBox 拒绝重复的标志注册——所以在运行两者的服务器上，无论哪个附属插件加载第二个都悄悄失去它的标志。
    - 🔺 ⚙️ **默认命令从 `/cb` 更改为 `/ch`。** CaveBlock 已经使用 `/cb` 和 `/cbadmin`，所以默认值现在是 `ch chunkblock`（玩家）和 `chadmin chunkblockadmin cha`（管理员）。现有服务器保留他们 `config.yml` 中的任何别名；只有新安装获得新的默认值。
    - **Level 缺失时清晰关闭。** ChunkBlock 现在禁用自己并显示清晰的消息，而不是留下半注册的监听器在每次加入和移动上垃圾邮件错误。

    🔺 **升级后：** 如果你从默认值改变了 BOSS 栏、动作栏或启动安全世界设置，升级后重新应用一次——旧的 `ONEBLOCK_*` / `START_SAFETY` 值不再被读取。

    🔡 **区域设置注意：** 键被重命名（`protection.flags.CHUNKBLOCK_*`，阶段 GUI 标题）。重新生成或更新自定义的区域设置文件。

    **兼容性：** BentoBox API 3.13.0+，Minecraft 1.21+，Java 21。

    [发布 1.0.1](https://github.com/BentoBoxWorld/ChunkBlock/releases/tag/1.0.1)
