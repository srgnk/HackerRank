#!/usr/bin/env python3

import heapq as hq

if __name__ == "__main__":
    cms_cnt = int(input().strip())
    q = []
    t_finished = 0
    wait_times = []
    customers = []
    
    for _ in range(cms_cnt):
        customers.append([int(x) for x in input().strip().split()])
    customers = sorted(customers, key = lambda x: -x[0])
        
    cur_time = 0
    while customers or q:
        while customers and cur_time > customers[-1][0]:
            hq.heappush(q, customers.pop()[::-1])
        
        if q:
            newcms = hq.heappop(q)
            cur_time += newcms[0]
            wait_times.append(cur_time - newcms[1])
        else:
            hq.heappush(q, customers.pop()[::-1])
            cur_time = q[0][1]
    
    print(sum(wait_times)//cms_cnt)
        