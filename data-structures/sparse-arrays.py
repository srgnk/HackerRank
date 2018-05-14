#!/usr/bin/env python3

if __name__ == "__main__":
    strings = []
    N = int(input().strip())
    for _ in range(N):
        strings.append(input().strip())
        
    Q = int(input().strip())
    for _ in range(Q):
        substr = input().strip()
        print(strings.count(substr))
    