#!/bin/python3

import sys

def max_permutation(n, k):
    #array = [x for x in range(1, n+1)]
    out = []
    switch = k
    if k == 0:
        return [x for x in range(1, n+1)]
    
    if n % (2*k) != 0:
        return [-1]
        
    for pos in range(1, n + 1):
        out.append(pos + switch)
        
        if pos % k == 0:
            switch *= -1
            
    return out
        
        

t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n),int(k)]
    
    print(" ".join(list(map(str, max_permutation(n, k)))))
