#!/usr/bin/env python3

n,m = map(int, input().split())

t1 = [0] * 100010
t2 = [0] * 100010
tt = int(0)

for i in range(n):
    l,r = map(int, input().split())
    t1[l] += 1
    t2[r+1] -= 1

for i in range(1,100010):
    t1[i] += t1[i-1]
    t2[i] += t2[i-1]

for i in range(m):
    l,r = map(int, input().split())
    tt += t1[r] + t2[l]

print(tt)