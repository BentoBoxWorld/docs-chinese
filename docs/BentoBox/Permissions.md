# BentoBox 权限

此处列出的权限是 BentoBox 的权限。附加组件注册自己的权限。

**BentoBox 权限（截至 1.6.0）**

| 权限                   | 父权限            | 默认值 | 描述                          |
|------------------------|-------------------|--------|-------------------------------|
| bentobox.admin         |                   | op     | 允许使用大多数 BentoBox 命令    |
| bentobox.admin.catalog | bentobox.admin    | op     | 允许使用 /bentobox catalog    |
| bentobox.admin.locale  | bentobox.admin    | op     | 允许使用 /bentobox locale     |
| bentobox.admin.manage  | bentobox.admin    | op     | 允许使用 /bentobox manage     |
| bentobox.admin.migrate | bentobox.admin    | op     | 允许使用 /bentobox migrate    |
| bentobox.admin.reload  | bentobox.admin    | op     | 允许使用 /bentobox reload     |
| bentobox.about         |                   | true   | 允许使用 /bentobox about      |
| bentobox.version       |                   | true   | 允许使用 /bentobox version    |