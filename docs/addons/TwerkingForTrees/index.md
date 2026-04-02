# TwerkingForTrees

**TwerkingForTrees** 可以让你的玩家通过扭动来更快地种植树木。

由 [tastybento](https://github.com/tastybento) 创建和维护。

{{ addon_description("TwerkingForTrees") }}

## 安装

1. 将插件 jar 文件放入 BentoBox 插件的 addons 文件夹

2. 重启服务器

3. 在你的岛屿上种植树木

4. 扭动,扭动,再扭动...

5. 树木长大了!

## 配置文件

```
# TwerkingForTrees 配置文件。
#
# 玩家必须扭动多少次才能让树木开始更快生长。
# 如果玩家扭动次数不够,树木将不会更快生长。
minimum-twerks: 4

sounds:
  # 开启/关闭声音。
  enabled: true
  
  twerk:
    # 当玩家扭动足够次数,树苗开始更快生长时播放的声音。
    # 可用的声音如下:
    # https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Sound.html
    sound: BLOCK_NOTE_BLOCK_BASS
    volume: 1.0
    pitch: 2.0
  
  growing-small-tree:
    # 当小树 (1x1) 生长时播放的声音。
    # 可用的声音如下:
    # https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Sound.html
    sound: BLOCK_BUBBLE_COLUMN_UPWARDS_AMBIENT
    volume: 1.0
    pitch: 1.0
  
  growing-big-tree:
    # 当大树 (2x2) 生长时播放的声音。
    # 可用的声音如下:
    # https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Sound.html
    sound: BLOCK_BUBBLE_COLUMN_UPWARDS_AMBIENT
    volume: 1.0  
    pitch: 1.0

effects:
  # 开启/关闭粒子效果。
  enabled: true
  
  # 每次玩家扭动时播放的效果。
  # 可用的效果如下:
  # https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Effect.html
  twerk: MOBSPAWNER_FLAMES
```