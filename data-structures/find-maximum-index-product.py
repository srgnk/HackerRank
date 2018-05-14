#!/usr/bin/env python3

import sys

def find_left(arr):
    lstack = [1]
    output = []
    
    for ind in range(1, len(arr)-1):
        while lstack and arr[lstack[-1]-1] <= arr[ind]:
            lstack.pop()
        
        left = lstack[-1] if lstack else 0
        lstack.append(ind+1)
        output.append(left)
    
    return output

def find_right(arr):
    arr_len = len(arr)
    rstack = [1]
    output = []
    
    for ind in range(1, len(arr)-1):
        while rstack and arr[rstack[-1]-1] <= arr[ind]:
            rstack.pop()
        
        right = arr_len - rstack[-1] + 1 if rstack else 0
        rstack.append(ind+1)
        output.append(right)
        
    return output[::-1]
    

def solution(arr):
    res = 0
    
    left = find_left(arr)
    right = find_right(arr[::-1])
    
    #print("left: {}".format(left))
    #print("rigt: {}".format(right))
    
    for el in zip(left, right):
        res = max(res, el[0]*el[1])
        
    return res

if __name__ == "__main__":
    n = int(input().strip())
    arr = [int(x) for x in input().strip().split()]
    
    print(solution(arr))