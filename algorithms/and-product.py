#!/bin/python3
# try bruteforce

import sys
from math import log2

def andProduct(a, b):
    if a == 0:
        return 0
    if int(log2(a)) != int(log2(b)):
        return 0
    else:
        res_bin = list(bin(a)[2:])
        len_res = len(res_bin)
        for ind, digit in enumerate(res_bin):
            if ind == 0 or digit == '0':
                continue
            else:
                #print("ind = {}".format(ind))
                test_bin = list(bin(b)[2:])
                #test_bin = list(res_bin)
                test_bin[ind] = '0'
                #print(test_bin)
                #print(1 << (len_res - ind))
                #test_dec = b & (((1 << (ind-1) ) | 1) << len_res - ind)
                #test_dec = (((1 << (ind-1) ) | 1) << len_res - ind)
                #test_dec = b & (((1 << (ind-1) ) | 1) << len_res - ind)
                #print("test_dec1 = {}".format(1 << (ind-1)))
                #print("test_dec2 = {}".format((1 << (ind-1)) | 1))
                test_dec = int("".join(test_bin), 2)
                #print("test_dec3 = {}".format(((1 << (ind-1)) | 1) << len_res - ind))
                if a <= test_dec <= b:
                    res_bin[ind] = '0'
        return int("".join(res_bin), 2)
            
if __name__ == "__main__":
    n = int(input().strip())
    for a0 in range(n):
        a, b = input().strip().split(' ')
        a, b = [int(a), int(b)]
        result = andProduct(a, b)
        print(result)
