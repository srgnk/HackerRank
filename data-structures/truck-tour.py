#!/usr/bin/env python3

import queue

if __name__ == "__main__":
    n = int(input().strip())
    res = 0
    tank = 0
    q = queue.Queue()

    
    for ind in range(n):
        petr, dist = [int(arg) for arg in input().strip().split()]
        tank += petr
        
        if dist <= tank:
            tank -= dist
        else:
            tank = 0
            res = ind+1
            
        q.put((petr, dist))
            
    print(res)