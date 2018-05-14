#!/bin/python3

import sys
from collections import Counter

def anagram(s):
    if len(s)%2 == 1:
        return -1
    
    res = 0
    
    cnt1 = Counter(s[:len(s)//2])
    cnt2 = Counter(s[len(s)//2:])
    cnt3 = {}
    
    for let, val in cnt1.items():
        cnt3[let] = abs(val - cnt2[let])
    for let, val in cnt2.items():
        cnt3[let] = abs(val - cnt1[let])
        
    for el in cnt3.values():
        res += el
    
    return res//2

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = anagram(s)
    print(result)
