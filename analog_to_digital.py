# In this folder, I create a list of wireless networks computational functions.
# These functions are used to facilitate the future computation and emphasize 
# my understanding of the course material.

# --------------------------Lecture 3 page 18-25------------------------------

import numpy as np
import matplotlib.pyplot as plt

import scipy
from scipy import signal

impulse = signal.unit_impulse(10, 'mid')
shifted_impulse = signal.unit_impulse(7, 2)

# Sine wave
t = np.linspace(0, 10, 100)
amp = 5 # Amplitude
f = 50
x = amp * np.sin(2 * np.pi * f * t) 

# Exponential Signal
x_ = amp * np.exp(-t)
plt.plot(t, x, linewidth=3, label='Sine wave')

print(t)
print(x)

plt.show()