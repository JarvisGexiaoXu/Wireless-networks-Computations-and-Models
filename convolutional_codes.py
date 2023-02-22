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

# --------------------------Lecture 5 page 19-17--------------------------
def complex_conv_encode(msg, reg, p1, p2):
    while(None in reg):
        last, msg = msg[0], msg[1:]
        reg = wl.shift_to_right(reg, last)
    code = [wl.sum_mod(reg*p1), wl.sum_mod(reg * p2)]
    while(len(msg) > 0):       
        last, msg = msg[0], msg[1:]
        reg = wl.shift_to_right(reg, last)
        code = code + [wl.sum_mod(reg * p1), wl.sum_mod(reg * p2)] 
    return np.asarray(code)


# p1 = wl.number_string_to_matrix(wl.binary_generator(K))
# p2 = wl.number_string_to_matrix(wl.binary_generator(K))


# Viterbi
def viterbi_decode(code, p1, p2, pm, reg): # pm -> wl.hamming_distance or wl.MSE
    msg = []
    while(len(code) > 0):
        last, code = code[0:2], code[2:]
        temp1 = wl.shift_to_right(reg, 0)
        temp2 = wl.shift_to_right(reg, 1)
        temp_code1 = [wl.sum_mod(temp1 * p1), wl.sum_mod(temp1 * p2)]
        temp_code2 = [wl.sum_mod(temp2 * p1), wl.sum_mod(temp2 * p2)]
        d1 = pm(temp_code1, last)
        d2 = pm(temp_code2, last)
        if d1 <= d2:
            msg.append(0)
            reg = temp1
        else: 
            msg.append(1)
            reg = temp2
    return np.asarray(msg)
# Test accuracy of convolutional encoding and Viterbi decoding
p1 = np.asarray([1,1,1,1])
p2 = np.asarray([1,0,1,0])
reg = np.asarray([0,0,0,None])
num_err = 0
num_act_err = 0
for i in range(1000):
    msg1 = wl.number_string_to_matrix(wl.binary_generator(200,0.5))
    # print(msg1)
    v1 = complex_conv_encode(msg1, reg, p1, p2)
    v2 = wl.mimic_transmission_error(v1, 0.005)
    if wl.hamming_distance(v1, v2) > 0: num_act_err += 1 
    decoded_msg = viterbi_decode(v2, p1, p2, wl.MSE, reg)
    # print(decoded_msg)
    if wl.hamming_distance(msg1, decoded_msg) > 0: num_err += 1 
print("actual number of errors occured:", num_act_err)
print("number of error remain after decoding:", num_err)