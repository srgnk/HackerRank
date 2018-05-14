#!/bin/python3

import sys

def check_a(number, a):
    for el in a:
        if number % el != 0:
            return False
    return True

def check_b(number, b):
    for el in b:
        if el % number != 0:
            return False
    return True

def getTotalX(a, b):
    res = 0
    max_a = max(a)
    min_b = min(b)
    
    probe = max_a
    
    while probe <= min_b:
        if check_a(probe, a) and check_b(probe, b):
            res += 1
        probe += max_a
        
    return res
    

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
