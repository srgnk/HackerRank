#!/bin/python3

import sys

def solve(n, bar, d, m):
    res = 0
    
    for a_i in range(len(bar)-m+1):
        if sum(bar[a_i:a_i+m]) == d:
            res += 1
    
    return res

n = int(input().strip())
bar = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, bar, d, m)
print(result)
