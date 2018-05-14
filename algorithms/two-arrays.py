#!/bin/python3

import sys

def twoArrays(k, A, B):
    res = 'YES'
    A = sorted(A)
    B = sorted(B, reverse=True)
    
    for el in zip(A, B):
        if sum(el) < k:
            res = 'NO'
            break
    
    return res
            

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        A = list(map(int, input().strip().split(' ')))
        B = list(map(int, input().strip().split(' ')))
        result = twoArrays(k, A, B)
        print(result)
