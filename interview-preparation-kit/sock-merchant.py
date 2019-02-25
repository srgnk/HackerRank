#!/bin/python3

import sys

def sockMerchant(n, ar):
    socks = {}
    res = 0
    
    for el in ar:
        if el not in socks.keys():
            socks[el] = 1
        else:
            socks[el] += 1
    
    for key in socks.keys():
        res += socks[key]//2
    
    return res

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
