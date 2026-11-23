# Boxed

玩家在一个只能通过完成进度来扩展的盒子中生存！

由 [tastybento](https://github.com/tastybento) 创建和维护。

{{ addon_description("Boxed") }}

## BentoBox 要求

* 总是使用最新版本的 BentoBox（快照版可以在此下载：[https://ci.bentobox.world](https://ci.bentobox.world)）
* InvSwitcher - 在服务器的世界之间保持进度、库存等分开。
* Border - 显示盒子的边界

## 如何安装

### 快速开始

1. 将 Boxed 插件放入 BentoBox 的 addons 文件夹中，连同 InvSwitcher 和 Border 一起（使用最新版本！）。
2. 重启服务器 - 将创建新的世界。*首次运行这将花费很长时间*
3. 登录
4. 输入 `/boxed` 开始。
5. （可选）关闭进度公告 `/gamerule announceAdvancements false`，否则当玩家获得进度时服务器会有大量垃圾信息。

* 你将从一棵树开始。这里有一个包含一些便利物品的箱子。（这是岛屿的蓝图）
* 你只能在显示为边界的盒子区域内操作。
* 完成进度以使你的盒子变大。
* 使用进度屏幕（L键）检查你的进度。
* 默认情况下，怪物不会在你的盒子外面生成，但你的盒子变大了，只需要一个方块就可以生成怪物！
* 盒子的所有者可以使用从盒子内部扔出的末影珍珠移动盒子。注意！这是单程旅行。（config.yml 中的可选设置）
* 盒子设置有一个选项，允许其他等级移动盒子（寻找堆肥箱图标）

## 自定义进度

[下载官方 Boxed DataPack](https://github.com/BentoBoxWorld/BoxedDataPack) 获取自定义进度。
或者你可以自己做。查看[教程视频了解更多信息](https://youtu.be/zNzQvIbweQs)

## 控制世界大小

!!! warning "不再需要 Regionerator"
    本指南的旧版本曾推荐使用第三方插件 [Regionerator](https://github.com/Jikoo/Regionerator) 来裁剪未使用的区块。**自 BentoBox 3.15.0 起，此功能已内置** —— BentoBox 现在会直接删除区域（`.mca`）文件，因此不再需要 Regionerator，也不再推荐在 Boxed 中使用它。如果你仍在运行它，可以将其移除：它是多余的，而且除非正确设置了种子世界的豁免，否则它可能会删除 Boxed 的种子世界并导致服务器启动非常缓慢。

随着玩家扩展和重置盒子，Boxed 世界会不断增大，而这些磁盘占用现在由 BentoBox 自身通过两种方式回收。

**自动维护（默认开启）。** 当盒子被重置时，它会被*软删除*（标记为待删除，而不是逐区块擦除），并由一个计划任务在后台回收其区域文件。deleted 清扫默认每 24 小时运行一次。BentoBox `config.yml` 中的相关部分为：

```yaml
island:
  deletion:
    housekeeping:
      # 回收已被标记为删除的盒子（例如重置后）的区域文件。
      # 默认开启。
      deleted-sweep:
        enabled: true
        interval-hours: 24
      # 回收长期未被访问的区域文件，无论盒子是否被重置。
      # 默认关闭 —— 若需最积极地控制世界大小，请开启此项。
      age-sweep:
        enabled: false
        interval-days: 30
        min-age-days: 60
```

**手动清除。** 你也可以根据需要从服务器控制台或游戏内回收空间（参见[指令](Commands)）：

* `/boxadmin purge deleted` —— 立即回收所有已被标记为删除的盒子的区域文件。
* `/boxadmin purge <days>` —— 回收那些所有者已 `<days>` 天未登录、且区域文件至少已存在那么久的盒子的区域文件。
* `/boxadmin purge unowned` —— 将所有无主盒子标记为可删除，以便下次清扫将其移除。

!!! note "大规模清除后请重启"
    区域文件会立即从磁盘删除，但 Paper 会将最近加载的区块保留在内存缓存中。**大规模清除后请重启服务器**，以清空该缓存并完全释放回收的空间。受清除保护的盒子、出生点岛屿，以及（若安装了 Level 附属）等级高于所配置清除等级的盒子，始终会被跳过。一如既往，**请在清除前备份你的世界文件夹。**

旧的 `keep-previous-island-on-reset` 设置已不复存在 —— 盒子在重置时始终会被软删除并由自动维护清理，因此无需为让 Regionerator“接管”而进行任何配置。


## 高级配置

### config.yml
配置与 BSkyBlock, AcidIsland 等非常相似。

每个玩家都将拥有自己的土地，直到岛屿距离值的限制。默认值是 400，所以土地将是 800 x 800 块。土地是半随机的，但每个玩家将获得大致相同的布局（参见生物群系配置）。结构如村庄、破损的下界门、沉船等是随机的，因此有些玩家可能会得到它们，有些则不会。在未来版本中，关闭结构将是一个配置选项。要塞被关闭，不存在。每个玩家的土地被不同温度的海洋包围。如果边界不是固体的，那么玩家理论上可以探索其他土地。

*世界种子*
世界种子是用来生成土地的。我建议保留这个值。如果你改变它，土地可能会非常不同。

Boxed 3.5.0 新增的选项：

??? note "boxed.structure-time-budget"
    每个 tick 中在盒子里放置原版结构（村庄、沉船等）最多可占用的毫秒数。结构会逐个放置，直到用完这段时间，因此服务器有余力时，新盒子能在几秒内放好所有结构。一个 tick 为 50 毫秒。如果放置结构导致卡顿，请调低此值。`0` 表示每 tick 只放置一个结构。

    只有当结构可能触及的所有区块都已加载时，才会放置该结构，因此靠近盒子边缘的结构会在玩家第一次走近时才出现，而不是在盒子创建后立即出现。

    默认：`10`

??? note "world.structure-settings"
    在 Boxed 世界中单独关闭或开启某个原版结构。这同时作用于世界生成和结构搜索：`/locate`、末影之眼、探险家地图和藏宝图、海豚以及制图师交易。键是原版结构 ID；值为 `false` 时禁用该结构，为 `true` 时即使 BentoBox 的全局 `world.disabled-structures` 列表禁用了它，也强制开启。未列出的结构遵循 BentoBox 的全局列表。

    ```yaml
    structure-settings:
      monument: false
      trial_chambers: false
    ```

    默认：`{}`

??? note "area.teams-disabled"
    在 Boxed 世界中关闭团队系统。设为 `true` 时，玩家无法邀请、接受团队邀请、踢出、离开、晋升、降级或更换所有者。信任和合作仍然有效。开启此项后，请运行一次 `/boxadmin team disbandall` 来解散现有团队。参见[关闭团队](../../BentoBox/About/Teams.md#turning-teams-off)。

    默认：`false`

!!! tip "如果创建盒子导致卡顿"
    试试 BentoBox 的区块预生成：在 BentoBox 的 `config.yml` 中设置 `island.pregeneration.enabled: true`（BentoBox 3.14.0 及更新版本）。它会在后台提前为接下来的几个盒子生成区块，赶在有人需要之前。

### 蓝图

有一个蓝图“岛屿”被用来生成树、箱子和下到 y = 5 的方块。默认的地面高度约为 y = 65，所以蓝图必须约 60 块高。如果你制作了任何好的蓝图，请分享它们！

### advancements.yml
这个文件包含所有的进度以及如果你获得一个，你的盒子应该增长多少。如果你有自定义进度，文件可以包含它们。

顶部有两个设置 - 第一个 `default-root-increase` 你可能不需要改变。这将任何根进度的分数设置为 0。换句话说，仅仅因为看到新的进度标签页，玩家不会获得盒子扩展。

第二个设置 `unknown-advancement-increase` 给予任何未知进度，即，这个文件中未列出的进度一个默认值。这是添加自定义进度通过数据包时使用的默认值，它免除了你在这个文件中列出每个新进度的需要。

示例：

```
# 列出当进度发生时盒子将增加多少块
settings:
  default-root-increase: 0
  unknown-advancement-increase: 1
advancements:
  'minecraft:adventure/adventuring_time': 1


  'minecraft:adventure/arbalistic': 1
  'minecraft:adventure/bullseye': 1
...
```
  
### biomes.yml
玩家的土地有生物群系，它们在这里定义。现在不可能定义生物群系的位置，只有它们对地形的影响。

* 高度：默认高度是 8。较低的数字会产生较低的土地，较高的数字会产生较高的土地。
* 规模：这是土地将会有多平滑。较小的数字更加崎岖，较大的数字更加平坦。

将海洋生物群系的高度数字设置得更高会导致海洋底部高于海平面并创建土地。

这些数字现在大多是粗略猜测，如果你提出了更好的值，请分享它们！


## 权限

权限可以在[这里](Permissions)找到。

## 指令

指令可以在[这里](Commands)找到。

## 占位符

占位符可以在[这里](Placeholders)找到。

## 更新日志

!!! warning "v3.5.0 新内容 —— 需要 Java 25 和 BentoBox 3.23.0"
    **发布于：** 2026-11-21

    兼容性：BentoBox 3.23.0 或更新版本 · Paper 1.21.5 – 26.3 · Java 25。

    - 🔺 **需要 Java 25。** Boxed 现在面向 Java 25 和 BentoBox 3.23 构建。它无法在旧版 Java 上加载，即使是 Minecraft 1.21.x 服务器也不行。
    - ⚙️ **新盒子中的结构放置更流畅。** 新盒子中的村庄、沉船、废墟和其他结构过去每 3 秒放置一个，一个盒子大约需要 3½ 分钟。现在它们在每 tick 的时间预算 `boxed.structure-time-budget`（默认 `10` 毫秒）内放置，几秒内就会出现。它们也不再迫使服务器在 tick 内生成区块：结构会等到其可能触及的所有区块都已加载，因此靠近盒子边缘的结构会在玩家第一次走近时出现。
    - 🔺 **结构不再被重复放置。** 重启后，结构可能会再次放置在玩家的盒子上，覆盖玩家的建筑并生成额外的生物。此问题已修复，旧版本保存的列表也会被自动清理。
    - ⚙️ **用新的 `area.teams-disabled` 选项禁用团队**（默认 `false`）。信任和合作仍然有效。
    - ⚙️ **用新的 `world.structure-settings` 选项控制原版结构**，可在 Boxed 世界中单独关闭某些结构或强制开启。
    - 🔺 **玩家可以列出、重命名和删除自己的家点。** `boxed.island.homes`、`boxed.island.renamehome` 和 `boxed.island.deletehome` 之前没有声明，因此只有操作员拥有。现在它们默认授予所有人。如果你不希望如此，请在权限插件中将其设为否定。
    - 🔺 **`/boxadmin place` 改用 `boxed.admin.place`**（默认仅操作员）。它以前检查的是未声明的节点 `boxed.boxed.commands.boxadmin.place`。如果你曾把该节点授予非操作员的工作人员，请改为授予 `boxed.admin.place`。
    - 🐛 无法加载的结构不再导致之后的所有结构在重启前都无法放置；`structures.yml` 中缺失的结构名也不再导致其后列出的所有结构被跳过。

    新选项会以默认值添加到 `config.yml` 中；参见 [config.yml](#configyml)。

    [发布 v3.5.0](https://github.com/BentoBoxWorld/Boxed/releases/tag/3.5.0)

??? note "v3.4.1 新内容"
    **发布于：** 2026-09-25

    一个维护版本。需要 BentoBox **3.17.0** 或更新版本。兼容性：Paper 1.21.x – 26.x · Java 21。

    - 🐛 **启用时不再出现 `contloc out of spec` 崩溃。** 在首次启动时，从战利品箱中掷出的探险家地图可能会搜索远超种子区域之外，其中陆地性下降到 -1.2 以下，而 BentoBox 跳过了 Boxed。范围外的值现在落入最外层带。
    - 🐛 **`/boxadmin place ... NO_MOBS` 有效。** 第 7 个参数被拒绝，无法被读取；现在它被接受，不再继续进入后续放置。
    - 🐛 缺少的一对括号在一些侵蚀等级 5 种子区域中选择了错误的生物群系。仅升级后生成的种子世界受影响。
    - ⚙️ `config.yml` 中更清晰的 `area.deaths` 注释，解释哪些死亡设置影响[等级](../../addons/Level/index.md) 2.29.0 下的岛屿等级，哪些仅影响 BentoBox 的死亡计数器和 `%boxed_deaths%`。仅注释更改。
    - 现在还将发布到 CurseForge 和 Hangar。

    [发布 v3.4.1](https://github.com/BentoBoxWorld/Boxed/releases/tag/3.4.1)

??? note "v3.4.0 新内容"
    **发布于：** 2026-05-30

    - **试炼密室(Trial Chambers)支持。** 当结构从种子世界拉取到玩家的盒子中时,Boxed 现在会捕获并恢复试炼刷怪笼(Trial Spawner)的状态(包括普通*和*不祥(ominous)两种配置),并将 `trial_chambers` 识别为受进度驱动的盒子扩展所追踪的结构。
    - 🐛 **不再跨游戏模式丢失进度。** 当在*其他*非 Boxed 游戏模式中重置岛屿时,Boxed 不再清除玩家的进度和统计数据。
    - 🐛 删除岛屿时,待处理的结构粘贴现在会被取消,防止将结构放入已不存在的盒子。
    - 🐛 不祥的试炼刷怪笼现在会以正确的配置恢复,而不是总是应用普通配置。
    - 构建与测试栈现代化:Paper 1.21.11、BentoBox API 3.13.0、JUnit 5 + Mockito + MockBukkit。

    !!! note
        试炼密室是在生成盒子时从种子世界捕获的,因此在 3.4.0 *之前*创建的盒子不会追溯获得它们。新盒子(以及新扩展的区域)将包含它们。

    [发布 v3.4.0](https://github.com/BentoBoxWorld/Boxed/releases/tag/3.4.0)

## 翻译

{{ translations("Boxed") }}