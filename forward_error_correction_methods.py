# In this folder, I create a list of wireless networks computational functions.
# These functions are used to facilitate the future computation and emphasize 
# my understanding of the course material.
import wireless_lib as wl
# --------------------------Lecture 4 page 12------------------------------
# Parameters
len_code = 32
num_rendundant_bit = 1
error_p = 0.001 # p has to be smaller than 0.5

# Random bit error Channels 
# If without permuatation it means you know exact bit has error occurred (page 13)
# With permutation, you know error happens but do not know which bits (page 15)
def error_pattern_prob(num_errors, p, len_code):
    # Without permutation
    # return (p**(num_errors)) * ((1 - p)**(len_code - num_errors)) 
    # # With permutation
    return wl.permutation(len_code, num_errors) * (p**(num_errors)) * ((1 - p)**(len_code - num_errors)) 

''' TEST CODE'''
num_errors = 0
undetect_error_prob = 0
while(num_errors <= len_code):
    # Add permutations to the following computation
    if num_errors % 2 == 0 and num_errors != 0: undetect_error_prob += error_pattern_prob(num_errors, error_p, len_code)
    print('With error probablity', error_p, 'the distinct probablities of having', num_errors, 
        'in', len_code, 'bits code is', error_pattern_prob(num_errors, error_p, len_code))
    num_errors += 1
print("Undetectable error pattern if even number of bit errors, the probablity is", undetect_error_prob) # May contain mistake

# IMPORTANT!!!:: All the calculations below are for Single Parity check codes only

# Redundancy (overhead) (page 14) 
def redundancy(num_rendundant_bit, len_code):
    return 1/(len_code + num_rendundant_bit)

# Information Rate (Code Rate/Goodput) (page 14)
def info_rate(num_rendundant_bit, len_code):
    return len_code/(len_code + num_rendundant_bit)


# print('Single parity check code adds 1 redundant bit per k = 8 information bits, overhead is than',
#         redundancy(num_rendundant_bit, len_code))
# print('The goodput is', info_rate(num_rendundant_bit, len_code))

# Coverage # TODO

