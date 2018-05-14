#!/bin/python3

import sys

def appleAndOrange(s, t, a, b, apple, orange):
    count_app = 0
    count_org = 0
    for el in apple:
        if s <= el+a <= t:
            count_app += 1
    
    for el in orange:
        if s <= el+b <= t:
            count_org += 1
    
    return [ count_app, count_org ]

if __name__ == "__main__":
    s, t = input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = list(map(int, input().strip().split(' ')))
    orange = list(map(int, input().strip().split(' ')))
    result = appleAndOrange(s, t, a, b, apple, orange)
    print ("\n".join(map(str, result)))


