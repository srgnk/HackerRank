#!/bin/python3

import sys

allres = []

def k_factorization(n, arr, cur, result):
    #print("n = {} cur = {} arr = {} res = {}".format(n, cur, arr, result))
    if cur == n:
        allres.append(list(result))
        return True
    elif cur > n:
        return False
    
    for ind, el in enumerate(arr):
        result.append(cur*el)
        
        k_factorization(n, arr[ind:], cur*el, result)
        
        result.pop()
    
    return False

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = sorted(list(map(int, input().strip().split(' '))))
    result = [1]
    k_factorization(n, arr, 1, result)
    #print("final: {}".format(allres))
    if not allres:
        print(-1)
    else:
        print(" ".join(list(map(str, min(allres, key = len)))))


