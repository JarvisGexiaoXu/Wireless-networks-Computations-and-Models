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
# --------------------------Lecture 5 page 62-64---------------------------
'''
Digital information -> Analogue signals

Techniques of selection of analogue signals
-Pulse shaping
-Line coding
-Modulation
-Encoding
Transmitted through
-Baseband channel
-Bandpass channel
Key performance indicators
-Bit rate
-Error probability

Frouier Theorem: Any signal can be uniquely and reversibly decomposed into a sum of sinusoids with 
different amplitudes, frequencies, and phases.
Bandwidth: The range of frequencies that includes all non-zero (or significant) spectral components 
of a signal.
General Rules:
    The faster varying the signal, the larger its bandwidth.
    Slow (abrupt) amplitude changes contribute to low (high) frequency components
'''
'''
# Transmissions Rates
W = 100 # Bandwidth of the channel, (Hz) 
SNR = 20 # the signal to noise ratio, (dB or a dimensionless quantity)
number_of_bits_per_symbol = 4
# The duration of symbol determines how quickly data can be transmitted over the channel.
# shorter the symbol duration, faster the data rate can be, but it will also requires more 
# sophisticated signal processing techniques to minimize errors caused by noise and interference.
symbol_duration = 10 # (seconds) usually use fraction of second, need to convert.
Pe = 0.001 # the probability of errors
info = 100 # the amount of useful data that is transmitted through the channel per unit time, measured
           # in bits per second (bps)
overhead = 50 # the amount of nonuseful data that is transmitted through the channel per unit time, 
              # such as control information, error correction code... measured in bits per second (bps)
# Channel Capacity
C = W*np.log2(1 + SNR) # (bits/section)
print(C)
# The spectrum efficiency determines the maximum bits per Hz that can be transmitted for a given SNR
Eta = np.log2(1 + SNR)
# The transmission rate (R) is defined as the total number of bits transmitter per second on a communication channel
R = number_of_bits_per_symbol/symbol_duration
# The throughput (T) is the total number of successfully transmitted bits per second
T = R * (1 - Pe)
# The goodput (G) is the number of information bits successfully received per second at the receiver
G = T * (info/(info + overhead))
'''
'''
def unipolar_NRZ(data):
    encoded = []
    for bit in data:
        if bit == 0:
            encoded += [0, 0]
        else:
            encoded += [1, 1]
    return encoded

def polar_NRZ(data):
    encoded = []
    for bit in data:
        if bit == 0:
            encoded += [-1, -1]
        else:
            encoded += [1, 1]
    return encoded

def NRZ_inverted(data):
    code = [-1,-1]
    encoded = []
    for bit in data:
        if bit == 0:
            encoded += [code[0], code[1]]
        else:
            for i in range(len(code)): code[i] = code[i] * -1
            encoded += [code[0], code[1]]
    return encoded

def bipolar(data):
    code = [-1,-1]
    encoded = []
    for bit in data:
        if bit == 0:
            encoded += [0, 0]
        else:
            for i in range(len(code)): code[i] = code[i] * -1
            encoded += [code[0], code[1]]
    return encoded

def manchester(data):
    encoded = []
    for bit in data:
        if bit == 0:
            encoded += [-1, 1]
        else:
            encoded += [1, -1]
    return encoded

def diff_machester(data):
    code = [-1,1]
    encoded = []
    for bit in data:
        if bit == 0:
            encoded += [code[0], code[1]]
        else:
            for i in range(len(code)): code[i] = code[i] * -1
            encoded += [code[0], code[1]]
    return encoded

data = [1, 0, 1, 0, 1, 1, 1, 0, 0] # binary data to encode
encoded_data = bipolar(data) # apply Manchester encoding
encoded_data.append(encoded_data[-1])
# plot the encoded data as a pulse train
print(encoded_data)
plt.step(range(len(encoded_data)), encoded_data, where='post')
for i in range(len(encoded_data)):
    plt.axvline(x=i, ymin=-5, ymax = 5, linestyle= 'dotted', linewidth = 1)
plt.ylim(-5, 5)
plt.xlabel('Bit Time')
plt.ylabel('Voltage')
plt.title('Manchester Line Coding')
plt.show()
'''
# All the codes above about line codes (including visualization) are functionized in wireless_lib
# Use case example
wl.line_code_visualize([1,0,1,0,1,1,1,0,0], wl.bipolar, name='bipolar')
