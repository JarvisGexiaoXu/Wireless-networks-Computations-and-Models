# In this folder, I create a list of wireless networks computational functions.
# These functions are used to facilitate the future computation and emphasize 
# my understanding of the course material.
import sys
# --------------------------Lecture 2 page 9-10------------------------------
# Huffman Codes

# Creating tree nodes
class Node(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

context = "Lionel Andrés Messi, also known as Leo Messi, is an Argentine professional footballer who plays as a forward for Ligue 1 club Paris Saint-Germain and captains the Argentina national team."
# The main function
def Huffman_Coding(s):
    # Remove duplicates
    temp = []
    l = len(s) # Length of the original text
    prob = [] # probablity (frequency) list
    for c in s: 
        if c not in temp: temp.append(c)
    
    # Compute probabilities (frequency)
    for c in temp:
        prob.append(s.count(c)/l)

    # E = 0
    # temp_prob = prob.copy()
    # temp_prob.sort()
    # print(len(temp_prob))
    # for i in range(len(temp_prob)):
    #     E += (temp_prob[i] * (i+1))
    # print("The average number of bits per symbol is ",E)

    # Create Huffman Tree    
    head = Node()
    form_Huffman_Tree(head, prob, temp)

    # Retuen the head of the generated Huffman Tree
    return head


def form_Huffman_Tree(node, prob, s):
    # Base case len(prob) == 1
    p = max(prob)
    i = prob.index(p)
    node.left = s[i] 
    if len(prob) > 1:
        del prob[i]
        del s[i]
        new_node = Node()
        node.right = new_node
        form_Huffman_Tree(new_node, prob, s)

def encode_char_Huffman(node, target):
    if node.left == target: return '0'
    else:
        return '1' + encode_char_Huffman(node.right, target)

def encode_str_Huffman(node, s):
    code = ''
    for c in s:
        code += encode_char_Huffman(node, c)
    return code

def decode_str_Huffman(head, code):
    temp = head
    s = ''
    for c in code:
        if c == '1': temp = temp.right
        elif c == '0':
            s = s + temp.left
            temp = head
    return s

print("The original message:")
print(context)
size_original_msg = sys.getsizeof(context) * 8
print("Get the size of the original message:", size_original_msg)
head = Huffman_Coding(context)
encoded_msg = encode_str_Huffman(head, context)
encoded_msg_int = int(encoded_msg)
print("Encoded using Huffman code:")
print(encoded_msg)
print("Turning into numeric expression:")
print(encoded_msg_int)
size_encoded_msg = len(encoded_msg)
print("Get the size of the encoded message:", size_encoded_msg)
decoded_msg = decode_str_Huffman(head, encoded_msg)
print("The decoded message:")
print(decoded_msg)
print("Compression ratio", size_original_msg/size_encoded_msg)