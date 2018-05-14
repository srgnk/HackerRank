#!/bin/python3

import sys

def get_open(page):
    return 1 + (page//2)

def solve(n, p):
    return min(get_open(p) - get_open(1), get_open(n) - get_open(p))
        
n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
