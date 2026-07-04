# BentoBox 蓝图规范

**第1版**

本文档中的关键词"MUST"、"MUST NOT"、"REQUIRED"、"SHALL"、"SHALL NOT"、"SHOULD"、"SHOULD NOT"、"RECOMMENDED"、"MAY"和"OPTIONAL"应按照[RFC 2119](http://www.ietf.org/rfc/rfc2119.txt)中的描述进行解释。

## 简介

此规范定义了一种格式，该格式描述[Minecraft](https://minecraft.net)世界的一个区域（由方块和实体组成），用于序列化并存储到磁盘或基于JSON的数据库。它的设计目的是允许平台、版本和各种修改状态之间的最大跨兼容性。

BentoBox蓝图格式的目标是让我们能够将Minecraft世界的区域序列化到磁盘或任何用户选择的存储方法，以便稍后放回世界中，同时避免依赖第三方软件或插件来提供序列化和反序列化功能。

## 修订历史

| 版本 | 日期 | BentoBox 版本 | 描述
|---|---|---|---|
| 1 | 2019-06-09 | [1.5.0](https://github.com/BentoBoxWorld/BentoBox/releases/tag/1.5.0) | 初始版本，源自 BentoBox Schem 格式

## 定义

### <a name="defMaterial"></a>材质（Material）

[Material](https://hub.spigotmc.org/javadocs/spigot/org/bukkit/Material.html) 是由 [Bukkit API](https://dev.bukkit.org/) 提供的一个ID，定义了方块或物品的实际类型。它影响客户端的各种渲染选项，例如光线、透明度或显示效果。它们代表实际对应 NamespacedKey 的编程快捷方式。

## 规范

### 格式

由本规范指定的结构使用[JavaScript 对象表示法](https://json.org)（JSON）格式持久化到用户选择的存储方法。数据必须使用...数据压缩算法进行压缩。

使用此规范的文件必须使用以下文件扩展名之一：
* `.blueprint` ;
* `.blu`

规范中的所有字段名称都**区分大小写**。

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