# In this folder, I create a list of wireless networks computational functions.
# These functions are used to facilitate the future computation and emphasize 
# my understanding of the course material.

# --------------------------Lecture 2 page 9-10------------------------------
# define parameters

num_routers = 2 # Number of Routers
err_prob = [10**(-5), 10**(-5)] # Frame error probability of the i-th segment
rate = [100000, 100000] # Rate of the i-th segment (in bps)
length = [300, 700] # Length of i-th segment (in m)
proc = [3, 4] # Processing time of the i-th router (in s)
sig_speed = [2*(10**8),2*(10**8)] # Signal speend on the i-th segment (in m/s)
frame_len = [1024, 1024] # The number of bits per frame (in bits)

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

# Computational results are 
    # The Overall error probability
    # The Actual rate
    # The delay of the abstract link connecting the computer to the server (in s)
        # more precisely, we need to calculate the time taken by the first bit sent 
        # from the computer to reach the server given that there are several routers 
        # in the middle.

def Overall_Err_Prob(err_prob):
    temp = 1
    for x in err_prob:
        temp *= (1-x)
    res = 1 - temp
    return res

def Actual_Rate(rate):
    return min(rate)

def Delay_Computer_Server(length, sig_speed, proc, frame_len, rate, num_routers): # return in seconds
    temp1 = 0
    temp2 = 0
    for i in range(num_routers): 
        temp1 += length[i]/sig_speed[i]
        temp2 += frame_len[i]/rate[i]
    temp3 = sum(proc)
    return temp1 + temp2 + temp3

     









































def main():
    # Test
    # print(Overall_Err_Prob(err_prob))
    print(Actual_Rate(rate))
    # print(byteps_to_bps(1))
    print(Delay_Computer_Server(length, sig_speed, proc, frame_len, rate, num_routers))

main()