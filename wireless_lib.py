# In this library, I create a list of functions to support creating wireless 
# related demos.These functions are used to facilitate the future computation 
# and emphasize my understanding of the course material.
import random as r
import sys

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
def binary_generator(length, prob): 
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
def mimic_transmission_error(b, rate):
    transed_b = ''
    for i in range(len(b)):
        if r.random() < rate:
            # print(i) # Check which bits are errors
            if b[i] == '1': transed_b += '0'
            else: transed_b += '1'
        else:
            transed_b += b[i]
    return transed_b