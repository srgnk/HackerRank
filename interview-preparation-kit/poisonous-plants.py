#!/bin/python3

import sys

def do_day(arr):
    prev = arr[0]
    res = [arr[0]]
    for el in arr[1:]:
        temp = el
        if el <= prev:
            #print("{} > {}".format(el, prev))
            #arr.remove(el)
            res.append(el)
        prev = temp
    return res

def poisonousPlants_brute(arr):
    res = 0
    arr_prev = []
    arr_cur = arr
    while arr_cur != arr_prev:
        #print("cur = {} prev = {}".format(arr_cur, arr_prev))
        arr_cur, arr_prev = do_day(list(arr_cur)), arr_cur
        res += 1
        
    return res - 1
    
def poisonousPlants(arr):
    stack = [0]
    days = [0] * len(arr)
    pivot = arr[0]
    res = 0
    
    for ind in range(1, len(arr)):
        if arr[ind] > arr[ind - 1]:
            days[ind] = 1
            
        pivot = min(pivot, arr[ind])
        
        #print("stack = {}".format(stack))
        while stack and arr[stack[-1]] >= arr[ind]:
            if arr[ind] > pivot:
                days[ind] = max(days[ind], days[stack[-1]] + 1)
                
            stack.pop()
            
        res = max(res, days[ind])
        stack.append(ind)
            
            
    return res
    

if __name__ == "__main__":
    n = int(input().strip())
    p = list(map(int, input().strip().split(' ')))
    result = poisonousPlants(p)
    print(result)
