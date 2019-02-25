#!/bin/python3

import sys

def _digitSum(number):
    if len(number) == 1:
        return int(number)
    else:
        temp = str(sum([int(x) for x in number]))
        return _digitSum(temp)

def digitSum(number, k):
    temp = str(k*sum([int(x) for x in number]))
    return _digitSum(temp)
    
    
if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [str(n), int(k)]
    result = digitSum(n, k)
    print(result)
