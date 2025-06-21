from scamp import *

s = Session(tempo=120)

s.print_available_midi_output_devices()

# alt_sax = s.new_part("Alto SAX")
#
# # play major scale
# for i in [0, 2, 4, 5, 7, 9, 11, 12]:
#     alt_sax.play_note(60 + i, 0.8, 1.0)
#
# # small rest
# wait(1.0)