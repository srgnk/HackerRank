#!/bin/python3

import sys

def marsExploration(s):
    res = 0
    for ind in range(0, len(s), 3):
        if s[ind] != 'S':
            res += 1
        if s[ind+1] != 'O':
            res += 1
        if s[ind+2] != 'S':
            res += 1
            
    return res
        

if __name__ == "__main__":
    s = input().strip()
    result = marsExploration(s)
    print(result)
