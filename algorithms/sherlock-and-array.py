#!/bin/python3

import sys

def solve(arr):
    res = 'NO'
    right = sum(arr)
    left = 0
    
    for el in arr:
        right -= el
        
        #print("left = {} el = {} right = {}".format(left, el, right))
        if right == left:
            res = 'YES'
            break
            
        left += el
            
    return res

T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = solve(a)
    print(result)
