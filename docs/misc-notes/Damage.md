# Damage

Here's a quick dump of everything I've figured out about damage so far:

- Damage is received via the `IAttackReceiver` interface. The components I can find that appear to implement this are:
  - `Balloon`
  - `Boneworks.AttackReceiver_ProgressionTarget`
  - `Boneworks.AttackReceiver_Targets`
  - `Boneworks.AttackReceiver_TimeSlow`
  - `DoorControl.ReceiveAttack`
  - `EnemyDamageReceiver`
  - `PlayerDamageReceiver`
  - `Prop_DamageReceiver`
  - `PuppetMasta.MuscleCollisionBroadcaster`
  - `RigidbodyProjectile`
  - `SixSidedCrate`
  - `StressLevelZero.Combat.AttackReceiver`
  - `StressLevelZero.Combat.GenericAttackReceiver`
  - `StressLevelZero.Combat.ImpactProperties`
  - `StressLevelZero.Combat.ProjectileBalloon`
  - `StressLevelZero.Combat.ProjectileBaloon_Arena`
  - `StressLevelZero.Combat.VisualDamageReceiver`
  - `StressLevelZero.Props.Balloon`
  - `StressLevelZero.Props.CollisionCheck`
  - `StressLevelZero.Props.ObjectDestructable`
  - `ZombieDamageReceiver`
- The generated assemblies don't show implemented interfaces, so search for a `ReceiveAttack` method.
- If you just need the raw damage value, the `GenericAttackReceiver` component has a UnityEvent with the damage passed in as a float
- If you need more, hook one of the components above
- Player damage is applied by just subtracting the damage value of an attack from the player's health
- ~~Damage multipliers appear to be applied somewhere before `ReceiveAttack` is called, currently unsure where~~ This doesn't seem right, looking at decompiled StabSlash + Projectile - they don't do anything special
- In Ghidra you can find anything that deals damage by looking at the xrefs for `ExecuteEvents_EventFunction_1_StressLevelZero_Combat_IAttackReceiver__Class*`
- Somewhere around that you'll probably find really messy code setting members of a random type with lots of offsets, generally making not much sense. Retype that variable as `Attack__Boxed*` and it'll make sense

- Damage multipliers found experimentally:
| Body part | Multiplier |
| --------- | ---------- |
| Head      | 4          |
| Chest     | 1          |
| Hand      | 0.6        |
