#!/usr/bin/env python3

if __name__ == "__main__":
    N = int(input().strip())
    stamps = set()
    
    for _ in range(N):
        stamp = input().strip()
        stamps.add(stamp)
        
    print(len(stamps))