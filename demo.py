from scamp import *

s = Session(tempo=120)

alt_sax = s.new_part("Alto SAX")

# play major scale
for i in [0, 2, 4, 5, 7, 9, 11, 12]:
    alt_sax.play_note(60 + i, 0.8, 1.0)

# small rest
wait(1.0)

# play triad
for i in [0, 4, 7, 12, 7, 4, 0]:
    alt_sax.play_note(60 + i, 0.8, 1.0)