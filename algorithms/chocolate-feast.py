#!/bin/python3

import sys

def wrappers(wr, m):
    res = 0
    if wr//m > 0:
        res += wr//m + wrappers(wr//m + wr%m, m)
    return res
    

def chocolateFeast(n, c, m):
    return n//c + wrappers(n//c, m)


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, c, m = input().strip().split(' ')
        n, c, m = [int(n), int(c), int(m)]
        result = chocolateFeast(n, c, m)
        print(result)
