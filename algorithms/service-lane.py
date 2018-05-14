#!/bin/python3

import sys

def check_interval(i, j):
    res = 3
    for inter in range(i, j + 1):
        res = min(res, width[inter])
    
    return res

n,t = input().strip().split(' ')
n,t = [int(n),int(t)]
width = [int(width_temp) for width_temp in input().strip().split(' ')]
for a0 in range(t):
    i,j = input().strip().split(' ')
    i,j = [int(i),int(j)]
    
    print(check_interval(i, j))
