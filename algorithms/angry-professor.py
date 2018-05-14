#!/bin/python3

import sys

def angryProfessor(k, a):
    res = 'NO'
    if len(list(filter(lambda x: x <= 0, a))) < k:
        res = 'YES'
    return res

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        a = list(map(int, input().strip().split(' ')))
        result = angryProfessor(k, a)
        print(result)
