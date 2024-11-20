#!/usr/bin/env python3

from scipy.io.wavfile import read
import matplotlib.pyplot as plt

import numpy

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

rate, data = read("./same.wav")
plt.plot(data[0:1024])
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.show()

zero_crossings = numpy.where(numpy.diff(numpy.sign(data)))[0]
print(zero_crossings)
