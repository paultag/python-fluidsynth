# Muse, from https://github.com/paultag/python-muse

from muse.scales.minor import NaturalMinorScale
from muse.chords import chord, MINOR_7TH
from muse.tone import Tone

from fluidsynth import Synth
import time

synth = Synth("/home/tag/organ.sf2", config={
    "audio.driver": "pulseaudio"
})
synth.start()


def take(it, n):
    for _ in range(n):
        yield next(it)


def play_chord(chord, duration):
    for c in chord:
        synth.noteon(0, c.to_midi(), 80)

    time.sleep(duration)

    for c in chord:
        synth.noteoff(0, c.to_midi())

while True:
    for note in take(NaturalMinorScale(Tone(0)).acending(), 7):
        play_chord(chord(note, MINOR_7TH), 2)


synth.shutdown()
