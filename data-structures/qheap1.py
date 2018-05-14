#!/usr/bin/env python3

import heapq as hq
from bisect import insort

if __name__ == "__main__":
    t = int(input().strip())
    q = []
    
    for _ in range(t):
        args = input().strip().split()
        if args[0] == '1':
            insort(q, int(args[1]))
            #hq.heappush(q, int(args[1]))
        elif args[0] == '2':
            q.remove(int(args[1]))
            #hq.heapify(q)
        elif args[0] == '3':
            print(q[0])
            