#!/bin/python3

import sys

def diagonalDifference(a):
    # compute primary diagonal
    n = len(a)
    diag_pr = diag_sec = 0
    for i in range(n):
        diag_pr += a[i][i]
        diag_sec += a[n-i-1][i]
    
    return abs(diag_pr - diag_sec)

if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
       a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
       a.append(a_t)
    result = diagonalDifference(a)
    print(result)
