#  fluid_settings_t* settings;
#  fluid_synth_t* synth;
#  fluid_audio_driver_t* adriver;
#  int sfont_id;
#  int i, key;
#
#  settings = new_fluid_settings();
#  synth = new_fluid_synth(settings);
#  adriver = new_fluid_audio_driver(settings, synth);
#  sfont_id = fluid_synth_sfload(synth, "example.sf2", 1);
#  for (i = 0; i < 12; i++) {
#    key = 60 + (int) (12.0f * rand() / (float) RAND_MAX);
#    fluid_synth_noteon(synth, 0, key, 80);
#    sleep(1);
#    fluid_synth_noteoff(synth, 0, key);
#  }
#
#  delete_fluid_audio_driver(adriver);
#  delete_fluid_synth(synth);
#  delete_fluid_settings(settings);

import fluidsynth.fluidsynth
