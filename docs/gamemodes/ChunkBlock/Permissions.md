# ChunkBlock 权限

每个 ChunkBlock 权限有前缀 `chunkblock.`。默认被选择所以一个香草安装玩意图的游戏没有权限插件：玩家需要的一切是 `true`，管理工具是 OP，两个会改变游戏本身的节点——阶段 GUI 和区块锁定绕过——直到你授予它们才关闭。

!!! warning "`chunkblock.mod.bypasschunks` 故意不是一个 OP 默认"
    它豁免持有者来自区块锁定完全并启用 `/chadmin bypass`。它的默认是 `false`，**不是** `op`，所以员工遵循与每个人相同的规则直到你明确在你的权限插件中授予它。

    它是一个单独的节点来自 `chunkblock.mod.bypasslock`，这是 BentoBox 的岛屿 *lock* 绕过和对区块锁做任何事。

!!! note "两个节点默认是关闭的"
    - `chunkblock.phases` ——`/ch phases` GUI。授予它如果你想要玩家浏览和重放阶段。
    - `chunkblock.island.setcount` ——重放一个阶段。OP 只有默认，阶段 GUI 检查它在提供 *"点击改变"* 前。

## ChunkBlock 特定权限

| 权限 | 描述 | 默认 |
|------------|-------------|---------|
| `chunkblock.admin.chunks` | 允许使用 '/chadmin chunks' 命令 - 检查、设置或重新计算玩家的解锁区块 | OP |
| `chunkblock.admin.phases` | 允许使用 '/chadmin phases' 命令 - 打开阶段顺序编辑器 | OP |
| `chunkblock.admin.sanity` | 允许使用 '/chadmin sanity' 命令 - 在控制台中显示阶段概率的清理检查 | OP |
| `chunkblock.admin.setchest` | 允许使用 '/chadmin setchest' 命令 - 把看着的箱子放在一个阶段带指定稀有性 | OP |
| `chunkblock.admin.setcount` | 允许使用 '/chadmin setcount' 命令 - 设置玩家的方块数 | OP |
| `chunkblock.count` | 允许使用 '/ch count' 命令 - 显示方块数和阶段 | `true` |
| `chunkblock.island.actionbar` | 允许使用 '/ch actionbar' 命令 - 切换动作栏 | `true` |
| `chunkblock.island.bossbar` | 允许使用 '/ch bossbar' 命令 - 切换 BOSS 栏 | `true` |
| `chunkblock.island.chunks` | 允许使用 '/ch chunks' 命令 - 显示你的解锁区块和领地地图 | `true` |
| `chunkblock.island.setcount` | 允许使用 '/ch setCount' 命令 - 设置方块数到以前完成的值 | OP |
| `chunkblock.mod.bypasschunks` | 豁免持有者来自区块锁定完全；也允许 '/chadmin bypass' 来切换它。不默认授予运维人员 - 它必须被明确授予所以员工在他们选择加入前遵循同样的规则。 | `false` |
| `chunkblock.phases` | 允许使用 '/ch phases' 命令 - 显示所有阶段的列表 | `false` |
| `chunkblock.respawn-block` | 允许使用 '/ch respawnBlock' 命令 - 在他们消失的情况下重生魔法方块 | `true` |

## 完整列表

