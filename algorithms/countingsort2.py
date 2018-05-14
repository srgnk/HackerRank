#!/bin/python3

import sys

def countingSort(arr):
    cnt = [0] * (max(arr) + 1)
    output = [0] * (len(arr))
    
    for el in arr:
        cnt[el] += 1
        
    total = 0
    for ind in range(len(cnt)):
        old = cnt[ind]
        cnt[ind] = total
        total += old
        
    for el in arr:
        output[cnt[el]] = el
        cnt[el] += 1
        
    return output

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = countingSort(arr)
    print (" ".join(map(str, result)))


