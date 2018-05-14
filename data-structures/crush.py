#!/bin/python3

import sys

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    array = [0] * (n+1)
    for a0 in range(m):
        a, b, k = input().strip().split(' ')
        a, b, k = [int(a), int(b), int(k)]
        
        array[a-1] += k
        if b+1 <= n:
            array[b] -= k
        
    res_max = 0
    res = 0
    for dif in array:
        res += dif
        res_max = max(res_max, res)
        
    print(res_max)
        
        
