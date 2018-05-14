#!/bin/python3

import sys

def luckBalance(n, k, arr):
    res = sum(list(map(lambda x: x[0], filter(lambda x: x[1] == 0, arr))))
    arr = sorted(arr, key=lambda x: (-x[1], -x[0]))
    important = len(list(filter(lambda x: x[1] == 1, arr)))
    kcnt = 0
    
    for ind in range(important):
        #print("res = {} adding {}".format(res, arr[ind][0]))
        if kcnt < k:
            res += arr[ind][0]
            kcnt += 1
        else:
            res -= arr[ind][0]
        
    #print(arr)
    return res

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    contests = []
    for contests_i in range(n):
        contests_t = [int(contests_temp) for contests_temp in input().strip().split(' ')]
        contests.append(contests_t)
    result = luckBalance(n, k, contests)
    print(result)
