# 🍱 BentoBox 文档（中文）

欢迎来到 BentoBox 中文文档的官方源码仓库。本仓库包含所有原始文档文件（Markdown 格式），用于构建官方中文文档网站。

-----

## 📖 阅读文档

已发布的最新文档可在以下地址查阅：

**[https://docs.bentobox.world](https://docs.bentobox.world)**

> 如果你只是想阅读文档或获取 BentoBox 的帮助，请访问上方链接。本仓库供**贡献**文档使用。

英文参考文档位于主仓库：[BentoBoxWorld/docs](https://github.com/BentoBoxWorld/docs)。

-----

## 🌐 关于本翻译

本仓库包含 BentoBox 文档的中文简体翻译，涵盖以下内容：

- BentoBox 核心文档
- 游戏模式（AcidIsland、AOneBlock、BSkyBlock、CaveBlock 等）
- 附加插件（Bank、Border、Challenges、Level、Limits、Warps 等）
- 开发者教程

翻译内容会定期与英文主文档同步。如果发现内容缺失或过时，欢迎贡献！

-----

## 🤝 参与贡献

我们欢迎各种形式的贡献，无论是修正一个错别字还是翻译整篇新指南，你的帮助都能让所有中文用户获益。

### 贡献方式

1. **Fork** 本仓库到你的 GitHub 账户。
2. **创建新分支**用于你的修改（例如 `fix/修正配置说明` 或 `feat/翻译xyz插件`）。
3. **编辑** Markdown 文件。
4. **提交并推送**你的修改到你的 fork。
5. 从你的分支向本仓库的 `master` 分支**发起 Pull Request（PR）**。

### 翻译注意事项

- 保留技术名称的英文原文：命令名（如 `/island`）、YAML 键名（如 `disabled-gamemodes`）、Java 类名、MkDocs 宏（如 `{{ addon_description("Level") }}`）。
- 翻译章节标题、描述和解释性文字。
- 保持现有的 Markdown 格式（代码块、admonition 提示块、表格）。

-----

## 🚀 自动发布流程

本仓库与 **[ReadTheDocs](https://readthedocs.org/)** 服务相连，负责构建和部署流程。

- **每次提交/合并时：** 当新的提交推送到 `master` 分支时，会触发 ReadTheDocs 的 webhook。
- **构建：** ReadTheDocs 拉取最新修改，将 Markdown 文件编译为静态 HTML 网站。
- **发布：** 构建成功后，新版本文档自动上线。

你的贡献将在 Pull Request 合并后几分钟内出现在文档网站上。

## 📄 许可证

BentoBox 文档（本仓库）的文字和内容采用 **[知识共享 署名-相同方式共享 4.0 国际许可协议（CC BY-SA 4.0）](https://creativecommons.org/licenses/by-sa/4.0/deed.zh)** 授权。

文档中包含的代码片段，除非另有说明，均采用 **[MIT 许可证](https://opensource.org/licenses/MIT)** 授权。
