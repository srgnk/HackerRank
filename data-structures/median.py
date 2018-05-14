#!/usr/bin/env python3

import sys
from bisect import insort
    
def median(a_sorted):
    if len(a_sorted) == 0:
        return "Wrong!"
    res = 0
    half = len(a_sorted)//2
    
    if len(a_sorted) % 2 == 0:
        res = (a_sorted[half-1] + a_sorted[half])/2
    else:
        res = a_sorted[half]
    if res - int(res) == 0:
        res = int(res)
    return res
        
if __name__ == "__main__":
    N = int(input())
    array = []
    output = []
    for i in range(N):
        op, num = input().strip().split()
        num = int(num)
        #print("array is {} op = {} num = {}".format(array, op, num))
        
        if op == 'a':
            insort(array, num)
            output.append(median(array))
        elif op == 'r':
            if num in array:
                array.remove(num)
                output.append(median(array))
            else:
                output.append("Wrong!")
                
    print("\n".join(map(str, output)))