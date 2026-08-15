# CaveBlock 权限

<table align='center'>
<tr>
<td align='left'><b>权限</b></td>
<td align='left'><b>启用给</b></td>  
<td align='left'><b>描述</b></td>
</tr>
<tr>
<td align='left'>caveblock.admin.clearresetall</td>
<td align='left'>op</td>
<td align='left'>允许清除所有玩家的洞穴重置限制</td>
</tr>
<tr>
<td align='left'>caveblock.admin.delete</td>
<td align='left'>op</td>
<td align='left'>让玩家完全删除一个玩家（包括洞穴）</td>
</tr>
<tr>
<td align='left'>caveblock.admin.deleteisland</td>
<td align='left'>op</td>
<td align='left'>让玩家完全移除他所在的洞穴</td>
</tr>
<tr>
<td align='left'>caveblock.admin.noban</td>
<td align='left'>op</td>
<td align='left'>玩家不能被洞穴封禁</td>
</tr>
<tr>
<td align='left'>caveblock.admin.purge</td>
<td align='left'>op</td>
<td align='left'>让玩家清除旧的洞穴</td>
</tr>
<tr>
<td align='left'>caveblock.admin.register</td>
<td align='left'>op</td>
<td align='left'>让玩家将最近的洞穴注册给另一个玩家</td>
</tr>
<tr>
<td align='left'>caveblock.admin.reload</td>
<td align='left'>op</td>
<td align='left'>重新加载 config.yml</td>
</tr>
<tr>
<td align='left'>caveblock.admin.reserve</td>
<td align='left'>op</td>
<td align='left'>为玩家的下一个洞穴保留一个空位</td>
</tr>
<tr>
<td align='left'>caveblock.admin.setlanguage</td>
<td align='left'>op</td> 
<td align='left'>重置所有玩家语言并设置默认语言</td>
</tr>
<tr>
<td align='left'>caveblock.admin.setspawn</td>
<td align='left'>op</td>
<td align='left'>允许使用出生点工具</td>
</tr>
<tr>
<td align='left'>caveblock.admin.setrange</td>
<td align='left'>op</td>
<td align='left'>允许设置洞穴保护范围</td>
</tr>
<tr>
<td align='left'>caveblock.admin.settingsreset</td>
<td align='left'>op</td>
<td align='left'>将所有洞穴重置为默认保护设置</td>
</tr>
<tr>
<td align='left'>caveblock.admin.unregister</td>
<td align='left'>op</td> 
<td align='left'>在不删除洞穴方块的情况下从洞穴中删除玩家</td>
</tr>
<tr>
<td align='left'>caveblock.mod.bypasscooldowns</td>
<td align='left'>op</td>
<td align='left'>允许管理员绕过冷却时间</td>
</tr>
<tr>
<td align='left'>caveblock.mod.bypassexpel</td>
<td align='left'>op</td>
<td align='left'>允许管理员绕过洞穴驱逐</td>
</tr>
<tr>
<td align='left'>caveblock.mod.bypasslock</td>
<td align='left'>op</td>  
<td align='left'>绕过洞穴锁定</td>
</tr>
<tr>
<td align='left'>caveblock.mod.bypassprotect</td>
<td align='left'>op</td>
<td align='left'>允许管理员绕过洞穴保护</td> 
</tr>
<tr>
<td align='left'>caveblock.mod.clearreset</td>
<td align='left'>false</td>
<td align='left'>允许清除洞穴重置限制</td>
</tr>
<tr>
<td align='left'>caveblock.mod.info</td>
<td align='left'>op</td>
<td align='left'>让管理员查看玩家的信息</td>
</tr>
<tr>
<td align='left'>caveblock.mod.lock</td>
<td align='left'>op</td>
<td align='left'>锁定或解锁洞穴</td>
</tr>
<tr>
<td align='left'>caveblock.mod.name</td>
<td align='left'>false</td>
<td align='left'>允许为玩家的洞穴命名</td>
</tr>
<tr>
<td align='left'>caveblock.mod.resethome</td>
<td align='left'>op</td>
<td align='left'>允许设置或重置玩家的家的位置</td>
</tr>
<tr>
<td align='left'>caveblock.mod.resetname</td>
<td align='left'>false</td>
<td align='left'>允许重置玩家的洞穴名称</td>
</tr>
<tr>
<td align='left'>caveblock.mod.team</td>
<td align='left'>false</td> 
<td align='left'>允许通过踢出和添加指令修改团队</td>
</tr>
<tr>
<td align='left'>caveblock.mod.tp</td>
<td align='left'>op</td>
<td align='left'>允许传送到洞穴</td>
</tr>
<tr>
<td align='left'>caveblock.skywalker</td>
<td align='left'>op</td>
<td align='left'>允许玩家在高度限制之上行走</td>
</tr>
<tr>
<td align='left'>caveblock.island</td>
<td align='left'>true</td>
<td align='left'>允许使用 <b>/cave</b> 指令</td>
</tr>
<tr>
<td align='left'>caveblock.island.ban</td>
<td align='left'>true</td>
<td align='left'>允许封禁访客</td>
</tr>
<tr>
<td align='left'>caveblock.island.create</td>
<td align='left'>true</td>
<td align='left'>允许创建洞穴</td>
</tr>
<tr>
<td align='left'>caveblock.island.expel</td>
<td align='left'>true</td>
<td align='left'>允许驱逐访客</td>
</tr>
<tr>
<td align='left'>caveblock.island.home</td>
<td align='left'>true</td>
<td align='left'>允许传送到玩家的洞穴</td>
</tr>
<tr>
<td align='left'>caveblock.island.info</td>
<td align='left'>true</td>
<td align='left'>让玩家使用岛屿信息指令</td>
</tr>
<tr>
<td align='left'>caveblock.island.language</td>
<td align='left'>true</td>
<td align='left'>玩家可以选择语言</td>
</tr>
<tr>
<td align='left'>caveblock.island.lock</td>
<td align='left'>false</td>
<td align='left'>允许锁定洞穴</td>
</tr>
<tr>
<td align='left'>caveblock.island.name</td>
<td align='left'>true</td>
<td align='left'>玩家可以设置洞穴的名称</td>
</tr>
<td align='left'>caveblock.island.number</td>
<td align='left'>false</td>
<td align='left'>x 设置玩家可以创建的洞穴数量。</td>
</tr>
<tr>
<td align='left'>caveblock.island.reset</td>
<td align='left'>true</td>
<td align='left'>玩家可以使用洞穴重置或重启指令</td>
</tr>
<tr>
<td align='left'>caveblock.island.sethome</td>
<td align='left'>true</td>
<td align='left'>让玩家设置他们的洞穴传送点</td>
</tr>
<tr>
<td align='left'>caveblock.island.settings</td>
<td align='left'>true</td>
<td align='left'>玩家可以查看服务器设置</td>
</tr>
<tr>
<td align='left'>caveblock.island.spawn</td>
<td align='left'>true</td>
<td align='left'>如果出生点存在，玩家可以使用洞穴出生点指令</td>
</tr>
<tr>
<td align='left'>caveblock.island.team</td>
<td align='left'>true</td>
<td align='left'>让玩家使用团队指令</td>
</tr>
<tr>
<td align='left'>caveblock.island.team.coop</td>
<td align='left'>true</td>
<td align='left'>让玩家使用团队合作指令</td> 
</tr>
<tr>
<td align='left'>caveblock.island.team.trust</td>
<td align='left'>true</td>
<td align='left'>让玩家使用团队信任指令</td>
</tr>
<tr>
<td align='left'>caveblock.settings.*</td>
<td align='left'>true</td>
<td align='left'>允许在洞穴上使用设置</td>
</tr>
<tr>
<td align='left'>caveblock.team.maxsize.[NUMBER]</td>
<td align='left'>false</td>
<td align='left'>让玩家获得比默认值更大的团队规模。</td>
</tr>
<tr>
<td align='left'>caveblock.island.maxhomes.[NUMBER]</td>
<td align='left'>false</td>
<td align='left'>让玩家获得比默认值更多的家。</td>
</tr>
<tr>
<td align='left'>caveblock.island.range.[NUMBER]</td>
<td align='left'>false</td> 
<td align='left'>让玩家获得比默认值更大的保护范围。</td>
</tr>
</table>
