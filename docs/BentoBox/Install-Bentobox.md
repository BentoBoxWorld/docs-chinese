# 视频教程

[![视频缩略图](https://i.ytimg.com/vi/01MagYDuOCk/hqdefault.jpg?sqp=-oaymwEjCPYBEIoBSFryq4qpAxUIARUAAAAAGAElAADIQj0AgKJDeAE=&rs=AOn4CLCzVNO0ObSEMOOpYtUEtv4LjsMhBA)](https://www.youtube.com/watch?v=01MagYDuOCk)

# 简介

BentoBox 是一个功能强大的插件，安装方式与普通 Spigot 插件有所不同。它不仅仅是把 jar 文件拖进 `plugins/` 文件夹那么简单，但只需多花几分钟，就能解锁无数的玩法可能性——绝对值得。

让我们开始吧！

***

# 下载 BentoBox

你可以在不同的网站上**免费**下载 BentoBox。官方版本可以在插件的 Spigot 页面或 [GitHub `Releases` 选项卡](https://github.com/BentoBoxWorld/bentobox/releases)中找到，而**未经测试的**开发版本可以从 [Jenkins](https://ci.codemc.org/job/BentoBoxWorld/job/BentoBox/) 下载。

# 设置 BentoBox

下载 BentoBox 后，将其放入服务器的 `plugins` 文件夹即可。与 ASkyBlock 不同，BentoBox 没有必需的依赖项——它会自动检测并对接服务器上已安装的插件（如 Vault、PlaceholderAPI、Multiverse-Core 等），以扩展自身功能。

启动服务器并等待所有插件完全加载。连接到服务器后，你会发现 BentoBox 并没有做任何明显的事情——这是正常的。**BentoBox 本身只是一个平台**：它需要配合 [Addons](https://github.com/BentoBoxWorld/bentobox/wiki/Addons) 才能发挥作用，比如管理 Skyblock 游戏模式。

现在，关闭服务器。你可以查看 BentoBox 的 `config.yml` 文件。

# 安装附加组件

[Addons](/BentoBox/Addons) 是 BentoBox 的特色所在。但是，请注意，这些**不是插件**：如果你只是把它们放在 `plugins` 文件夹中，它们**不会启动**。

首先，下载你想要的附加组件。官方附加组件可以在 [BentoBoxWorld 的仓库列表](https://github.com/BentoBoxWorld) 中找到，从各自仓库的 `Releases` 选项卡下载（也可以从 [Jenkins](https://ci.codemc.org/job/BentoBoxWorld/) 获取**未经测试的**开发版本）。你也可以直接访问 [https://download.bentobox.world](https://download.bentobox.world) 一次性下载所有官方插件的整合包。

下载好所需的附加组件后，将它们全部放入 `plugins\BentoBox\addons` 文件夹，启动服务器以生成配置文件和目录，然后再次关闭服务器，方便在不影响服务器运行的情况下修改配置。

请注意，附加组件可能与某些 BentoBox 版本不兼容。官方附加组件**始终**会明确标注支持的版本范围。通常情况下，附加组件无需更新也能兼容更新的 BentoBox 版本。

# 结论

一切就绪！
感谢你选择我们的插件，希望你玩得开心——就像我们享受开发它一样。