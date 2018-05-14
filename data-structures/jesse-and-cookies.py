#!/usr/bin/env python3

import heapq as hq

if __name__ == "__main__":
    n, k = map(int, input().strip().split(' '))
    candies = list(map(int, input().strip().split(' ')))
    q = []
    res = 0
    
    for el in candies:
        hq.heappush(q, el)
    
    while any(c < k for c in q) and len(q) > 1:
        last = hq.heappop(q)
        prelast = hq.heappop(q)
        
        new = last + 2*prelast
        
        hq.heappush(q, new)
        res += 1
        
    if all(c >= k for c in q):
        print(res)
    else:
        print(-1)
        