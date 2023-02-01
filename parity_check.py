# In this folder, I create a list of wireless networks computational functions.
# These functions are used to facilitate the future computation and emphasize 
# my understanding of the course material.
import wireless_lib as wl
import random as r
# --------------------------Lecture 4 page 9-10------------------------------
# Single Parity Check

# b = wl.binary_generator(10,0.6)
# print(b)

def single_parity_encode(b):
    temp = 0
    for i in range(len(b)):
        temp += int(b[i])
    temp = temp % 2
    return b + str(temp)


# encoded_b = single_parity_encode(b)
# print(encoded_b)

# transed_encoded_b = wl.mimic_transmission_error(encoded_b, 0.1)
# print(transed_encoded_b)

def receiver_check(b):
    # Check even number of 1s
    num = 0
    for i in range(len(b)):
        if b[i] == '1': num += 1
    num = num % 2
    if num == 1: 
        # print("Error Detected: Even number of 1s.")
        return False
    else: 
        # print("No Error Detected")
        return True

num_no_error = 0
num_detected_error = 0
num_undetected_error = 0
num_runs = 100000
for i in range(num_runs):
    b = wl.binary_generator(4, 0.5)
    # print(b)
    encoded_b = single_parity_encode(b)
    # print(encoded_b)
    transed_encoded_b = wl.mimic_transmission_error(encoded_b, 0.1)
    # print(transed_encoded_b)
    res = receiver_check(transed_encoded_b)
    # print("Error free:", res)
    # print("Actually error free:", encoded_b == transed_encoded_b)
    if res == True and encoded_b == transed_encoded_b: num_no_error += 1
    elif res == True and encoded_b != transed_encoded_b: num_undetected_error += 1
    else: num_detected_error += 1

print("no error: ", num_no_error/num_runs)
print("detected error: ", num_detected_error/num_runs)
print("undetected error: ", num_undetected_error/num_runs)


