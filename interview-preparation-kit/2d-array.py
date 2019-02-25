#!/bin/python3

import sys


arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

    
best = 0
for ind_i in range(6-2):
    for ind_j in range(6-2):
        temp = 0
        temp += arr[ind_i][ind_j] + arr[ind_i][ind_j+1] + arr[ind_i][ind_j+2]
        temp += arr[ind_i+1][ind_j+1]
        temp += arr[ind_i+2][ind_j] + arr[ind_i+2][ind_j+1] + arr[ind_i+2][ind_j+2]
        if ind_i == 0 and ind_j == 0:
            best = temp
        else:
            best = max(best, temp)
    
print(best)