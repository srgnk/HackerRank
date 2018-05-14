#!/bin/python3

import sys

def largestRectangle(h):
    res = 0
    
    for i in range(len(h)):
        length = 0
        for j in range(i, -1, -1):
            if h[j] >= h[i]:
                length += 1
            else:
                break
                
        for j in range(i+1, len(h)):
            if h[j] >= h[i]:
                length += 1
            else:
                break
        
        res = max(res, length*h[i])
            
    return res

if __name__ == "__main__":
    n = int(input().strip())
    h = list(map(int, input().strip().split(' ')))
    result = largestRectangle(h)
    print(result)
