# SkyGrid

**SkyGrid** 是一个充满了浮动方块的地图，这些方块放置在一个四方格网上。所以每个方向上的每第四个方块是实际的方块，其他的都是空气。原始SkyBlick的创造者SethBling于2012年发布了SkyGrid，它已成为最受欢迎的Minecraft地图之一。

在SkyGrid中玩耍（和生存）有其目标和技巧，网络上有大量的帮助、技巧和方法，使这个游戏非常有趣！

由[tastybento](https://github.com/tastybento)创建和维护。

{{ addon_description("SkyGrid") }}

## 安装

0. 安装BentoBox并至少运行一次服务器以创建其数据文件夹。
1. 将这个jar文件放在BentoBox插件的addons文件夹中。
2. 重启服务器。
3. 插件将创建世界和一个数据文件夹，并且文件夹中会有一个config.yml。
4. 停止服务器。
5. 按照您的意愿编辑config.yml。
6. 如果您做了会影响它们的更改，删除默认创建的任何世界。
7. 重启服务器。

## 权限

权限可以在[这里](Permissions)找到。

## 指令

指令可以在[这里](Commands)找到。

## 占位符

占位符可以在[这里](Placeholders)找到。

## 更新日志

??? warning "v2.2.4 新内容 —— 世界生成修复"
    **发布于：** 2026-11-05

    兼容性：BentoBox API 3.3.1 · Minecraft 1.21.x（在 Paper 26.3 上测试）· Java 21。

    - 🔺 **网格不再充满石头和草。** 原版地形会在网格下方生成，原版地表生成也会把方块替换为草。现在网格位置只会放置你配置中的方块。[PR #88](https://github.com/BentoBoxWorld/SkyGrid/pull/88)
    - 🔺 **区块不再重复。** 每个区块都从相同的随机序列开始，因此同样的图案每 16 格重复一次。现在每个区块都有自己的随机序列。[PR #88](https://github.com/BentoBoxWorld/SkyGrid/pull/88)
    - **甘蔗现在有水了。** 它位于一个小型砂岩水池中，水不会流走。在寒冷的生物群系中水池里的水可能会结冰。[PR #89](https://github.com/BentoBoxWorld/SkyGrid/pull/89)
    - **仙人掌和枯萎的灌木不再悬空。** 它们现在立在砂岩上方的沙子上。[PR #89](https://github.com/BentoBoxWorld/SkyGrid/pull/89)

    🔺 **现有世界：** 已生成的区块不会改变，因此新旧区块交界处会出现明显的不一致。如需一致的网格，请删除你的 SkyGrid 世界并让其重新生成——**这会移除这些世界中的所有岛屿**，请事先与玩家沟通并做好备份。

    [发布 v2.2.4](https://github.com/BentoBoxWorld/SkyGrid/releases/tag/2.2.4)

## 翻译

{{ translations("SkyGrid") }}