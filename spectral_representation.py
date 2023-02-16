# In this folder, I create a list of wireless networks computational functions.
# These functions are used to facilitate the future computation and emphasize 
# my understanding of the course material.
import wireless_lib as wl
import numpy as np
import matplotlib.pyplot as plt
# --------------------------Lecture x page x------------------------------
# Try to represent different types of signals
'''All the following waves are functionized in wireless_lib.py'''
'''
Fs = 100 # sample rate 100Hz
size = 1000 # # of samples 1000
t = np.arange(0, size)/Fs # signal length = 10s

# Sine wave
x1 = np.sin(2 * np.pi * 1 * t)
# plt.plot(t,x1)
# plt.show()

# Square wave, obtained from sine wave
x2 = np.array([1,0])
x2 = np.repeat(x2, Fs//2)
x2 = np.tile(x2, size//(Fs//1))
# plt.plot(t,x2)
# plt.show()

# Triangle wave, obtained from sine wave
x2 = x2 - np.mean(x2)
x3 = np.zeros(size)
sum = 0
for i in range(size):
    sum += x2[i]
    x3[i] = sum
x3 /= np.max(x2)
# plt.plot(t,x3)
# plt.show()

# White Gaussian noise
n1 = np.random.randn(size) * 2
# plt.plot(t,n1)
# plt.show()

# Uniformly distributed white noise
n2 = np.random.rand(size)
n2 -= np.mean(n2)
plt.plot(t,n2)
plt.show()
'''

