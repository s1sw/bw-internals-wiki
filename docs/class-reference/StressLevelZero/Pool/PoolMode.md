# enum PoolMode

Enum for various pool modes.

Grow increases the pool when it reaches the max amount. 
ReuseDeadOrGrow reuses dead enemies, or grows if exceeds amount.
ReuseNewest reuses entities that are newly spawned.
ReuseNone is self explanitory.
ReuseOldest reuses entities that have been spawned earlier on.

## Enum values
- GROW
- REUSEDEADORGROW
- REUSENEWEST
- REUSENONE
- REUSEOLDEST