# class TimeTrialData

Class that handles your best time, and previous times on the Time Trial.

## Methods
- void Clear()
- [TTTime](/class-reference/StressLevelZero/Data/TTTime.md) GetSceneTime(string ttTime)
- void Load()
- void Save()
- void SetSceneTime(string ttTime, [TTTime](/class-reference/StressLevelZero/Data/TTTime.md) newSceneTime)

## Fields
- int ActiveSlot
- Dictionary<string, [TTTime](/class-reference/StressLevelZero/Data/TTTime.md)> __tttimes