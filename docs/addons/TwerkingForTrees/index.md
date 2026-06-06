# TwerkingForTrees

**TwerkingForTrees** 可以让你的玩家通过扭动来更快地种植树木。

由 [tastybento](https://github.com/tastybento) 创建和维护。

{{ addon_description("TwerkingForTrees") }}

!!! info "兼容性"
    需要 **BentoBox 3.14.0** 或更新版本，**Minecraft 1.21.3 – 1.21.4**，以及 **Java 21**。

## 安装

1. 将插件 jar 文件放入 BentoBox 插件的 addons 文件夹

2. 重启服务器

3. 在你的岛屿上种植树木

4. 扭动,扭动,再扭动...

5. 树木长大了!

## 树木

大多数树木从单棵扭动的树苗生长。**深色橡树**和**苍白橡树**是例外：与原版 Minecraft 一样，它们是仅限 2x2 的巨型树，因此你必须将四棵树苗排成 2x2 网格并在旁边扭动——单棵树苗不会生长。

## 配置文件

```
# TwerkingForTrees 配置文件。
#
# 玩家必须扭动多少次才能让树木开始更快生长。
# 如果玩家扭动次数不够,树木将不会更快生长。
minimum-twerks: 4
# 长按扭动。无障碍功能。无需连续按下潜行键,只需按住即可。
hold-for-twerk: false
# 使用疾跑而非扭动来种植树木。
sprint-to-grow: false
# 扭动时寻找树苗的范围。范围为 5 表示在玩家周围各个方向 +/- 5 个方块内查找。
# 设置过大会导致服务器卡顿。
range: 5
sounds:
  # 开启/关闭声音。
  enabled: true
  twerk:
    # 当玩家扭动足够次数,树苗开始更快生长时播放的声音。
    # 可用的声音如下:
    #    https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Sound.html
    sound: block.note_block.bass
    volume: 1.0
    pitch: 2.0
  growing-small-tree:
    # 当小树 (1x1) 生长时播放的声音。
    # 可用的声音如下:
    #    https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Sound.html
    sound: block.bubble_column.upwards_ambient
    volume: 1.0
    pitch: 1.0
  growing-big-tree:
    # 当大树 (2x2) 生长时播放的声音。
    # 可用的声音如下:
    #    https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Sound.html
    sound: block.bubble_column.upwards_ambient
    volume: 1.0
    pitch: 1.0
effects:
  # 开启/关闭粒子效果。
  enabled: true
  # 每次玩家扭动时播放的效果。
  # 可用的效果如下:
  #    https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Effect.html
  twerk: MOBSPAWNER_FLAMES

```

## 翻译

{{ translations("TwerkingForTrees") }}

??? warning "v1.6.0 更新内容 — 重大变更"
    **发布日期：** 2026-06-01

    一次重大的现代化更新。完整说明见 [Release v1.6.0](https://github.com/BentoBoxWorld/TwerkingForTrees/releases/tag/1.6.0)。

    - 🔺 **需要 BentoBox 3.14.0**（Java 21、Paper 1.21.11、Minecraft 1.21.3 – 1.21.4）。该插件无法在更旧的服务器上加载。
    - 🌳 新增**苍白橡树**支持，包括其 2x2 巨型树变体。与深色橡树一样，苍白橡树是仅限 2x2 的树——单棵树苗不会生长。
    - ⚙️ **声音配置格式已更改。** config.yml 中的声音标识符现在使用小写点号格式（例如 `block.note_block.bass`）。如果从 1.5.2 沿用旧的 config.yml，请刷新它以保证扭动和树木生长的声音正常工作。
    - 新增配置选项：`hold-for-twerk`（无障碍——按住潜行而非连续点击）、`sprint-to-grow`（通过疾跑种植树木）以及 `range`（树苗搜索半径）。
    - 现在附带 `Pladdon` 和 `plugin.yml`，以便在现代 Paper 服务器上进行依赖感知加载。
    - 修复了深色橡树可从单棵树苗生长的问题，恢复了逐方块的岛屿边界强制执行（原木和树叶不会再越过岛屿边界），并修复了树木生长时的资源泄漏。
    - 新增 JUnit 5 / MockBukkit 测试套件。
