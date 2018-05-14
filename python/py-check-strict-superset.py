#!/usr/bin/env python3

if __name__ == "__main__":
    A = set(map(int, input().strip().split(' ')))
    t = int(input().strip())
    superset = True
    
    for _ in range(t):
        subset = set(map(int, input().strip().split(' ')))
        if len(subset - A) != 0 or len(A - subset) == 0:
            superset = False
            break
    
    print(superset)