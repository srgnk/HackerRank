#!/bin/python3

import sys

def countingValleys(n, s):
    res = 0
    in_valley = 0
    curr = 0
    
    for step in s:
        if step == 'U':
            curr += 1
        else:
            curr -= 1
        
        if curr < 0 and in_valley == 0:
            in_valley = 1
        if in_valley == 1 and curr == 0:
            in_valley = 0
            res += 1

    return res

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)
