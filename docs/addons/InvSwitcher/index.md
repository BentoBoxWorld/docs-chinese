# InvSwitcher

**InvSwitcher** 在不同世界之间分离玩家物品栏和其他方面。

由 [tastybento](https://github.com/tastybento) 创建和维护。

{{ addon_description("InvSwitcher") }}

以下内容在每个世界之间独立:

* 物品栏和盔甲
* 进度
* 饥饿度
* 经验值
* 生命值
* 游戏模式(创造、生存等)

## 如何使用

1. 将插件 jar 文件放入 BentoBox 插件的 addons 文件夹
2. 重启服务器
3. 完成!

## Config.yml

InvSwitcher 有一个 `config.yml`,包含两个主要部分。

### 世界

列出 InvSwitcher 运行的游戏模式世界。下界和末地世界会自动包含。

```yml
worlds:
- bskyblock_world
- acidisland_world
- oneblock_world
# ... 等等
```

### 选项

控制每个世界(以及可选地每个岛屿)切换哪些玩家方面。

```yml
options:
  inventory: true
  health: true
  food: true
  advancements: true
  gamemode: true       # 游戏模式(生存/创造/等)
  experience: true
  ender-chest: true
  statistics: true
  # 每个岛屿的物品栏切换(1.17.0 新增)
  # 世界级选项也必须为 true,岛屿选项才能生效。
  islands:
    active: true       # 总体启用每岛屿切换
    inventory: true    # 为玩家拥有的每个岛屿提供不同的物品栏
    health: false
    food: false
    advancements: false
    gamemode: false
    experience: false
    ender-chest: true
    statistics: false
```

将 `islands.active: true` 设置为允许拥有多个岛屿的玩家每个岛屿维护独立的物品栏(以及其他方面),而不仅仅是每个游戏模式世界。

## 命令

没有命令。

## 它的作用

这个插件将为玩家在每个已安装的游戏模式及其对应的世界中提供独立的物品栏、生命值、饥饿度、进度和经验值。它使玩家能够独立地玩每个游戏模式。

## 一个例子

**BSkyBlock** 的物品栏、生命值、饥饿度、进度和经验值仅在其相应的世界之间共享:

- BSkyBlock_world
- BSkyBlock_world_nether
- BSkyBlock_world_the_end

**请注意:**

- 它不仅限于 BentoBox 世界。它适用于服务器上的所有世界(目前)。

## 更新日志

??? note "v1.17.0 新内容"
    **发布于:** 2026-03-31

    - **每岛屿物品栏切换。** 拥有多个岛屿的玩家现在可以在同一游戏模式中每个岛屿维护独立的物品栏(以及可选的生命值、饥饿度、经验值、末影箱、统计数据)。通过 `options.islands.active: true` 启用,并配置每个子选项。世界级选项也必须为 `true`,其对应的岛屿选项才能生效。
    - ⚙️ `config.yml` 中新增 `options.islands` 部分。
    - 错误修复:返回原始岛屿时物品栏丢失的问题。

    [发布 v1.17.0](https://github.com/BentoBoxWorld/InvSwitcher/releases/tag/1.17.0)

## 翻译

{{ translations("InvSwitcher") }}