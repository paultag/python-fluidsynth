from .fluidsynth import C


class Synth(object):
    def __init__(self, font):
        self.settings = C.new_fluid_settings()
        self.synth = C.new_fluid_synth(self.settings)
        self.sfont_id = C.fluid_synth_sfload(self.synth, font.encode(), 1)
        self.adriver = None

    def start(self):
        self.adriver = C.new_fluid_audio_driver(self.settings, self.synth)

    def noteon(self, channel, key, velocity):
        C.fluid_synth_noteon(self.synth, channel, key, velocity);

    def noteoff(self, channel, key):
        C.fluid_synth_noteoff(self.synth, channel, key);

    def shutdown(self):
        C.delete_fluid_audio_driver(adriver);
        C.delete_fluid_synth(synth);
        C.delete_fluid_settings(settings);
