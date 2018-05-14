#!/usr/bin/env python3

from collections import deque

if __name__ == "__main__":
    t = int(input().strip())
    
    for _ in range(t):
        num_cnt = int(input().strip())
        deq = deque(list(map(int, input().strip().split(' '))))
        
        prev = max(deq[0], deq[-1])
        while deq:
            if prev >= deq[0] and prev >= deq[-1]:
                if deq[0] >= deq[-1]:
                    prev = deq.popleft()
                else:
                    prev = deq.pop()
            else:
                break
                
        if len(deq) == 0:
            print('Yes')
        else:
            print('No')
            
            