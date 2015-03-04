# Copyright (c) Paul R. Tagliamonte <tag@pault.ag>, 2015
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.


from .fluidsynth import C


class Synth(object):
    def __init__(self, font, *, config):
        self.settings = C.new_fluid_settings()

        for key, value in config.items():
            C.fluid_settings_setstr(self.settings, key.encode(), value.encode())

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
