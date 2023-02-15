# In this folder, I create a list of wireless networks computational functions.
# These functions are used to facilitate the future computation and emphasize 
# my understanding of the course material.
import wireless_lib as wl
import numpy as np
# --------------------------Lecture 5 page 8------------------------------
'''
Implemented via shift-register of a given size (constraint length [k])
A generator polynomial is used to compute parity bits using the incoming bit along
with the [k-1] bits in the shift-register.
We only send the parity bits not the information bits.
Code Rates  = 1/(# of generators)
'''

# K = 4 # K is the constraint length of the code
# msg = wl.number_string_to_matrix(wl.binary_generator(20))
# reg = wl.number_string_to_matrix(wl.binary_generator(K))

# print(msg)
# print(reg)

def simple_conv_encode(msg, reg):
    code = [wl.sum_mod(reg)]
    while(len(msg) > 0):       
        last, msg = msg[-1], msg[:-1]
        reg = wl.shift_to_right(reg, last)
        code = [wl.sum_mod(reg)] + code
    return np.asarray(code)

# print(simple_conv_encode(msg, reg))

def complex_conv_encode(msg, reg, p1, p2):
    while(None in reg):
        last, msg = msg[-1], msg[:-1]
        reg = wl.shift_to_right(reg, last)
    code = [wl.sum_mod(reg*p1), wl.sum_mod(reg * p2)]
    while(len(msg) > 0):       
        last, msg = msg[-1], msg[:-1]
        reg = wl.shift_to_right(reg, last)
        code = [wl.sum_mod(reg * p1), wl.sum_mod(reg * p2)] + code
    return np.asarray(code)


# p1 = wl.number_string_to_matrix(wl.binary_generator(K))
# p2 = wl.number_string_to_matrix(wl.binary_generator(K))
p1 = np.asarray([1,1,1])
p2 = np.asarray([1,0,1])
msg = np.asarray([0,1,1,1])
reg = np.asarray([0,0,None])

print(p1, p2)
print(complex_conv_encode(msg, reg, p1, p2))

#TODO Viterbi
