#!/bin/python3

import sys

def jump(c):
    res = 0
    ind = 0
    
    while ind != len(c)-1:
        if ind != len(c)-2 and c[ind+2] == 0:
            ind += 2
        else:
            ind += 1
        res += 1
        
    return res
    

if __name__ == "__main__":
    n = int(input().strip())
    c = list(map(int, input().strip().split(' ')))
    result = jump(c)
    print(result)
