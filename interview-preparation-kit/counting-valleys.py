#!/bin/python3

import sys

def countingValleys(n, s):
    stepSum=0
    valleyCount=0
    for i in path:
        stepSum=stepSum+1 if i=="U" else stepSum
        stepSum=stepSum-1 if i=="D" else stepSum
        if stepSum==0 and i=="U":
            valleyCount=valleyCount+1
    return (valleyCount)   

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    result = countingValleys(n, s)
    print(result)
