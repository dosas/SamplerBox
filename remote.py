#!/home/pi/venv/bin/python

import rtmidi
import time
import sys

midiout = rtmidi.MidiOut()
midiout.open_virtual_port("sample shark remote")

time.sleep(1.5)

note = 60

if len(sys.argv) > 1:
    key = int(sys.argv[1])
    if key == 1:
        pass
    elif key == 2:
        note = 62
    elif key == 3:
        note = 64
    elif key == 4:
        note = 66
    else:
        note = key

with midiout:
    note_on = [0x90, note, 127]  # channel 1, middle C, velocity
    midiout.send_message(note_on)

del midiout
