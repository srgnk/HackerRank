#!/bin/python3

import sys

def alternatingCharacters(s):
    string = list(s)
    last = string.pop()
    res = 0
    
    while string:
        newone = string.pop()
        if newone == last:
            res += 1
        else:
            last = newone
        
    return res

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)
