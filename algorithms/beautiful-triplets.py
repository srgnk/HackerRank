#!/bin/python3

import sys

def beautifulTriplets(d, arr):
    res = 0
    
    for el in arr:
        if el + d in arr and el + 2*d in arr:
            res += 1
            
    return res

    
if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    arr = list(map(int, input().strip().split(' ')))
    result = beautifulTriplets(d, arr)
    print(result)
