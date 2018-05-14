#!/bin/python3

import sys

def theGreatXor(x):
    res = 0
    n_bin = bin(x).replace('0b', '')
    
    for ind, digit in enumerate(reversed(n_bin)):
        if digit == '0':
            res += pow(2, ind)
        
    return res


q = int(input().strip())
for a0 in range(q):
    x = int(input().strip())
    result = theGreatXor(x)
    print(result)
