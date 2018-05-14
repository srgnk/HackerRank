#!/bin/python3

import sys

def solution():
    res = 0
    cnt = 0
    for ind in range(len(topic)-1):
        for jnd in range(ind+1, len(topic)):
            tmp = bin(int(topic[ind], 2) | (int(topic[jnd], 2))).count("1")
            if tmp > res:
                res = tmp
                cnt = 1
            elif tmp == res:
                cnt += 1

    return (res, cnt)


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in range(n):
    topic_t = str(input().strip())
    topic.append(topic_t)

print("\n".join(map(str, solution())))
