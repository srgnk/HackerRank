#!/bin/python3

import sys

def calc_pattern():
    max_n = 50
    ads = 5
    output = []
    for i in range(max_n):
        output.append(ads//2)
        ads = (ads//2)*3
        
    return output

def viralAdvertising(n, pattern):
    return sum(pattern[:n])

if __name__ == "__main__":
    n = int(input().strip())
    pattern = calc_pattern()
    result = viralAdvertising(n, pattern)
    print(result)
