#!/bin/python3

import sys

def camelcase(s):
    res = 1
    for let in s:
        if let.isupper():
            res += 1
    
    if not s:
        res = 0
    
    return res

if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)
