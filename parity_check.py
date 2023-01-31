# In this folder, I create a list of wireless networks computational functions.
# These functions are used to facilitate the future computation and emphasize 
# my understanding of the course material.

# --------------------------Lecture 4 page 9-10------------------------------
# Single Parity Check
import wireless_lib as wl
import random as r

b = wl.binary_generator(10,0.6)
print(b)

def single_parity_encode(b):
    temp = 0
    for i in range(len(b)):
        temp += int(b[i])
    temp = temp % 2
    return b + str(temp)


encoded_b = single_parity_encode(b)
print(encoded_b)

transed_encoded_b = wl.mimic_transmission_error(encoded_b, 0.1)
print(transed_encoded_b)

def receiver_check(b):
    # Check even number of 1s
    num = 0
    for i in range(len(b)):
        if b[i] == '1': num += 1
    num = num % 2
    if num == 1: 
        print("Error Detected: Even number of 1s.")
        return False
    else: 
        print("No Error Detected")
        return True

res = receiver_check(transed_encoded_b)
print("Error free:", res)
print("Actually free:", encoded_b == transed_encoded_b)

