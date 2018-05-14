#!/bin/python3
# try a dumb bruteforce

import sys
from itertools import combinations

def check_array(k, arr):
    for el1 in arr:
        test_arr = list(arr)
        test_arr.remove(el1)
        
        for el2 in test_arr:
            if (el1 + el2) % k == 0:
                return False
    return True

def nonDivisibleSubset_brute(k, arr):
    if check_array(k, arr):
        return len(arr)
    
    best = 0
    for num in range(1, len(arr)):
        to_remove = list(combinations(arr, num))
        #print("to_remove = {}".format(to_remove))
        for option in to_remove:
            test_arr = list(arr)
            #print("test_arr = {}".format(test_arr))
            for el in option:
                test_arr.remove(el)

            if check_array(k, test_arr) == True:
                best = max(len(test_arr), best)

    return best

def nonDivisibleSubset(k, arr):
    resid_cnt = [0] * k
    
    for el in arr:
        resid_cnt[el%k] += 1
        
    res = min(1, resid_cnt[0])
    for ind in range(1, (k//2)+1):
        if ind != k - ind:
            res += max(resid_cnt[ind], resid_cnt[k - ind])
    
    if k % 2 == 0 and resid_cnt[int(k/2)] != 0:
        res += 1
    
    return res
    
if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = nonDivisibleSubset(k, arr)
    print(result)
