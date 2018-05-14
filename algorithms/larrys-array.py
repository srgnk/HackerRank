#!/bin/python3

import sys

def rotate(A, pos):
    A[pos], A[pos+1], A[pos+2] = A[pos+1], A[pos+2], A[pos]

def larrysArray(A):
    for _ in range(len(A)):
        for ind in range(1, len(A) - 1):
            a, b, c = A[ind-1], A[ind], A[ind+1]
            #print("ind = {} A = {} B = {} C = {}".format(ind, a, b, c))
            if a > b or c < a:
                #print("rotating 1")
                rotate(A, ind-1)
        
    if A == sorted(A):
        return 'YES'
    else:
        return 'NO'

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        A = list(map(int, input().strip().split(' ')))
        result = larrysArray(A)
        print(result)
