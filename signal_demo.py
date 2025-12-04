import numpy as np
import matplotlib.pyplot as plt
import rainflow
from math import sin, cos

sample_rate = 1000  # samples per second
time = np.linspace(0, 4.0, 4 * sample_rate)
#time = [4.0 * i / 200 for i in range(200 + 1)]
signal = [0.2 + 0.5 * sin(t) + 0.2 * cos(10*t) + 0.2 * sin(4*t) for t in time]

cycles = rainflow.count_cycles(signal)
#print(cycles)

from src.rainflow import reversals

reversal_points = list(reversals(signal))
reversal_with_time = [(float(time[index]), float(magnitude)) for index, magnitude in reversal_points]
print(reversal_with_time)


plt.figure(figsize=(10, 4))
plt.plot(time, signal)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Time Domain Signal")
plt.show()


