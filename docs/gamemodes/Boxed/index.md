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

## 使用 Regionerator

*注意：此插件旨在删除你世界的未使用区域！如果你使用它，请确保进行备份！风险自负！*

[Regionerator](https://github.com/Jikoo/Regionerator) 是一个插件，可以逐渐删除未使用的区块以保持世界大小较小。它不是由 BentoBox 团队编写，但它支持 BentoBox 并尊重盒子边界。它可以用来删除盒子区块，以便它们可以再生成。由于 Boxed 使用种子世界进行复制，这些可能会被 Regionerator 视为未使用并被删除，这意味着启动变得非常慢。为避免这种情况，将种子世界设置为免除其删除，将这些设置在 Regionarator 配置文件的世界部分：

```
# 插件能够删除区域的世界
worlds:
  # “default” 应用于未指定的所有世界。
  boxed_world/seed_base:
    days-till-flag-expires: -1
  boxed_world/seed:
    days-till-flag-expires: -1
  default:
    # 标记早于 x 天的旗帜可以被忽略并且该区域被删除。
    # 设置为 -1 以在世界中禁用 Regionerator。
    # 要禁用标记，请将此设置为 0。
    # days-till-flag-expires 必须大于 0 才能与 delete-new-unvisited-chunks 一起使用
    days-till-flag-expires: 0
```

为了

最大化利用 Regionarator，更改 BentoBox config.yml 文件以*不*在岛屿被移除时删除区块。这将留给它进行删除，并且如果未使用区域足够大，它应该会清理区块。配置是设置 `keep-previous-island-on-reset: true`：

```
deletion:
    # 切换是否在玩家重置它们时应保留岛屿，在世界中保留或删除。
    # * 如果设置为 'true'，每当玩家重置他的岛屿时，他的前一个岛屿将变为无主并且不会从世界中删除。
    #   然而，你仍然可以通过清理删除那些无主岛屿。
    #   在更大的服务器上，这可能导致世界大小增加。
    #   然而，这允许管理员在重置命令不当使用的情况下检索玩家的旧岛屿。
    #   管理员可以通过将他注册到它来重新添加玩家到他的旧岛屿。
    # * 如果设置为 'false'，每当玩家重置他的岛屿时，他的前一个岛屿将从世界中删除。
    #   这是默认行为。
    # 自 1.13.0 版本添加。
    keep-previous-island-on-reset: true
```


## 高级配置

### config.yml
配置与 BSkyBlock, AcidIsland 等非常相似。

每个玩家都将拥有自己的土地，直到岛屿距离值的限制。默认值是 400，所以土地将是 800 x 800 块。土地是半随机的，但每个玩家将获得大致相同的布局（参见生物群系配置）。结构如村庄、破损的下界门、沉船等是随机的，因此有些玩家可能会得到它们，有些则不会。在未来版本中，关闭结构将是一个配置选项。要塞被关闭，不存在。每个玩家的土地被不同温度的海洋包围。如果边界不是固体的，那么玩家理论上可以探索其他土地。

*世界种子*
世界种子是用来生成土地的。我建议保留这个值。如果你改变它，土地可能会非常不同。

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

## 命令

命令可以在[这里](Commands)找到。

## 占位符

占位符可以在[这里](Placeholders)找到。

## 翻译

{{ translations("Boxed") }}