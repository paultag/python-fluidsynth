from fluidsynth import Synth
import time


synth = Synth("/home/tag/organ.sf2")
synth.start()


while True:
    synth.noteon(0, 69, 80)
    time.sleep(1)
    synth.noteoff(0, 69)
    time.sleep(3)

synth.shutdown()
