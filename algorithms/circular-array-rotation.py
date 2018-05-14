#!/bin/python3

import sys

def rightRotation(a, d):
    out = list(a)
    a_len = len(a)
    for ind, el in enumerate(a):
        out[(ind + d) % a_len] = el

    return out

def circularArrayRotation(a, m):
    out = []
    for pos in m:
        out.append(a[pos])
        
    return out
    

if __name__ == "__main__":
    n, k, q = input().strip().split(' ')
    n, k, q = [int(n), int(k), int(q)]
    a = list(map(int, input().strip().split(' ')))
    m = []
    m_i = 0
    for m_i in range(q):
        m_t = int(input().strip())
        m.append(m_t)
    a = rightRotation(a, k)
    result = circularArrayRotation(a, m)
    print ("\n".join(map(str, result)))


