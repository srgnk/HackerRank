#!/bin/python3

import sys

def sequence(N):
    x = N % 8
    if x == 0 or x == 1:
        return N
    if x == 2 or x == 3:
        return 2
    if x == 4 or x == 5:
        return N+2
    if x == 6 or x == 7:
        return 0

def solution(L, R):
    res = 0
    if (R - L) % 2 == 1:
        for ind in range(L+1, R+1, 2):
            res ^= ind
    else:
        for ind in range(L+1):
            res ^= ind
        for ind in range(L+2, R+1, 2):
            res ^= ind
            
    return res
        

Q = int(input().strip())
for a0 in range(Q):
    L,R = input().strip().split(' ')
    L,R = [int(L),int(R)]
    #print(solution(L,R))
    print(sequence(L-1)^sequence(R))
