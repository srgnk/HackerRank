#!/bin/python3

import sys

def check(array):
    return len(list(filter(lambda x: x%2 == 0, array))) == len(array)

def fairRations(B):
    res = 0
    
    for ind in range(len(B)-1):
        if B[ind]%2 == 1:
            B[ind] += 1
            B[ind+1] += 1
            res += 2
            
    return res if check(B) else 'NO'

if __name__ == "__main__":
    N = int(input().strip())
    B = list(map(int, input().strip().split(' ')))
    result = fairRations(B)
    print(result)
