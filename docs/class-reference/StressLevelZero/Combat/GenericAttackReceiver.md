# class GenericAttackReceiver : MonoBehaviour,&nbsp;[IAttackReceiver](/class-reference/StressLevelZero/Combat/IAttackReceiver.md)

Implements IAttackReceiver exposing a UnityEvent that gets passed the damage.

## Methods
- void ReceiveAttack([Attack](/class-reference/StressLevelZero/Combat/Attack.md) attack)

## Fields
- UnityEventFloat AttackEvent
    - Called when an attack is received. The single float argument is the damage.
