#!/usr/bin/env python3

from collections import deque

if __name__ == "__main__":
    num = int(input().strip())
    deq = deque()
    
    for _ in range(num):
        args = input().strip().split()
        
        if args[0] == 'append':
            deq.append(args[1])
        elif args[0] == 'appendleft':
            deq.appendleft(args[1])
        elif args[0] == 'pop':
            deq.pop()
        elif args[0] == 'popleft':
            deq.popleft()
            
    out = []
    for el in deq:
        out.append(el)
            
    print(" ".join(map(str, out)))