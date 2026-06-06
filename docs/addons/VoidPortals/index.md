# 虚空传送门

**虚空传送门**让玩家通过跳入虚空在维度之间穿梭。当玩家在启用了该标志的世界中跳入虚空时，他们会被安全地传送到下一个维度的对应位置——**主世界 → 下界 → 末地 → 主世界**——而不是死亡。

由[BONNe](https://github.com/BONNe)创建和维护。

{{ addon_description("VoidPortals", beta=True) }}

!!! info "兼容性"
    需要 **BentoBox 3.14.0** 或更新版本，**Minecraft 1.21+**，以及 **Java 21**。

## 安装

1. 将插件的 jar 文件放入 BentoBox 插件的 addons 文件夹中。
2. 重启服务器。
3. “虚空世界传送”标志**默认禁用**——在游戏模式的管理设置面板中按世界启用它。

## 标志

虚空传送门添加了一个世界设置标志。在游戏模式的管理设置面板中按世界切换它。

{{ flags_source("VoidPortals", "WORLD_SETTING") }}

## 翻译

{{ translations("VoidPortals") }}

??? note "v1.6.1 更新内容"
    **发布日期：** 2026-06-01

    一个错误修复版本。完整说明见 [Release v1.6.1](https://github.com/BentoBoxWorld/VoidPortals/releases/tag/1.6.1)。

    - 跳入虚空不再会在到达时杀死你。坠入虚空会积累向下的速度，并在传送时延续，使你在到达下一个维度的瞬间撞向地面。现在你的速度和坠落距离会在到达时重置，因此你能安全着陆。

??? warning "v1.6.0 更新内容 — 重大变更"
    **发布日期：** 2026-06-01

    自 2019 年以来的首个版本——虚空传送门已为当前的 BentoBox 生态系统全面现代化。完整说明见 [Release v1.6.0](https://github.com/BentoBoxWorld/VoidPortals/releases/tag/1.6.0)。

    - 🔺 **需要 Java 21、Paper 1.21.11 和 BentoBox 3.14.0**（原为 Spigot 1.13.2 / BentoBox 1.5.0）。该版本无法在更旧的服务器上加载。
    - 现在附带 `Pladdon` 和 `plugin.yml`，以便 jar 在现代 Paper 服务器上正确加载。
    - 🔡 新增 14 种语言并将所有语言文件转换为 **MiniMessage** 格式。如果你自定义了语言文件，请重新生成或迁移你的修改——不再使用旧的 `&` 颜色代码。
    - 新增 JUnit 5 / MockBukkit 测试套件，包括一个确保对角虚空坠落仍能传送的回归测试。
