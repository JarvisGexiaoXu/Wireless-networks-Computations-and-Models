# In this library, I create a list of functions to support creating wireless 
# related demos.These functions are used to facilitate the future computation 
# and emphasize my understanding of the course material.
import random as r
import sys
import math as m
import numpy as np
import matplotlib.pyplot as plt

# Converters
def bps_to_kbps(bps):
    return bps*0.001 

def kbps_to_bps(kbps):
    return kbps/0.001 

def kbps_to_byteps(kbps):
    return kbps/0.008

def byteps_to_kbps(byteps):
    return byteps*0.008

def bps_to_byteps(bps):
    return kbps_to_byteps(bps_to_kbps(bps))

def byteps_to_bps(byteps):
    return kbps_to_bps(byteps_to_kbps(byteps))


# Binary Generator
# Generates a binary number in string
def binary_generator(length, prob = 0.5): 
    if prob < 0 or prob > 1: 
        print("invalid probablity")
        return None
    elif length < 1:
        print("invalid length")
        return None
    else:
        b = ''
        for i in range(length):
            if r.random()< prob: b += '0'
            else: b += '1'
        return b
        
# Convert from binary to real number
def binary_to_real_number(b): return int(b,2) 

# Compression Ratio
def compression_ratio(ori_s, compres_s):
    return sys.getsizeof(ori_s)/sys.getsizeof(compres_s)

# Mimic Transmission Error
def mimic_transmission_error(b, error_prob):  # error_prob < 0.5 makes the channel worthwhile
    transed_b = ''
    for i in range(len(b)):
        if r.random() < error_prob:
            # print(i) # Check which bits are errors
            if b[i] == '1': transed_b += '0'
            else: transed_b += '1'
        else:
            transed_b += b[i]
    return transed_b

# Computations
def permutation(n, k): # 0 <= k <= n 
    if 0 <= k and k <= n:
        return (m.factorial(n))/(m.factorial(k) * m.factorial(n-k))
    else: return None

# Convert btw string binary and numpy matrix
def number_string_to_matrix(b):
    temp = []
    for c in b: temp.append(int(c))
    return np.asarray(temp)

def number_matrix_to_string(b):
    temp = ''
    for n in b: temp += str(int(n))
    return temp

# Sum all the numbers in the list then mod 2
def sum_mod(b):
    return sum(b) % 2

# Shift registers to the left
def shift_to_left(b_lst, b):
    temp = []
    for i in range(len(b_lst)):
        if i != 0: temp.append(b_lst[i])
    temp.append(b)
    return np.asarray(temp)

# Shift registers to the right
def shift_to_right(b_lst, b):
    temp = [b]
    for i in range(len(b_lst)):
        if i != len(b_lst)-1: temp.append(b_lst[i])
    return np.asarray(temp)

# Hamming Distance between two vectors
def hamming_distance(v1, v2):
    if len(v1) == len(v2):
        d = 0
        for i in range(len(v1)):
            if v1[i] != v2[i]: d += 1
        return d
    else: 
        print("inequal length")
        return False

# Mean Square Error (MSE) between two vectors
def MSE(v1, v2):
    if len(v1) == len(v2):
        d = 0
        for i in range(len(v1)):
            d = d + (v1[i] - v2[i])**2
        return d/len(v1)
    else: 
        print("inequal length")
        return False

# Waves
# Fs, sample rate 100Hz
# size, # of samples 1000
# t = np.arange(0, size)/Fs, signal length
def sine_wave(t):
    x1 = np.sin(2 * np.pi * 1 * t)
    # plt.plot(t,x1)
    # plt.show()
    return x1

def square_wave(Fs, t, size):
    x2 = np.array([1,0])
    x2 = np.repeat(x2, Fs//2)
    x2 = np.tile(x2, size//(Fs//1))
    # plt.plot(t,x2)
    # plt.show()
    return x2

def triangle_wave(Fs, t, size):
    x2 = square_wave(Fs, t, size)
    x2 = x2 - np.mean(x2)
    x3 = np.zeros(size)
    sum = 0
    for i in range(size):
        sum += x2[i]
        x3[i] = sum
    x3 /= np.max(x2)
    # plt.plot(t,x3)
    # plt.show()
    return x3

def white_gaussian_noise(t, size):
    n1 = np.random.randn(size) * 2
    # plt.plot(t,n1)
    # plt.show()    
    return n1

def uniform_white_noise(t, size):
    n2 = np.random.rand(size)
    n2 -= np.mean(n2)
    # plt.plot(t,n2)
    # plt.show()
    return n2