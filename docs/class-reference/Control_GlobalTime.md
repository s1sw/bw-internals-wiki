# class Control_GlobalTime

Class that manages the speed of time. Can slow down, speed up, and everything in between.

## Methods
- void add_OnSlowTime(Control_GlobalTime.SlowTime value)
- void DECREASE_TIMESCALE()
- void DROP_TIMESCALE()
- void INCREASE_TIMESCALE()
- IEnumerator LERP_TIMESCALE()
- void remove_OnSlowTime(Control_GlobalTime.SlowTime value)
- void RESET_TIMESCALE()
- void RISE_TIMESCALE()
- void SET_TIMESCALE(float intensity)
- void Start()
- void STEP_TIMESCALE(int step)
- void TOGGLE_TIMESCALE()
- void Update()

## Fields
- AudioClip accelTime
- bool ControllingTime
- float cur_intensity
- int cur_timeScaleStep
- AudioClip decelTime
- float def_FixedDeltaTime
- float def_intensity
- float def_lrp_time
- float lrp_calc_t
- float lrp_count
- float lrp_time
- float max_intensity
- int max_timeScaleStep
- AudioMixerGroup mixerGroup
- Control_GlobalTime.SlowTime OnSlowTime
- bool override_Keyboard
- bool override_TimeControl
- float tar_intensity
- float tmp_intensity
- float tru_max_intensity