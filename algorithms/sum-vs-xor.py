#!/bin/python3

import sys

def solve(n):
    res = 1
    n_bin = bin(n).replace('0b', '')
    
    if (n == 0):
        return 1
    
    for digit in n_bin:
        if digit == '0':
            res *= 2
        
    return res

n = int(input().strip())
result = solve(n)
print(result)
