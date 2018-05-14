#!/bin/python3

import sys
from math import ceil

def workbook(n, k, arr):
    res = 0
    page = 1
    
    for el in arr:
        pr_cur = 1
        for pr in range(pr_cur, pr_cur + el):
            if pr == page + pr//k - (1 if pr%k == 0 else 0):
                res += 1
            #print("problem = {} page = {} page% = {} res = {}".format(pr, page + pr//k - (1 if pr%k == 0 else 0), pr%k, res))
        
        #print()
        
        if el%k == 0:
            page += el//k
        else:
            page += 1 + el//k
        #print("page at end: {}".format(page))
        
    return res

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = workbook(n, k, arr)
    print(result)
