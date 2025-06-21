# defining the scale; could put this in a separate file and import the pg object
from scamp_extensions.pitch import ScaleType, Scale

# specify the tuning (you can also load scales from a scala file with `ScaleType.load_from_scala`
pythagorean_scale_type = ScaleType("2187/2048", "9/8", "32/27", "81/64", "4/3", "729/512", "3/2",  "6561/4096", "27/16", "16/9", "243/128", "2/1")

pg = Scale(pythagorean_scale_type, 0)


# main script
from scamp import *

s = Session()

clarinet = s.new_part("violin")

tune = [
    (60, 1.0, 1),  # Middle C, full volume, quarter note
    (62, 0.8, 0.5),  # D, 80% volume, half note
    (64, 0.7, 0.25),  # E, 70% volume, quarter note
    (65, 0.6, 0.25),  # F, 60% volume, quarter note
    (67, 0.5, 0.5),  # G, 50% volume, half note
    (69, 0.4, 0.25),  # A, 40% volume, quarter note
    (71, 0.3, 0.5),  # B, 30% volume, half note
    (72, 0.2, 0.25),  # High C, 20% volume, quarter note
    (74, 0.1, 0.5),  # D, 10% volume, half note
    (76, 0.9, 0.75),  # E, 90% volume, dotted quarter note
    (77, 0.7, 0.25),  # F, 70% volume, quarter note
]
#
tune = [
    (60, 0.8, 0.5),  # Middle C, 80% volume, half note
    (62, 0.7, 0.25),  # D, 70% volume, quarter note
    (64, 0.6, 0.25),  # E, 60% volume, quarter note
    (65, 0.5, 0.5),  # F, 50% volume, half note
    (67, 0.4, 0.25),  # G, 40% volume, quarter note
    (69, 0.3, 0.25),  # A, 30% volume, quarter note
    (71, 0.2, 0.5),  # B, 20% volume, half note
    (72, 0.9, 0.25),  # High C, 90% volume, quarter note
    (74, 0.8, 0.25),  # D, 80% volume, quarter note
    (76, 0.7, 0.5),  # E, 70% volume, half note
    (77, 0.6, 0.25),  # F, 60% volume, quarter note
]

tune = [
    (60, 0.8, 0.5),  # Middle C, 80% volume, half note
    (62, 0.7, 0.25),  # D, 70% volume, quarter note
    (64, 0.6, 0.5),  # E, 60% volume, half note
    (65, 0.5, 0.25),  # F, 50% volume, quarter note
    (67, 0.4, 0.5),  # G, 40% volume, half note
    (69, 0.3, 0.25),  # A, 30% volume, quarter note
    (71, 0.2, 0.75),  # B, 20% volume, dotted quarter note
    (72, 0.9, 0.25),  # High C, 90% volume, quarter note
    (74, 0.8, 0.5),  # D, 80% volume, half note
    (76, 0.7, 0.25),  # E, 70% volume, quarter note
    (77, 0.6, 0.75),  # F, 60% volume, dotted quarter note
]
#
tune = [
    (60, 0.8, 0.5),  # Middle C, 80% volume, half note
    (62, 0.6, 0.25),  # D, 60% volume, quarter note
    (59, 0.7, 0.5),  # B, 70% volume, half note (downward)
    (63, 0.5, 0.25),  # E, 50% volume, quarter note (upward)
    (57, 0.6, 0.5),  # A, 60% volume, half note (downward)
    (64, 0.4, 0.25),  # F, 40% volume, quarter note (upward)
    (55, 0.7, 0.75),  # G, 70% volume, dotted quarter note (downward)
    (65, 0.9, 0.25),  # F#, 90% volume, quarter note (upward)
    (56, 0.6, 0.5),  # G#, 60% volume, half note (downward)
    (67, 0.7, 0.25),  # A#, 70% volume, quarter note (upward)
    (58, 0.8, 0.5),  # B, 80% volume, half note (downward)
]
tune = [
    (60, 0.8, 0.25),  # Middle C, 80% volume, quarter note
    (63, 0.6, 0.5),   # E, 60% volume, half note (upward)
    (58, 0.7, 0.25),  # B, 70% volume, quarter note (downward)
    (65, 0.5, 0.5),   # F#, 50% volume, half note (upward)
    (57, 0.6, 0.25),  # A, 60% volume, quarter note (downward)
    (67, 0.4, 0.25),  # G, 40% volume, quarter note (upward)
    (62, 0.7, 0.5),   # D, 70% volume, half note (downward)
    (69, 0.9, 0.25),  # A, 90% volume, quarter note (upward)
    (56, 0.6, 0.5),   # G#, 60% volume, half note (downward)
    (71, 0.7, 0.25),  # B, 70% volume, quarter note (upward)
    (59, 0.8, 0.5),   # B, 80% volume, half note (downward)
]

