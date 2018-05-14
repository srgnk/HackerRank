#!/bin/python3

import sys


g = int(input().strip())
for a0 in range(g):
    n,m,x = input().strip().split(' ')
    n,m,x = [int(n),int(m),int(x)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    
    a = a[::-1]
    b = b[::-1]
    
    handy_stack = []
    el_count = 0
    total = 0
    
    while len(a) > 0:
        if total + a[-1] <= x:
            temp = a.pop()
            handy_stack.append(temp)
            total += temp
            el_count += 1
        else:
            break
            
    
    total_b = 0
    while len(b) > 0:
        if total_b + b[-1] <= x:
            if total + b[-1] <= x:
                temp = b.pop()
                total += temp
                total_b += temp
                el_count += 1
            else:
                temp = b.pop()
                total = total - handy_stack.pop() + temp
                total_b += temp
        else:
            break
            
    print(el_count)
                
            
        
            
    
    
    