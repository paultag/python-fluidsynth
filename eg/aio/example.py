from muse.chords import (MAJOR, MAJOR_SEVENTH,)
from muse.tone import Tone

from fluidsynth.aio import AsyncSynth
import asyncio
import time

synth = AsyncSynth("/home/tag/piano/Full Grand Piano.sf2", config={
    "audio.driver": "pulseaudio",
    "synth.reverb.active": "yes"
})
synth.start()


time.sleep(3)


A3 = Tone(-1200)
D3 = A3.relative_tone(500)
F2 = D3.relative_tone(300).relative_tone(-1200)


@asyncio.coroutine
def play_chord(note, chord_, duration, lag):
    yield from asyncio.sleep(lag)
    yield from synth.chord(0, [x.to_midi() for x in note.chord(chord_)], 80, duration)


@asyncio.coroutine
def main():
    yield from asyncio.gather(
        asyncio.async(play_chord(D3, MAJOR_SEVENTH, 5.0, 0)),
        asyncio.async(play_chord(A3, MAJOR, 5.0, 2)),
        asyncio.async(play_chord(A3, MAJOR_SEVENTH, 5.0, 3)),
        asyncio.async(play_chord(F2, MAJOR_SEVENTH, 5.0, 4.5)),
    )


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

time.sleep(4)

synth.shutdown()
