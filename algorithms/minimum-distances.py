#!/bin/python3

import sys

def minimumDistances(array):
    res = -1
    memo = [-1] * (10**5 + 3)
    
    for ind, el in enumerate(array):
        if memo[el] >= 0:
            res = min(res if res >= 0 else 10**5 + 2, ind - memo[el])
        memo[el] = ind
        
    return res

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = minimumDistances(a)
    print(result)
