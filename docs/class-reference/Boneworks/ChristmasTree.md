# class ChristmasTree

Class that handles the functionality of the slow-time tree. 
Found in REDACTED Chamber, outside the bounds of Warehouse, and outside the bounds of the Hover Junkers level.

Time slows down when a player shoots, punctures, or hits any of the circles of the tree by a third for each plate.

## Methods
- void AutoDecrease()
- void DecreaseTimeScale()
- void IncreaseTimeScale
- IEnumerator PLAY_MUSIC()
- void SetRotation()
- void SetTimeScale(int step)
- void SlowTime(int target)
- void Start
- void ToggleTimeScale()

## Fields
- ConfigurableJoint jnt_tree_A
- ConfigurableJoint jnt_tree_B
- ConfigurableJoint jnt_tree_C
- int maxTimeScaleStep
- AudioSource musicPlayer
- float targetRot_A
- float targetRot_B
- float targetRot_C
- int timeScaleStep
- bool tree_A
- bool tree_B
- bool tree_C