#!/usr/bin/env python3

if __name__ == "__main__":
    happiness = 0
    n, m = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    
    good = set(map(int, input().strip().split(' ')))
    bad = set(map(int, input().strip().split(' ')))
    
    for el in arr:
        if el in good:
            happiness += 1
        elif el in bad:
            happiness -= 1
    
    print(happiness)