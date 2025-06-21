# defining the scale; could put this in a separate file and import the pg object
from scamp_extensions.pitch import ScaleType, Scale

# specify the tuning (you can also load scales from a scala file with `ScaleType.load_from_scala`
pythagorean_scale_type = ScaleType("2187/2048", "9/8", "32/27", "81/64", "4/3", "729/512", "3/2",  "6561/4096", "27/16", "16/9", "243/128", "2/1")

pg = Scale(pythagorean_scale_type, 0)


# main script
from scamp import *

s = Session()

clarinet = s.new_part("clarinet")



s.start_transcribing()

# play individual notes
for pitch in range(60, 73):
    clarinet.play_note(pg[pitch], 0.7, 0.5)

# play sequence of perfect 5ths
for pitch in range(60, 73):
    clarinet.play_chord(pg[pitch, pitch + 7], 0.7, 0.5)

    print(pg[pitch])

performance = s.stop_transcribing()

performance.to_score(title="Test", composer="Test").show_xml()


