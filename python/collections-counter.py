#!/usr/bin/env python3

from collections import Counter

if __name__ == "__main__":
    X = int(input().strip())
    shoes = list(map(int, input().strip().split()))
    N = int(input().strip())
    result = 0
    
    warhs = Counter(shoes)
    for _ in range(N):
        size, money = map(int, input().strip().split(' '))
        
        if warhs[size] > 0:
            result += money
            warhs[size] -= 1
        
    print(result)
    