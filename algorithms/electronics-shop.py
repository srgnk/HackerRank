#!/bin/python3

import sys
from collections import defaultdict
from itertools import product

def getMoneySpent(keyboards, drives, s):
    res = -1
    #keyboards = sorted(keyboards)
    #drives = sorted(drives)
    
    #for ind in min(len(keyboards), len(drives)):
    
    variants = list(filter(lambda x: sum(x) <= s, list(product(keyboards, drives))))
    if variants:
        res = sum(max(variants, key = sum))
    
    return res
        
        
        

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
