#!/bin/python3

import sys
from collections import Counter

def beautifulPairs(arr, brr):
    res = 0
    arr = sorted(arr)
    brr = sorted(brr)
    
    acnt = Counter(arr)
    bcnt = Counter(brr)
    
    spare = 0
    for el in acnt.items():
        if el[0] in bcnt:
            get = bcnt[el[0]]
            res += min(el[1], get)
        else:
            spare += el[1]
        
    #print("res = {} spare = {}".format(res, spare))
    
    if spare:
        res += 1
    else:
        res -= 1
    
    return res

if __name__ == "__main__":
    n = int(input().strip())
    A = list(map(int, input().strip().split(' ')))
    B = list(map(int, input().strip().split(' ')))
    result = beautifulPairs(A, B)
    print(result)
