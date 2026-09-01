# BentoBox 蓝图规范

**第1版**

!!! warning "已被取代"
    本页面仅供历史参考。当前完整的规范——包括蓝图、方块、实体和包的每个字段，加上用于验证的已发布 JSON 模式——是[蓝图文件格式](Blueprint-Format.md)页面。

本文档中的关键词"MUST"、"MUST NOT"、"REQUIRED"、"SHALL"、"SHALL NOT"、"SHOULD"、"SHOULD NOT"、"RECOMMENDED"、"MAY"和"OPTIONAL"应按照[RFC 2119](http://www.ietf.org/rfc/rfc2119.txt)中的描述进行解释。

## 简介

此规范定义了一种格式，该格式描述[Minecraft](https://minecraft.net)世界的一个区域（由方块和实体组成），用于序列化并存储到磁盘或基于JSON的数据库。它的设计目的是允许平台、版本和各种修改状态之间的最大跨兼容性。

BentoBox蓝图格式的目标是让我们能够将Minecraft世界的区域序列化到磁盘或任何用户选择的存储方法，以便稍后放回世界中，同时避免依赖第三方软件或插件来提供序列化和反序列化功能。

## 修订历史

| 版本 | 日期 | BentoBox 版本 | 描述
|---|---|---|---|
| 1 | 2019-06-09 | [1.5.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/1.5.0) | 初始版本，源自 BentoBox Schem 格式
| 1.1 | 2026 | 2.x | 存储格式从压缩二进制文件转为扁平json；`.blueprint`现在是主要扩展名；旧版本`.blu`(压缩过的)为了向上兼容保持可加载 |

## 定义

### <a name="defMaterial"></a>材质（Material）

[Material](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html) 是由 [Bukkit API](https://dev.bukkit.org/) 提供的一个ID，定义了方块或物品的实际类型。它影响客户端的各种渲染选项，例如光线、透明度或显示效果。它们代表实际对应 NamespacedKey 的编程快捷方式。

## 规范

### 格式

本规范所指定的结构，将使用 [JavaScript Object Notation](https://json.org/)（JSON）格式持久化存储到用户所选的存储方式中。自 BentoBox 2.x 起，蓝图文件以**扁平（未压缩）JSON**格式存储，文件扩展名为 .blueprint。

旧版蓝图文件使用压缩后的二进制格式，扩展名为 .blu。为保持向后兼容性，BentoBox 将继续支持加载 .blu 文件，但所有新保存的蓝图将使用 .blueprint 纯 JSON 格式。

使用本规范的文件必须使用以下文件扩展名之一：

* `.blueprint` — 纯 JSON（当前推荐）
* `.blu` — 压缩 JSON（旧版）

本规范中的所有字段名均**区分大小写**。

### 模式

#### 字段

| 字段名 | 类型 | 描述 |
|---|---|---|
| name | `String` | 蓝图的显示名称 |
| icon | `String` | 代表蓝图在游戏中的图标的物品的[材质](#defMaterial) |
| attached | `Array` | |
| entities | `Array` | |
| blocks | `Array` | |
| xSize | `integer` | |
| ySize | `integer` | |
| zSize | `integer` | |
| bedrock | `Array` | |