| 权限 | 描述 | 默认 |
|------------|-------------|---------|
| `chunkblock.admin` | 允许使用 '/chadmin' 命令 - 管理命令 | OP |
| `chunkblock.admin.blueprint` | 允许使用 '/chadmin blueprint' 命令 - 操纵蓝图 | OP |
| `chunkblock.admin.blueprint.copy` | 允许使用 '/chadmin blueprint copy' 命令 - 复制由 pos1 和 pos2 设置的剪贴板并可选地空气方块 | OP |
| `chunkblock.admin.blueprint.delete` | 允许使用 '/chadmin blueprint delete' 命令 - 删除蓝图 | OP |
| `chunkblock.admin.blueprint.list` | 允许使用 '/chadmin blueprint list' 命令 - 列出可用蓝图 | OP |
| `chunkblock.admin.blueprint.load` | 允许使用 '/chadmin blueprint load' 命令 - 加载蓝图到剪贴板 | OP |
| `chunkblock.admin.blueprint.origin` | 允许使用 '/chadmin blueprint origin' 命令 - 设置蓝图的起点到你的位置 | OP |
| `chunkblock.admin.blueprint.paste` | 允许使用 '/chadmin blueprint paste' 命令 - 粘贴剪贴板到你的位置 | OP |
| `chunkblock.admin.blueprint.pos1` | 允许使用 '/chadmin blueprint pos1' 命令 - 设置立方体剪贴板的第 1 个角 | OP |
| `chunkblock.admin.blueprint.pos2` | 允许使用 '/chadmin blueprint pos2' 命令 - 设置立方体剪贴板的第 2 个角 | OP |
| `chunkblock.admin.blueprint.rename` | 允许使用 '/chadmin blueprint rename' 命令 - 重命名蓝图 | OP |
| `chunkblock.admin.blueprint.save` | 允许使用 '/chadmin blueprint save' 命令 - 保存复制的剪贴板 | OP |
| `chunkblock.admin.chunks` | 允许使用 '/chadmin chunks' 命令 - 检查、设置或重新计算玩家的解锁区块 | OP |
| `chunkblock.admin.deaths` | 允许使用 '/chadmin deaths' 命令 - 编辑玩家的死亡 | OP |
| `chunkblock.admin.deaths.add` | 允许使用 '/chadmin deaths add' 命令 - 添加死亡到玩家 | OP |
| `chunkblock.admin.deaths.remove` | 允许使用 '/chadmin deaths remove' 命令 - 从玩家移除死亡 | OP |
| `chunkblock.admin.deaths.reset` | 允许使用 '/chadmin deaths reset' 命令 - 重置玩家的死亡 | OP |
| `chunkblock.admin.deaths.set` | 允许使用 '/chadmin deaths set' 命令 - 设置玩家的死亡 | OP |
| `chunkblock.admin.delete` | 允许使用 '/chadmin delete' 命令 - 删除玩家的岛屿 | OP |
| `chunkblock.admin.getrank` | 允许使用 '/chadmin getrank' 命令 - 获得玩家在他们的岛屿或所有者的岛屿上的排名 | OP |
| `chunkblock.admin.noban` | 玩家不能从岛屿被禁止 | OP |
| `chunkblock.admin.noexpel` | 玩家不能从岛屿被驱逐 | OP |
| `chunkblock.admin.phases` | 允许使用 '/chadmin phases' 命令 - 打开阶段顺序编辑器 | OP |
| `chunkblock.admin.purge` | 允许使用 '/chadmin purge' 命令 - 清理被遗弃超过 [days] 的岛屿 | OP |
| `chunkblock.admin.purge.protect` | 允许使用 '/chadmin purge protect' 命令 - 切换岛屿清理保护 | OP |
| `chunkblock.admin.purge.status` | 允许使用 '/chadmin purge status' 命令 - 显示清理的状态 | OP |
| `chunkblock.admin.purge.stop` | 允许使用 '/chadmin purge stop' 命令 - 停止正在进行的清理 | OP |
| `chunkblock.admin.purge.unowned` | 允许使用 '/chadmin purge unowned' 命令 - 清理无主岛屿 | OP |
| `chunkblock.admin.range` | 允许使用 '/chadmin range' 命令 - 管理岛屿范围命令 | OP |
| `chunkblock.admin.range.add` | 允许使用 '/chadmin range add' 命令 - 增加岛屿保护范围 | OP |
| `chunkblock.admin.range.display` | 允许使用 '/chadmin range display' 命令 - 显示/隐藏岛屿范围指示器 | OP |
| `chunkblock.admin.range.remove` | 允许使用 '/chadmin range remove' 命令 - 减少岛屿保护范围 | OP |
| `chunkblock.admin.range.reset` | 允许使用 '/chadmin range reset' 命令 - 重置岛屿保护范围到世界默认 | OP |
| `chunkblock.admin.range.set` | 允许使用 '/chadmin range set' 命令 - 设置岛屿保护范围 | OP |
| `chunkblock.admin.register` | 允许使用 '/chadmin register' 命令 - 向无主岛屿注册玩家 | OP |
| `chunkblock.admin.reload` | 允许使用 '/chadmin reload' 命令 - 重新加载 | OP |
| `chunkblock.admin.resetflags` | 允许使用 '/chadmin resetflags' 命令 - 重置所有岛屿到 config.yml 中的默认标志设置 | OP |
| `chunkblock.admin.resets` | 允许使用 '/chadmin resets' 命令 - 编辑玩家重置值 | OP |
| `chunkblock.admin.resets.add` | 允许使用 '/chadmin resets add' 命令 - 添加这个玩家的岛屿重置计数 | OP |
| `chunkblock.admin.resets.remove` | 允许使用 '/chadmin resets remove' 命令 - 减少玩家的岛屿重置计数 | OP |
| `chunkblock.admin.resets.set` | 允许使用 '/chadmin resets set' 命令 - 设置这个玩家重置了多少次他的岛屿 | OP |
| `chunkblock.admin.sanity` | 允许使用 '/chadmin sanity' 命令 - 在控制台中显示阶段概率的清理检查 | OP |
| `chunkblock.admin.setchest` | 允许使用 '/chadmin setchest' 命令 - 把看着的箱子放在一个阶段带指定稀有性 | OP |
| `chunkblock.admin.setcount` | 允许使用 '/chadmin setcount' 命令 - 设置玩家的方块数 | OP |
| `chunkblock.admin.setprotectionlocation` | 允许使用 '/chadmin setprotectionlocation' 命令 - 设置当前位置或 [x y z] 作为岛屿保护区域的中心 | OP |
| `chunkblock.admin.setrank` | 允许使用 '/chadmin setrank' 命令 - 设置玩家在他们的岛屿或所有者的岛屿上的排名 | OP |
| `chunkblock.admin.setspawn` | 允许使用 '/chadmin setspawn' 命令 - 设置岛屿作为这个游戏模式的出生点 | OP |
| `chunkblock.admin.setspawnpoint` | 允许使用 '/chadmin setspawnpoint' 命令 - 设置当前位置作为这个岛屿的出生点 | OP |
| `chunkblock.admin.settings` | 允许使用 '/chadmin settings' 命令 - 打开设置 GUI 或设置设置 | OP |
| `chunkblock.admin.tp` | 允许使用 '/chadmin tp/tpnether/tpend' 命令 - 传送到玩家的岛屿 | OP |
| `chunkblock.admin.unregister` | 允许使用 '/chadmin unregister' 命令 - 从岛屿取消注册所有者，但保持岛屿方块 | OP |
| `chunkblock.admin.version` | 允许使用 '/chadmin version' 命令 - 显示 BentoBox 和附属插件版本 | OP |
| `chunkblock.admin.why` | 允许使用 '/chadmin why' 命令 - 切换控制台保护调试报告 | OP |
| `chunkblock.count` | 允许使用 '/ch count' 命令 - 显示方块数和阶段 | `true` |
| `chunkblock.island` | 允许使用 '/ch' 命令 - 主岛屿命令 | `true` |
| `chunkblock.island.actionbar` | 允许使用 '/ch actionbar' 命令 - 切换动作栏 | `true` |
| `chunkblock.island.ban` | 允许使用 '/ch ban' 或 '/ch unban' 或 '/ch banlist' 命令 - 被禁止的玩家 | `true` |
| `chunkblock.island.bossbar` | 允许使用 '/ch bossbar' 命令 - 切换 BOSS 栏 | `true` |
| `chunkblock.island.chunks` | 允许使用 '/ch chunks' 命令 - 显示你的解锁区块和领地地图 | `true` |
| `chunkblock.island.create` | 允许使用 '/ch create' 命令 - 创建岛屿，使用可选蓝图（需要权限） | `true` |
| `chunkblock.island.deletehome` | 允许使用 '/ch deletehome' 命令 - 删除一个家位置 | OP |
| `chunkblock.island.expel` | 允许使用 '/ch expel' 命令 - 从你的岛屿驱逐玩家 | `true` |
| `chunkblock.island.home` | 允许使用 '/ch go' 命令 - 传送你到你的岛屿 | `true` |
| `chunkblock.island.homes` | 允许使用 '/ch homes' 命令 - 列出你的家 | OP |
| `chunkblock.island.info` | 允许使用 '/ch info' 命令 - 显示你的岛屿或玩家的岛屿的信息 | `true` |
| `chunkblock.island.language` | 允许使用 '/ch language' 命令 - 选择语言 | `true` |
| `chunkblock.island.lock` | 允许岛屿锁定在设置中 | `true` |
| `chunkblock.island.name` | 允许使用 '/ch setname' 或 '/ch resetname' 命令 - 你的岛屿名称 | `true` |
| `chunkblock.island.near` | 允许使用 '/ch near' 命令 - 显示你周围邻近岛屿的名称 | `true` |
| `chunkblock.island.renamehome` | 允许使用 '/ch renamehome' 命令 - 重命名一个家位置 | OP |
| `chunkblock.island.reset` | 允许使用 '/ch reset' 命令 - 重启你的岛屿并移除旧的 | `true` |
| `chunkblock.island.setcount` | 允许使用 '/ch setCount' 命令 - 设置方块数到以前完成的值 | OP |
| `chunkblock.island.sethome` | 允许使用 '/ch sethome' 命令 - 设置你的家传送点 | `true` |
| `chunkblock.island.settings` | 允许使用 '/ch settings' 命令 - 显示岛屿设置 | `true` |
| `chunkblock.island.spawn` | 允许使用 '/ch spawn' 命令 - 传送你到出生点 | `true` |
| `chunkblock.island.team` | 允许使用 '/ch team' 命令 - 管理你的团队 | `true` |
| `chunkblock.island.team.accept` | 允许使用 '/ch team accept' 命令 - 接受一个邀请 | `true` |
| `chunkblock.island.team.coop` | 允许使用 '/ch team coop、uncoop' 命令 | `true` |
| `chunkblock.island.team.invite` | 允许使用 '/ch team invite' 命令 - 邀请玩家加入你的岛屿 | `true` |
| `chunkblock.island.team.kick` | 允许使用 '/ch team kick' 命令 - 从你的岛屿移除成员 | `true` |
| `chunkblock.island.team.leave` | 允许使用 '/ch team leave' 命令 - 离开你的岛屿 | `true` |
| `chunkblock.island.team.promote` | 允许使用 '/ch team promote、demote' 命令 | `true` |
| `chunkblock.island.team.reject` | 允许使用 '/ch team reject' 命令 - 拒绝一个邀请 | `true` |
| `chunkblock.island.team.setowner` | 允许使用 '/ch team setowner' 命令 - 将你的岛屿所有权转移到一个成员 | `true` |
| `chunkblock.island.team.trust` | 允许使用 '/ch team trust、untrust' 命令 | `true` |
| `chunkblock.mod.bypassban` | 绕过岛屿禁止 | OP |
| `chunkblock.mod.bypasschunks` | 豁免持有者来自区块锁定完全；也允许 '/chadmin bypass' 来切换它。不默认授予运维人员 - 它必须被明确授予所以员工在他们选择加入前遵循同样的规则。 | `false` |
| `chunkblock.mod.bypasscooldowns` | 允许仲裁者绕过冷却 | OP |
| `chunkblock.mod.bypassdelays` | 允许仲裁者绕过延迟 | OP |
| `chunkblock.mod.bypassexpel` | 允许仲裁者绕过岛屿驱逐 | OP |
| `chunkblock.mod.bypasslock` | 绕过岛屿锁 | OP |
| `chunkblock.mod.bypassprotect` | 允许仲裁者绕过岛屿保护 | OP |
| `chunkblock.mod.clearreset` | 允许清除岛屿重置限制 | `false` |
| `chunkblock.mod.deletehomes` | 允许使用 '/chadmin deletehomes' 命令 - 从岛屿删除所有命名的家 | OP |
| `chunkblock.mod.info` | 允许使用 '/chadmin info' 命令 - 获得你在那里的信息或玩家的岛屿 | OP |
| `chunkblock.mod.lock` | 允许岛屿的锁定或解锁 | OP |
| `chunkblock.mod.resetname` | 允许使用 '/chadmin resetname' 命令 - 重置玩家岛屿名称 | OP |
| `chunkblock.mod.switch` | 允许使用 '/chadmin switch' 命令 - 打开/关闭保护绕过 | OP |
| `chunkblock.mod.team` | 允许使用 '/chadmin team' 命令 - 管理团队 | `false` |
| `chunkblock.mod.team.add` | 允许使用 '/chadmin team add' 或 '/chadmin add' 命令 - 添加玩家到所有者的团队 | OP |
| `chunkblock.mod.team.disband` | 允许使用 '/chadmin team disband' 或 '/chadmin disband' 命令 - 遣散所有者的团队 | OP |
| `chunkblock.mod.team.fix` | 允许使用 '/chadmin team fix' 或 '/chadmin fix' 命令 - 扫描和修复数据库中的跨岛屿成员身份 | OP |
| `chunkblock.mod.team.kick` | 允许使用 '/chadmin team kick' 或 '/chadmin kick' 命令 - 从团队踢出玩家 | OP |
| `chunkblock.mod.team.setowner` | 允许使用 '/chadmin team setowner' 命令 - 将岛屿所有权转移到玩家 | OP |
| `chunkblock.phases` | 允许使用 '/ch phases' 命令 - 显示所有阶段的列表 | `false` |
| `chunkblock.respawn-block` | 允许使用 '/ch respawnBlock' 命令 - 在他们消失的情况下重生魔法方块 | `true` |
| `chunkblock.settings.*` | 允许在岛屿上使用设置 | `true` |
