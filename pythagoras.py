import math
import time

from pysinewave import SineWave

BASE_FREQ = 256

C = 0
CIS = 1
D = 2
DIS = 3
E = 4
F = 5
FIS = 6
G = 7
GIS = 8
A = 9
AIS = 10
B = 11


# Create scales

# Normal
normal_scale = []
for i in range(12):
    normal_scale.append(BASE_FREQ * math.pow(2, i/12))

normal_scale.append(BASE_FREQ * 2)

print(normal_scale)

# Pythagoras
pythagoras_scale = [BASE_FREQ * 2]
for i in range(11):
    new_freq = pythagoras_scale[i] * 2/3
    if new_freq < BASE_FREQ:
        new_freq *= 2
    pythagoras_scale.append(new_freq)

pythagoras_scale.append(BASE_FREQ)

pythagoras_scale.sort()

# komt niet overeen met: https://nl.wikipedia.org/wiki/Stemming_van_Pythagoras
print(pythagoras_scale)


# # Create a sine wave (pitch 0 = middle C)
# sinewave = SineWave(pitch = 0, pitch_per_second = 10000)
#
# # Set frequency directly
# sinewave.set_frequency(BASE_FREQ)
#
# # Turn the sine wave on.
# sinewave.play()
#
# for f in pythagoras_scale:
#     sinewave.set_frequency(f)
#     time.sleep(1)
#
#
# sinewave.stop()

scale = pythagoras_scale

tune = [(C, 1/4), (C, 1/4),
        (G, 1/4), (G, 1/4),
        (A, 1/4), (A, 1/4),
        (G, 1/2),
        (F, 1/8), (F, 1/8), (F, 1/8), (F, 1/8),
        (E, 1/4), (E, 1/4),
        (D, 1/4), (D, 1/4),
        (C, 1/2)]

# Create a sine wave (pitch 0 = middle C)
sinewave = SineWave(pitch = 0, pitch_per_second = 10000)

# Set frequency directly
sinewave.set_frequency(BASE_FREQ)


for note in tune:
    sinewave.set_frequency(scale[note[0]])
    sinewave.play()
    time.sleep(note[1] * 4)
    sinewave.stop()


sinewave.stop()