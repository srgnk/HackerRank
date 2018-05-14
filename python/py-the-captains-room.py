#!/usr/bin/env python3

if __name__ == "__main__":
    k = int(input().strip())
    numbers = list(map(int, input().strip().split(' ')))
    
    print((sum(set(numbers))*k - sum(numbers))//(k-1))