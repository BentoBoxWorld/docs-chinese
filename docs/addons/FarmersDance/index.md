# 农夫之舞

**农夫之舞**是一个简单的插件，允许玩家在任何植物附近跳舞以促使其生长。

由[BONNe](https://github.com/BONNe)创建和维护。

{{ addon_description("FarmersDance", beta=True) }}

## 安装

1. 将插件jar文件放在BentoBox插件的addons文件夹中
2. 重启服务器
3. 插件将生成一个可以更改的config文件。

## 信息

插件的主要思想是允许在你的岛屿上更快地生长任何植物。
与TwerkingForTrees的主要区别是，这个插件应该适用于任何可生长的植物，包括仙人掌、南瓜和蘑菇。

### config.yml

插件成功安装后，它将创建config.yml文件。这个文件中的每个选项都附有注释。请检查文件以获取更多信息。
你可以在这里找到最新的配置文件：[config.yml](https://github.com/BentoBoxWorld/FarmersDance/blob/develop/src/main/resources/config.yml)

## 权限

!!! 小贴士
    `[gamemode]`是一个前缀，根据你运行的游戏模式而变化。
    前缀是游戏模式的小写名称，即如果你使用BSkyBlock，前缀是`bskyblock`。
    类似地，如果你使用AcidIsland，前缀是`acidisland`。

=== "玩家权限"
    - `[gamemode].farmersdance` - 允许玩家使用跳舞促进植物生长的功能。

    
??? 问题 "缺少什么？"
    你可以在这个插件的[addon.yml](https://github.com/BentoBoxWorld/FarmersDance/blob/develop/src/main/resources/addon.yml)文件中找到权限的综合列表。  
    如果下面的列表确实缺少了什么，请告诉我们！

## 常见问题解答

??? 问题 "你能添加功能X吗？"
    请在[这里](https://github.com/BentoBoxWorld/FarmersDance/issues)添加。

## 兼容性

- [x] BentoBox - 1.20.0版本

插件基于Minecraft 1.19.2和BentoBox 1.20.0版本构建。

插件支持所有游戏模式插件。

## 翻译

{{ translations("FarmersDance") }}