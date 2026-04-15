# DimensionalTrees

**DimensionalTrees** 是一个插件，可以让在下界/末地生长的树变成该维度的树。

由 [Awakened-Redstone](https://github.com/Awakened-Redstone) 创建，由 [tastybento](https://github.com/tastybento) 维护。

{{ addon_description("DimensionalTrees") }}

## 配置

最新的 `config.yml` 可在[此处](https://github.com/BentoBoxWorld/DimensionalTrees/blob/develop/src/main/resources/config.yml)查看。

每个材料槽(`logs` / `leaves`)现在都接受 **`material: weight` 的权重映射**,而不仅仅是一个字符串。权重之和恰好为 100 时,各材料按所填权重精确出现;超过 100 时自动按比例缩放;不足 100 时差额会保留为 AIR。无论哪种情况,启动时都会在日志中记录警告。

```yaml
nether:
  logs:
    gravel: 80
    netherrack: 20
  leaves:
    glowstone: 70
    soul_sand: 30
```

树生长时的解析顺序为:**树种级别覆盖 → 游戏模式级别覆盖 → 全局默认**。

??? note "nether.logs / end.logs"
    下界 / 末地中原木的全局替换材料。支持旧版的单一材料名,也支持新的权重映射。

??? note "nether.leaves / end.leaves"
    下界 / 末地中树叶的全局替换材料。

??? note "nether.per-tree / end.per-tree"
    可选的按树种覆盖。可以为 `oak`、`acacia`、`birch`、`jungle`、`spruce` 和 `dark_oak` 分别指定各自的 `logs` / `leaves` 映射。未填写或无效项会自动回退到全局默认。

??? note "nether.per-gamemode / end.per-gamemode"
    可选的按游戏模式覆盖。适用于同时运行多个 BentoBox 游戏模式的服务器(如 BSkyBlock + CaveBlock)。游戏模式在事件发生时通过 `IWM.getAddon(world)` 解析。

!!! tip "从 1.8.0 自动迁移"
    原有的单一字符串值(如 `logs: gravel`)会在 1.9.0 首次启动时自动转换为新的权重映射形式(`logs: {gravel: 100}`),日志会记录确认信息,无需手动编辑配置文件。

## 更新日志

??? note "v1.9.0 新内容 — 按树种、按游戏模式配置及权重材料混合"
    **发布于:** 2026-04-14

    - ⚙️ **按树种覆盖** — 可在下界和末地为 6 种树分别配置不同的原木/树叶替换(`per-tree.logs`、`per-tree.leaves`)。
    - ⚙️ **按游戏模式覆盖** — 运行多个 BentoBox 游戏模式的服务器现在可以为不同游戏模式配置不同的替换(`per-gamemode.logs`、`per-gamemode.leaves`)。
    - ⚙️ 🔺 **权重多材料混合** — 所有材料槽都支持 `material: weight` 映射,可混合多种方块类型。
    - ⚙️ **配置自动迁移** — 1.8.0 的单一字符串值会在首次启动时自动转换为新的权重映射格式。
    - 升级至 Java 21、Paper 1.21.11、BentoBox 3.14.0,并新增 Pladdon 支持以兼容独立运行。
    - 新增基于 JUnit 5 + MockBukkit 的测试套件。
    - 将已弃用的 `Material.matchMaterial` 替换为现代 Registry API。
    - 🔡 更新语言文件,使错误信息使用 MiniMessage 颜色代码。

    [发布 v1.9.0](https://github.com/BentoBoxWorld/DimensionalTrees/releases/tag/1.9.0)

## 翻译

{{ translations("DimensionalTrees") }}
