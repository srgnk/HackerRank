#!/bin/python3

import sys

def maximumToys(prices, k):
    prices = sorted(prices)
    res = 0
    
    for el in prices:
        if k - el >= 0:
            k -= el
            res += 1
        else:
            break
        
    return res
    

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    prices = list(map(int, input().strip().split(' ')))
    result = maximumToys(prices, k)
    print(result)
