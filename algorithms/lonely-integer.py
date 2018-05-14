#!/bin/python3

import sys

def lonely_integer(a):
    res = 0
    for elem in a:
        res ^= elem
    return res
    

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))