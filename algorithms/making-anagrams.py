#!/bin/python3

import sys
from collections import Counter

def makingAnagrams(s1, s2):
    res = 0
    
    cnt1 = Counter(s1)
    cnt2 = Counter(s2)
    cnt3 = {}
    
    for let, val in cnt1.items():
        cnt3[let] = abs(val - cnt2[let])
    for let, val in cnt2.items():
        cnt3[let] = abs(val - cnt1[let])
        
    for el in cnt3.values():
        res += el
    
    return res


s1 = input().strip()
s2 = input().strip()
result = makingAnagrams(s1, s2)
print(result)
