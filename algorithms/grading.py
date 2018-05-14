#!/bin/python3

import sys

def solve(grades):
    res = []
    
    for el in grades:
        if el < 38:
            res.append(el)
        elif el%5 >= 3:
            res.append(el + 5-el%5)
        else:
            res.append(el)
    return res

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))


