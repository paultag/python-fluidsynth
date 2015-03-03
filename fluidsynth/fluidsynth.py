import time
from cffi import FFI
ffi = FFI()
ffi.cdef("""
typedef struct _fluid_hashtable_t fluid_settings_t;
typedef struct _fluid_synth_t fluid_synth_t;
typedef struct _fluid_audio_driver_t fluid_audio_driver_t;

fluid_settings_t* new_fluid_settings(void);
fluid_synth_t* new_fluid_synth(fluid_settings_t* settings);
fluid_audio_driver_t* new_fluid_audio_driver(fluid_settings_t* settings, fluid_synth_t* synth);
int fluid_synth_sfload(fluid_synth_t* synth, const char* filename, int reset_presets);

int fluid_synth_noteon(fluid_synth_t* synth, int chan, int key, int vel);
int fluid_synth_noteoff(fluid_synth_t* synth, int chan, int key);

void delete_fluid_audio_driver(fluid_audio_driver_t* driver);
int delete_fluid_synth(fluid_synth_t* synth);
void delete_fluid_settings(fluid_settings_t* settings);
""")
C = ffi.dlopen("/usr/lib/x86_64-linux-gnu/libfluidsynth.so.1")  # Testing

settings = C.new_fluid_settings()
synth = C.new_fluid_synth(settings)
adriver = C.new_fluid_audio_driver(settings, synth)
sfont_id = C.fluid_synth_sfload(synth, b"/usr/share/sounds/sf2/FluidR3_GS.sf2", 1)

key = 69  # ISO16 A4

C.fluid_synth_noteon(synth, 0, key, 80);

time.sleep(8);

C.fluid_synth_noteoff(synth, 0, key);

C.delete_fluid_audio_driver(adriver);
C.delete_fluid_synth(synth);
C.delete_fluid_settings(settings);
