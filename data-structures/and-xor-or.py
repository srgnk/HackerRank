#!/usr/bin/env python3
    
def solution(arr):
    res = 0
    stack = []
    
    for el in arr:
        while stack:
            res = max(res, el^stack[-1])
            
            if el < stack[-1]:
                stack.pop()
            else:
                break
        stack.append(el)
            
    return res
            
if __name__ == "__main__":
    n = int(input().strip())
    arr = [int(x) for x in input().strip().split()]
    print(solution(arr))