tune = [
    (60, 0.8, 0.5),  # Middle C, 80% volume, half note
    (63, 0.6, 0.25),  # E, 60% volume, quarter note
    (58, 0.7, 0.75),  # B, 70% volume, dotted quarter note
    (65, 0.5, 0.5),  # F#, 50% volume, half note
    (57, 0.6, 0.25),  # A, 60% volume, quarter note
    (67, 0.4, 0.75),  # G, 40% volume, dotted quarter note
    (62, 0.7, 0.5),  # D, 70% volume, half note
    (69, 0.9, 0.25),  # A, 90% volume, quarter note
    (56, 0.6, 0.75),  # G#, 60% volume, dotted quarter note
    (71, 0.7, 0.5),  # B, 70% volume, half note
]

tune = [
    (67, 0.9, 0.25),  # G5, 90% volume, quarter note (Staccato)
    (69, 0.9, 0.25),  # A5, 90% volume, quarter note (Staccato)
    (71, 0.9, 0.25),  # B5, 90% volume, quarter note (Staccato)
    (72, 0.9, 0.25),  # C6, 90% volume, quarter note (Staccato)

    (74, 0.9, 0.25),  # D6, 90% volume, quarter note (Staccato)
    (76, 0.9, 0.25),  # E6, 90% volume, quarter note (Staccato)
    (77, 0.9, 0.25),  # F6, 90% volume, quarter note (Staccato)
    (79, 0.9, 0.25),  # G6, 90% volume, quarter note (Staccato)

    (81, 0.9, 0.25),  # A6, 90% volume, quarter note (Staccato)
    (83, 0.9, 0.25),  # B6, 90% volume, quarter note (Staccato)
    (84, 0.9, 0.25),  # C7, 90% volume, quarter note (Staccato)
    (86, 0.9, 0.25),  # D7, 90% volume, quarter note (Staccato)

    (88, 0.9, 0.25),  # E7, 90% volume, quarter note (Staccato)
    (89, 0.9, 0.25),  # F7, 90% volume, quarter note (Staccato)
    (91, 0.9, 0.25),  # G7, 90% volume, quarter note (Staccato)
    (93, 0.9, 0.25),  # A7, 90% volume, quarter note (Staccato)
]

tune = [
    (67, 0.7, 0.25),  # G5, 70% volume, quarter note (Staccato)
    (69, 0.6, 0.125),  # A5, 60% volume, eighth note (Staccato)
    (71, 0.8, 0.125),  # B5, 80% volume, eighth note (Staccato)
    (72, 0.7, 0.375),  # C6, 70% volume, dotted quarter note (Staccato)

    (74, 0.9, 0.125),  # D6, 90% volume, eighth note (Staccato)
    (76, 0.6, 0.25),  # E6, 60% volume, quarter note (Staccato)
    (77, 0.8, 0.125),  # F6, 80% volume, eighth note (Staccato)
    (79, 0.7, 0.125),  # G6, 70% volume, eighth note (Staccato)

    (81, 0.6, 0.25),  # A6, 60% volume, quarter note (Staccato)
    (83, 0.8, 0.125),  # B6, 80% volume, eighth note (Staccato)
    (84, 0.7, 0.125),  # C7, 70% volume, eighth note (Staccato)
    (86, 0.9, 0.375),  # D7, 90% volume, dotted quarter note (Staccato)

    (88, 0.8, 0.125),  # E7, 80% volume, eighth note (Staccato)
    (89, 0.7, 0.25),  # F7, 70% volume, quarter note (Staccato)
    (91, 0.6, 0.125),  # G7, 60% volume, eighth note (Staccato)
    (93, 0.9, 0.125),  # A7, 90% volume, eighth note (Staccato)
]


