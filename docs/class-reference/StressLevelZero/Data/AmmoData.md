# class AmmoData

Class that handles the ammo related to the current scene that you are in. Ammo values vary from level to level.

## Methods
- void Clear()
- SceneAmmo GetSceneAmmo(string sceneName)
- void Load()
- void Save()
- void SetSceneAmmo(string sceneName, SceneAmmo newSceneAmmo)

## Fields
- int ActiveSlot
- Dictionary<string, SceneAmmo> _sceneAmmos