#!/bin/python3

import sys

def equalize(arr):
    res = 0
    for el in arr:
        while el != 0:
            if el == 1 or el == 2 or el == 5:
                el -= el
                res += 1
            elif el == 3 or el == 4:
                el -= el
                res += 2
            else:
                res += el//5
                el = int(el%5)
    return res

def equal(arr):
    res = 10**8
    arr_sorted = sorted(arr)
    arr_min = min(arr_sorted)
    
    for ind in range(3):
        arr_new = [ x - arr_min + ind for x in arr_sorted ]
        res = min(res, equalize(arr_new))
    
    return res

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = equal(arr)
        print(result)