tune = [
    (67, 0.7, 0.25),  # G5, 70% volume, quarter note (Staccato)
    (72, 0.8, 0.125),  # C6, 80% volume, eighth note (Staccato)
    (69, 0.6, 0.125),  # A5, 60% volume, eighth note (Staccato)
    (74, 0.7, 0.375),  # D6, 70% volume, dotted quarter note (Staccato)

    (76, 0.9, 0.125),  # E6, 90% volume, eighth note (Staccato)
    (71, 0.6, 0.25),  # B5, 60% volume, quarter note (Staccato)
    (79, 0.8, 0.125),  # G6, 80% volume, eighth note (Staccato)
    (77, 0.7, 0.125),  # F6, 70% volume, eighth note (Staccato)

    (88, 0.8, 0.25),  # E7, 80% volume, quarter note (Staccato)
    (83, 0.7, 0.125),  # B6, 70% volume, eighth note (Staccato)
    (81, 0.6, 0.125),  # A6, 60% volume, eighth note (Staccato)
    (86, 0.9, 0.375),  # D7, 90% volume, dotted quarter note (Staccato)

    (93, 0.9, 0.125),  # A7, 90% volume, eighth note (Staccato)
    (84, 0.7, 0.25),  # C7, 70% volume, quarter note (Staccato)
    (91, 0.8, 0.125),  # G7, 80% volume, eighth note (Staccato)
    (88, 0.7, 0.125),  # E7, 70% volume, eighth note (Staccato)
]

tune = [
    (67, 0.7, 0.25),  # G5, 70% volume, quarter note (Staccato)
    (72, 0.8, 0.125),  # C6, 80% volume, eighth note (Staccato)
    (69, 0.6, 0.125),  # A5, 60% volume, eighth note (Staccato)
    (74, 0.7, 0.375),  # D6, 70% volume, dotted quarter note (Staccato)

    (76, 0.9, 0.125),  # E6, 90% volume, eighth note (Staccato)
    (71, 0.6, 0.25),  # B5, 60% volume, quarter note (Staccato)
    (79, 0.8, 0.125),  # G6, 80% volume, eighth note (Staccato)
    (77, 0.7, 0.125),  # F6, 70% volume, eighth note (Staccato)

    (88, 0.8, 0.25),  # E7, 80% volume, quarter note (Staccato)
    (83, 0.7, 0.125),  # B6, 70% volume, eighth note (Staccato)
    (81, 0.6, 0.125),  # A6, 60% volume, eighth note (Staccato)
    (86, 0.9, 0.375),  # D7, 90% volume, dotted quarter note (Staccato)

    (93, 0.9, 0.125),  # A7, 90% volume, eighth note (Staccato)
    (84, 0.7, 0.25),  # C7, 70% volume, quarter note (Staccato)
    (91, 0.8, 0.125),  # G7, 80% volume, eighth note (Staccato)
    (88, 0.7, 0.125),  # E7, 70% volume, eighth note (Staccato)

    (74, 0.7, 0.25),  # D6, 70% volume, quarter note (Staccato)
    (81, 0.8, 0.125),  # A6, 80% volume, eighth note (Staccato)
    (79, 0.6, 0.125),  # G6, 60% volume, eighth note (Staccato)
    (76, 0.7, 0.375),  # E6, 70% volume, dotted quarter note (Staccato)
]
s.start_transcribing()

# play individual notes
for note in tune:
    print(note)
    clarinet.play_note(note[0], note[1], note[2])


performance = s.stop_transcribing()

# performance.to_score(title="Test", composer="Test").show_xml()


