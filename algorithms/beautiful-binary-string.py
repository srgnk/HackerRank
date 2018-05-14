#!/bin/python3

import sys

def beautifulBinaryString(b):
    res = 0
    
    while '010' in b:
        #print("found res = {} b = {}".format(res, b))
        res += 1
        b = b.replace("010","011", 1)
        
    return res
        

if __name__ == "__main__":
    n = int(input().strip())
    b = input().strip()
    result = beautifulBinaryString(b)
    print(result)
