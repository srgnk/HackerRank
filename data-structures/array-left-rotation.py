#!/bin/python3

import sys

def leftRotation(a, d):
    out = list(a)
    a_len = len(a)
    for ind, el in enumerate(a):
        out[(ind + a_len - d) % a_len] = el

    return out
        
if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = list(map(int, input().strip().split(' ')))
    result = leftRotation(a, d)
    print (" ".join(map(str, result)))


