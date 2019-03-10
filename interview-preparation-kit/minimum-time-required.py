#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def calculate_days(day, cnt):
    res = 0

    for el in cnt.items():
        res += el[1] * (day // el[0])

    return res


# Complete the minTime function below.
def minTime(machines, goal):
    cnt = Counter(machines)
    day_limit = 10**13
    curgoal = 0
    curday = 0
    res = 0
    prev_big = day_limit
    prev_low = 0

    curday = day_limit // 2

    while True:
        # detect if we are bouncing around in a loop
        if curday == prev_big or curday == prev_low:
            #print("curday = {} prev_low = {} prev_big = {}".format(curday, prev_low, prev_big))
            prev_low_res = calculate_days(prev_low, cnt)
            prev_big_res = calculate_days(prev_big, cnt)
            if prev_low_res >= goal:
                return prev_low
            else:
                return prev_big

        curgoal = calculate_days(curday, cnt)

        if curgoal < goal:
            prev_low = curday
            #print("micro curday = {} curgoal = {} < {}, diff = {}".format(curday, curgoal, goal, abs(curgoal - goal)))
            curday = curday + (1 + day_limit - curday)//2
            res = curday
        else:
            #print("micro curday = {} curgoal = {} > {}, diff = {}".format(curday, curgoal, goal, abs(curgoal - goal)))
            prev_big = curday
            day_limit = curday
            curday = curday // 2
            res = curday

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nGoal = input().split()

    n = int(nGoal[0])

    goal = int(nGoal[1])

    machines = list(map(int, input().rstrip().split()))

    ans = minTime(machines, goal)

    fptr.write(str(ans) + '\n')

    fptr.close()
