# class SpawnableObject

A widely used class for all spawnable entities.

SpawnableObjects inherit from the ScriptableObject class. SpawnableObjects have prefabs attached, and can be put into a category.
They also can be set with a pooled mode, a max pooled amount, and a pool type. SpawnableObjects also have pre-set UUIDs.
Once created, they can be serialized into the master list.

## Methods
- void OnAfterDeserialize()
- void OnBeforeSerialize()
- string ToString()

## Fields
- [CategoryFilters](/class-reference/StressLevelZero/Data/CategoryFilters.md) category
- string description
- bool isHidden
- [PoolMode](/class-reference/StressLevelZero/Pool/PoolMode.md) mode
- int pooledAmount
- GameObject prefab
- float spawnDistance
- float spawnFrequency
- int spawnStackCount
- float spawnStackDistance
- string title
- string UUID
- int warmupAmount
- string _uuid