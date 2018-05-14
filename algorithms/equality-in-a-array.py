#!/bin/python3

import sys
from collections import Counter

def equalizeArray(arr):
    cnt = Counter(arr)
    
    m_el_num = max(cnt.items(), key = lambda x: x[1])
    
    return len(arr) - m_el_num[1]
    

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = equalizeArray(arr)
    print(result)
