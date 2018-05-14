#!/usr/bin/env python3

if __name__ == "__main__":
    n = int(input().strip())
    english = set(map(int, input().strip().split(' ')))
    m = int(input().strip())
    french = set(map(int, input().strip().split(' ')))
    
    print(len(english.union(french)))
    
