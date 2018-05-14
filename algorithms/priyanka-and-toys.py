#!/bin/python3

import sys

def toys(w):
    w = sorted(w)
    res = 0
    limit = -1
    
    for el in w:
        if el > limit:
            limit = el + 4
            res += 1
    
    return res

if __name__ == "__main__":
    n = int(input().strip())
    w = list(map(int, input().strip().split(' ')))
    result = toys(w)
    print(result)
