#!/bin/python3
# stupid O(n^2) algorithm

import math
import sys

def miniMaxSum(arr):
    sum_min = math.inf
    sum_max = -math.inf
    sum_temp = 0
    
    for exclude in range(len(arr)):
        sum_temp = 0
        for ind, elem in enumerate(arr):
            if ind == exclude:
                continue
            sum_temp += elem
        if sum_temp < sum_min:
            sum_min = sum_temp
        if sum_temp > sum_max:
            sum_max = sum_temp
            
    print("{} {}".format(sum_min, sum_max))
    return sum_min, sum_max

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)
