# In this folder, I create a list of wireless networks computational functions.
# These functions are used to facilitate the future computation and emphasize 
# my understanding of the course material.

# --------------------------Lecture 3 page 14-16------------------------------
# Run Length Encodes (RLE)

# For both Huffman and RLE,
# PRO   - lossless, perfect recovery.
#       - high performance in case of the information contains redundant bits & long runs.
# CON   - depends on information content.
#       - lack of error propagation, can use external techniques, but high complexity.

import sys
import wireless_lib as wl
# String/text compression
b = wl.binary_generator(10000, 0.8)
print('Original Msg')
print(b)
# print(sys.getsizeof(b))

def rle_compres(s):
    temp = -1
    l = len(s)
    compressed_s = ''
    counter = 0
    for i in range(l):
        if i != 0 and i != (l-1):
            if temp != s[i]:
                compressed_s += (str(counter) + temp)
                temp = s[i]
                counter = 1
            else: # temp == s[i]
                if counter != 9: counter += 1
                else: # counter == 9
                    compressed_s += (str(counter) + temp)
                    counter = 1
        elif i == 0: 
            temp  = s[i]
            counter += 1
        else: # i == l - 1
            if temp == s[i]:
                counter += 1
                compressed_s += (str(counter) + temp)
            else: # temp != s[i]
                compressed_s += (str(counter) + temp)
                compressed_s += ('1' + s[i])
    return compressed_s

def rle_decompres(s):
    l = len(s)
    decompressed_s = ''
    for i in range(0,l,2):
        num = int(s[i])
        c = s[i+1]
        for _ in range(num):
            decompressed_s += c
    return decompressed_s


compres_b = rle_compres(b)
print('Compressed Msg')
print(compres_b)
# print(sys.getsizeof(compres_b))
decompre_b = rle_decompres(compres_b)
print('Decompressed Msg')
print(decompre_b)
# print(sys.getsizeof(decompre_b))
print('Lossless: ', b == decompre_b)
print(sys.getsizeof(b))
print(sys.getsizeof(compres_b))
print('Compression ratio:', wl.compression_ratio(b, compres_b))


# Image/file compression

# def compress(src_path, dest_path):
#     with open(dest_path, 'wb') as dest:
#         with open(src_path, 'rb') as src:


