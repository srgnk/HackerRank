#!/bin/python3

import sys

def bonAppetit(n, skip, b, ar):
    sum_actual = 0
    
    ar.pop(skip)
    sum_actual = sum(ar)//2
    
    if sum_actual == b:
        return 'Bon Appetit'
    else:
        return b - sum_actual
        

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
