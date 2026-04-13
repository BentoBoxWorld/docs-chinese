# AcidIsland

**AcidIsland** 是一种生存游戏模式，玩家必须在一个被酸海包围的岛屿上生存。

由 [tastybento](https://github.com/tastybento) 创建并维护。

{{ addon_description("AcidIsland") }}

## 故事
你在一个岛上，周围是酸海！如果你喜欢 Skyblock，尝试 AcidIsland，迎接新的挑战吧！

这是 SkyBlock 的一个变种。扩展你的岛屿时，你必须应对酸水，而不是掉落，玩家可以乘船前往彼此的岛屿。

## 安装

0. 安装 BentoBox 并至少运行一次以创建其数据文件夹。
1. 将此 jar 放入 BentoBox 插件的 addons 文件夹中。
2. 重启服务器。
3. 插件将创建世界和数据文件夹，在文件夹内将有一个 config.yml。
4. 停止服务器。
5. 按照您的意愿编辑 config.yml。
6. 如果您进行了会影响它们的更改，请删除默认创建的任何世界。
7. 重启服务器。

## 权限

权限可以在 [这里](Permissions) 找到。

## 命令

命令可以在 [这里](Commands) 找到。

## 占位符

占位符可以在 [这里](Placeholders) 找到。

## 更新日志

??? warning "v1.21.0 新内容 — 需要 BentoBox 3.14.0,语言文件迁移"
    **发布于:** 2026-04-12

    - **樱花林起始岛屿。** 为 Minecraft 1.21+ 服务器新增以樱花林生物群系为主题的起始岛屿蓝图。要激活它,请删除 `BentoBox/addons/AcidIsland/blueprints/`,以便在下次启动时重新生成蓝图。
    - 🔺 **现在需要 BentoBox API 3.14.0。** 安装此版本前请更新 BentoBox。
    - 🔡 **全部 24 个语言文件从 `&` 代码迁移至 MiniMessage。** 删除 `BentoBox/locales/AcidIsland/` 并重启以重新生成。自定义文件中任何剩余的 `&` 代码将显示为纯文本。
    - 错误修复:EssentialsX 启动时加载失败时,EssentialsX 上帝模式检查中的 NullPointerException。
    - 迁移过程中修复了几个预先存在的语言文件错误。

    [发布 v1.21.0](https://github.com/BentoBoxWorld/AcidIsland/releases/tag/1.21.0)

## 翻译

{{ translations("AcidIsland") }}