# class VisualDamageController

Class that controls visual damage (i.e. bullet holes, stab wounds) through decal projection.

## Methods
- void AddToCutArray(Matrix4x4 Matrix)
- void AddToHitArray(Matrix4x4 Matrix)
- void Awake()
- IEnumerator BleedOverTimer()
- void InitializeBlock()
- void OnEnable()
- void ResetHits()
- void SendMessageToDismemberSys(GibID gibID, float Damage)
- void UpdateArray()

## Fields
- int Count
- int Count_CUT
- List<Matrix4x4> CutPoint
- Il2CppStructArray<Matrix4x4> CutPos
- DismembermentController dismemberment
- List<Matrix4x4> HitPoint
- Il2CppStructArray<Matrix4x4> HitPos
- float hitScaleFactor
- int MAX_HITS
- int MAX_HITS_CUT
- float meshScaleFactor
- int NumberOfCuts
- int NumberOfHits
- MaterialPropertyBlock propertiesBlock
- Il2CppReferenceArray<Renderer> Renderers