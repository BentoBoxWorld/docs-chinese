# BSkyBlock

玩家必须在天空中迷失的岛屿上生存。

由 [tastybento](https://github.com/tastybento) 创建并维护。

{{ addon_description("BSkyBlock") }}

## 历史
**BSkyBlock** 是 **ASkyBlock** 的进化版，适用于更新的 Minecraft 服务器版本。

## 安装

0. 安装 BentoBox 并至少运行一次，以创建其数据文件夹。
1. 将此 jar 文件放入 BentoBox 插件的 addons 文件夹中。
2. 重启服务器。
3. 插件将创建世界和数据文件夹，在该文件夹内将有一个 config.yml。
4. 停止服务器。
5. 根据您的需求编辑 config.yml。
6. 如果您进行了会影响它们的更改，请删除默认创建的任何世界。
7. 重启服务器。

## Config.yml

Config.yml 与 ASkyBlock 相似，但*不相同*。请注意，岛屿间距离和保护范围是**半径值**，因此岛屿大小将是这些值的两倍（以方块计）！此外，岛屿之间的距离将自动设置为区块边界（16 块的倍数）。

## 权限

权限可以在 [这里](Permissions) 找到。

## 命令

命令可以在 [这里](Commands) 找到。

## 占位符

占位符可以在 [这里](Placeholders) 找到。

## 更新日志

??? warning "v1.20.0 新内容 — 需要 BentoBox 3.13.0 和 Paper 1.21.11"
    **发布于：** 2026-04-27

    - 🐛 **修复了怪物生成。** 区块生成器没有重写 `shouldGenerateMobs()`，这在所有 BSkyBlock 生成的世界中悄悄地抑制了原版怪物生成。怪物现在能再次正确生成。
    - 🐛 **修复了水生动物（鱼、鱿鱼）的生成。** 自 1.21 平台迁移以来损坏的鱼和鱿鱼自然生成已恢复。修复 [BentoBox #2593](https://github.com/BentoBoxWorld/BentoBox/issues/2593)。
    - ⚡ **现代化的区块生成。** 世界生成器已从已弃用的 `generateChunkData()` + `BiomeGrid` 方法迁移到 Paper 当前的 `generateNoise()` + `BiomeProvider` API。
    - 🔡 全部 17 个语言文件中的告示牌文本已从传统的 `&c` 颜色代码迁移到 MiniMessage 格式。
    - 现代化构建：JDK 21、JUnit 5 + MockBukkit 测试栈。

    🔺 **需要 BentoBox 3.13.0 或更高版本以及 Paper 1.21.11。** 旧版 BentoBox 无法加载此插件。

    🔡 **语言提示：** 告示牌文本现在使用 MiniMessage 标签（如 `<red>…</red>` 而不是 `&c`）。已自定义的语言文件需要更新。

    [Release v1.20.0](https://github.com/BentoBoxWorld/BSkyBlock/releases/tag/1.20.0)

## 翻译

{{ translations("BSkyBlock") }}