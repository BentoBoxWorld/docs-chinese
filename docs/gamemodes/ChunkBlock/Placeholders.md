# ChunkBlock 占位符

ChunkBlock 注册从 AOneBlock 引擎继承的魔法方块占位符，所有有前缀 `chunkblock_`，加上它自己的五个领地占位符。

!!! tip "你可能想在你的记分板上的五个"
    - `%chunkblock_island_chunks%` ——拥有的区块
    - `%chunkblock_island_max_chunks%` ——上限
    - `%chunkblock_island_chunk_credit%` ——现在可花费的等级
    - `%chunkblock_island_next_chunk_level%` ——购买下一个区块的岛屿等级
    - `%chunkblock_island_ring%` ——领地从中心到达有多远

    `credit` 和 `chunks` 一起是整个进度一眼：*"9 个区块，3 个可花。"*

读一个玩家的 **自己** 岛屿的占位符解决到他们拥有的岛屿，即使他们站在别人的上面。`visited_island_*` 变体读玩家现在站在的岛屿。

{{ placeholders_bundle(gamemode_name="chunkblock") }}
