#!/usr/bin/env python3

import heapq as hq

if __name__ == "__main__":
    n = int(input().strip())
    minq = []
    maxq = []
    median = int(input().strip())
    hq.heappush(maxq, -median)
    print("{:.1f}".format(float(median)))
    
    for _ in range(n-1):
        getnew = int(input().strip())
        
        if getnew >= median:
            hq.heappush(minq, getnew)
        else:
            hq.heappush(maxq, -getnew)
            
        if len(minq) - len(maxq) > 1:
            hq.heappush(maxq, -hq.heappop(minq))
        elif len(maxq) - len(minq) > 1:
            hq.heappush(minq, -hq.heappop(maxq))
        
        if len(maxq) == len(minq):
            median = (minq[0] - maxq[0])/2
        else:
            if len(minq) > len(maxq):
                median = minq[0]
            else:
                median = -maxq[0]
        
        print("{:.1f}".format(median))
        