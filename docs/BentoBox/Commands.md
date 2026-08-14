BentoBox 实现了一些指令来帮助您管理整个 BentoBox 安装。

**可用指令（截至 2.2.0 版）**

| 指令                                     | 权限                        | 描述                                                       |
|-----------------------------------------|------------------------------|------------------------------------------------------------|
| /bentobox [help/h]                      | bentobox.admin               | 显示所有可用的 BentoBox 指令                               |
| /bentobox about                         | bentobox.about               | 显示版权和许可信息                                         |
| /bentobox catalog                       | bentobox.admin.catalog       | 显示目录                                                   |
| /bentobox locale                        | bentobox.admin.locale        | 执行本地化文件分析                                         |
| /bentobox manage/overview               | bentobox.admin.manage        | 显示管理面板                                               |
| /bentobox migrate                       | bentobox.admin.migrate       | 从一个数据库迁移数据到另一个                               |
| /bentobox perms                         | bentobox.admin.perms         | 以 YAML 格式显示 BentoBox 和插件的有效权限                |
| /bentobox rank [list \| add \| remove] [rank reference] [rank value] | bentobox.admin.rank | 列出、添加或移除等级                                  |
| /bentobox reload/rl                     | bentobox.admin.reload        | 重新加载 BentoBox 和所有插件、设置和本地化文件            |
| /bentobox version/v/versions/addons     | bentobox.version             | 显示 BentoBox 和插件版本                                   |

`/bentobox` 的别名是 `/bbox`。

在提交错误报告或寻求支持时，**必须**提供 `/bentobox version` 指令的输出，以便我们了解您正在使用的软件、数据库和插件的版本。