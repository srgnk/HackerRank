#!/bin/python3

import sys
from collections import Counter

def is_palindrome(s):
    return s == s[::-1]

def palindromeIndex(s):
    ret = -1
    lens = len(s)
    ind = 0
    
    if is_palindrome(s):
        return ret
    
    while ind < lens//2:
        if s[ind] != s[lens-ind-1]:
            if s[ind+1] == s[lens-ind-1] and s[ind+2] == s[lens-ind-2]:
                ret = ind
                break
            else:
                ret = lens-ind-1
                break
        ind += 1
    
    return ret
    

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = palindromeIndex(s)
    print(result)
