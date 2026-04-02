# 欢迎来到 BentoBox 开发者文档！

BentoBox 是一个平台插件，支持一套可在其上运行的插件 API。其架构与 Bukkit 插件系统几乎相同。你可以创建像 BSkyBlock 这样的游戏模式插件，为玩家提供你自己的游戏模式体验，或者你可以开发实用程序插件，如 Warps，使任何游戏模式（甚至普通世界）中的玩家都可以使用传送牌。

## Pladdons

由于服务器运作方式的改变（代码在加载时的重新映射），现在建议所有插件现在都在 Bukkit 插件包装器内运行，该包装器由 BentoBox 提供，称为 Pladdon -
Pladdons = Plugin + Addon。通过成为插件，它们在加载时将被正确重新映射，这对于 Paper 等服务器很重要。

Pladdon 包装器的任务是生成附加组件实例，并在通过 `getAddon` 方法请求时提供它。

由于附加组件是插件，它们将被服务器列为插件，但它们仍应放在 `Bentobox/Addons` 文件夹中。

# JavaDocs

Javadocs 在这里：[https://javadocs.bentobox.world](https://ci.codemc.io/job/BentoBoxWorld/job/BentoBox/javadoc/)

核心 API 包是 world.bentobox.bentobox.api.\*。这些包中的方法会尽可能长期保持稳定。api 包之外的方法和类可能会频繁或大幅度改变。

# 示例插件

@BONNe 在这里维护了一个示例插件：[https://github.com/BONNePlayground/ExampleAddon](https://github.com/BONNePlayground/ExampleAddon)