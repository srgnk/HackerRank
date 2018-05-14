#!/bin/python3

import sys


def closestNumbers(arr):
    output = []
    arr = sorted(arr)
    nowmin = 10**9
    
    for ind in range(1, len(arr)):
        diff = abs(arr[ind-1] - arr[ind])
        
        if diff < nowmin:
            output = [(arr[ind-1], arr[ind])]
            nowmin = diff
        elif diff == nowmin:
            output.append((arr[ind-1], arr[ind]))
            
    flat_list = [item for sublist in output for item in sublist]
        
    return flat_list
    

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = closestNumbers(arr)
    print (" ".join(map(str, result)))


