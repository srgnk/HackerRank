#!/bin/python3

import sys

def pickingNumbers(arr):
    arr_s = sorted(arr)
    res = 1
    cur = 1
    diff = 0
    for ind in range(1, len(arr_s)):
        #print("arr[{}] - arr[{}] = {} - {} res = {} cur = {}".format(ind, ind - 1, arr_s[ind], arr_s[ind - 1], res, cur))
        diff += arr_s[ind] - arr_s[ind - 1]
        if diff > 1:
            res = max(res, cur)
            cur = 1
            diff = 0
        else:
            cur += 1
            
    res = max(res, cur)
    
    return res
        

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = pickingNumbers(a)
    print(result)
