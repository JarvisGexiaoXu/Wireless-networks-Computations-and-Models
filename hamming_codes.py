# In this folder, I create a list of wireless networks computational functions.
# These functions are used to facilitate the future computation and emphasize 
# my understanding of the course material.
import wireless_lib as wl
import numpy as np
# --------------------------Lecture 4 page 19------------------------------
# Hamming code

# (7,4) Hamming codes example (page 20 left)
# Example code for single line
b = wl.binary_generator(4, 0.5)
# print(b)
def hamming_code_7_4(b): # b has length equal to 4 (b type string)
    b5 = str((int(b[0]) + int(b[2]) + int(b[3])) % 2)
    b6 = str((int(b[0]) + int(b[1]) + int(b[3])) % 2)
    b7 = str((int(b[1]) + int(b[2]) + int(b[3])) % 2)
    b += (b5 + b6 + b7)
    return b

def weight(b):
    counter = 0
    for c in b: 
        if c == '1': counter += 1
    return counter


# hamming_encoded_b = hamming_code_7_4(b)
# print(hamming_encoded_b)
# temp = wl.number_string_to_matrix(hamming_encoded_b)
# print(temp)
# w = weight(hamming_encoded_b)
# print(w)

# (7,4) Hamming codes example (page 20 right)
def code_generator(b):
    b5 = (b[0] + b[2] + b[3]) % 2
    b6 = (b[0] + b[1] + b[3]) % 2
    b7 = (b[1] + b[2] + b[3]) % 2
    b = np.append(b, b5)
    b = np.append(b, b6)
    b = np.append(b, b7)
    return b

def hamming_code_simulation():
    x = wl.binary_generator(4, 0.5) # This is the original msg
    x = (wl.number_string_to_matrix(x))
    # print('Transmitted vector:', x)
    # Compute code generator matrix
    i4_matrix = np.identity(4)
    g = np.apply_along_axis(code_generator, 1, i4_matrix) # IMPORTANT!!!
    # print('G: ')
    # print(g)
    # Compute parity check matrix
    p = g[:,[4,5,6]]
    p_transpose = p.transpose()
    i3_matrix = np.identity(3)
    h = np.hstack((p_transpose, i3_matrix))
    # print('H: ')
    # print(h)
    # Codeword: b = x * G Assume x = 1, b = G
    codeword = np.dot(x, g) % 2 # This is what actually tranmitted
    codeword = wl.number_string_to_matrix(wl.number_matrix_to_string(codeword))
    temp = wl.number_matrix_to_string(codeword)
    temp = wl.mimic_transmission_error(temp, 0.1) 
    trans_codeword = wl.number_string_to_matrix(temp)
    # print('Codeword:', codeword)
    # print('Transmitted Codeword:', trans_codeword)
    # Syndrome: s = H * b_transpose
    s = np.dot(h, codeword.transpose()) % 2
    trans_s = np.dot(h, trans_codeword.transpose()) % 2
    # print('Syndrome of the original code:', s)
    # print('Syndrome of the transmitted code:', trans_s)
    if(np.array_equal(codeword, trans_codeword)): return 1 # No error
    elif(np.array_equal(trans_s, s)):return 2 # Undetected error
    else: return 3 # Detected error
# Syndrome computation
# s = H r = H (b + error) = H b + H error = 0 + H error = H error
# s = H error
no_e = 0
undetected_e = 0
detected_e = 0
num_runs = 10000
for i in range(num_runs):
    if hamming_code_simulation() == 1: no_e += 1
    elif hamming_code_simulation() == 2: undetected_e += 1
    else: detected_e += 1
print('No error:', no_e/num_runs)
print('Detected error', detected_e/num_runs)
print('Undetected error', undetected_e/num_runs)
'''
Now we have the syndrome, let's try to understand how it works,
if syndrome == 0:
    it could mean two things:
        1. no error,
        2. error vector corresponds to any valid codeword, (e = b) then it is undetectable
'''
