# class StabSlash

Class that handles stabbing of various entities.

## Methods
- void FixedUpdate()
- void InitializePreStab()
- void OnCollisionEnter(Collision c)
- void OnCollisionStay(Collision c)
- void ProcessCollision(Collision c, bool isStay = false)
- void Start()

## Fields
- StabSlash.BladeAudio bladeAudio
- Rigidbody rb
- Il2CppReferenceArray<StabSlash.SlashBlade> slashBlades
- Il2CppReferenceArray<StabSlash.StabPoint> stabPoints
- InteractableHost _host
