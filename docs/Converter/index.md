# ASkyBlock 转 BSkyBlock 转换器插件

## 兼容性

转换器应与最新版本的 BentoBox 和 BSkyBlock 配合使用。转换器是一个插件，你需要下载后放入 BentoBox 的 addons 文件夹中。运行转换前，请阅读以下全部说明。

## 简介

转换器会读取 ASkyBlock 的数据文件，并在 BSkyBlock/BentoBox 数据库中创建新版本。以下内容会被转换：

* 玩家和团队
* 岛屿
* 传送点
* 大部分 Config.yml 设置
* 挑战

以下内容不会被转换：

* 结构文件（Schematics）——BSkyBlock 不支持，请改用 BentoBox 蓝图。
* 生态区——BSkyBlock 本身不支持，请改用 Biome 插件。
* 魔法圆石——BSkyBlock 本身不支持，相应的插件正在开发中。
* 酸水或酸雨设置——BSkyBlock 不支持。
* 团队聊天——BSkyBlock 不支持。
* 合作关系转换——BSkyBlock 中合作关系的处理方式不同，玩家需要手动重新设置。
* 等级相关设置——BSkyBlock 本身不支持，请使用 Level 插件。

## 备份

**警告！** 本软件按“原样”提供，不附带任何担保。使用风险自负，请务必备份你的服务器文件和文件夹。这一点非常重要！

## 转换准备

**注意：** 除了服务器升级到最新版本外，ASkyBlock 世界不会被做任何更改。转换后你使用的仍然是与之前 BSkyBlock 相同的世界，也就是说世界名称保持不变。

如果你当前的服务器运行在 1.12.2 版本，则必须先将服务器升级到最新版本的 Minecraft。

## 步骤

**注意：** 如果你的世界很大，你需要调整服务器的超时时间，以免看门狗计时器（watchdog timer）在转换过程中终止服务器。

*你已经记得备份数据了吧？*

0. 编辑 spigot.yml，将 **timeout-time:** 改为较大的值，例如 60000，以防止看门狗计时器在转换期间终止服务器。
1. 停止服务器，并将 Spigot 1.14.4（或更高版本）的服务器 jar 文件添加到服务器文件夹中。
2. 从 plugins 文件夹中移除 ASkyBlock.jar。**不要**移除 ASkyBlock 文件夹或世界。
3. 将 BentoBox 1.12.0（或更高版本）安装到 plugins 文件夹中。
4. 使用 **--forceUpgrade** 选项启动新服务器。这将把你所有的世界升级为新格式。
5. 在一切完全加载完毕并看到 BentoBox 的 logo 后，停止服务器。
6. 将 **BSkyBlock** 插件、**Challenges** 插件、**Warps** 插件和 **Converter** 插件放入 BentoBox 的 addons 文件夹中。
7. 再次使用 **--forceUpgrade** 选项重启服务器。
8. 服务器加载完毕并看到 BentoBox 的 logo 后，在控制台输入 **bsb convert** 开始转换。
9. 转换完成后，停止服务器。**非常重要：请停止服务器！不要重载（reload）！！！** 这样才能正确注册世界生成器。
10. 根据需要编辑 BSkyBlock 的 config.yml 设置。
11. 编辑 spigot.yml，将 **timeout-time:** 改回较小的值，例如 60。
12. 移除转换器插件以及转换过程中创建的默认 BSkyBlock 世界文件夹。
13. 重启服务器。此后你不再需要使用 forceUpgrade 选项，BSkyBlock 插件将使用 ASkyBlock 的世界。

**注意：** BentoBox 使用 PAPI 或 MVdW 来处理占位符。如果你对占位符感兴趣，请阅读占位符相关文档。

**注意：** Challenges 和 Warps 并非必需。转换器在没有它们的情况下也能运行，但相应的数据不会被转换。
