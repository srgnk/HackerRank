#!/bin/python3

import sys

def is_leap_greg(year):
    return (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))

def is_leap_jul(year):
    return year % 4 == 0

def solve(year):
    target = 256
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if year < 1918:
        if is_leap_jul(year):
            months[1] = 29
    elif year > 1919:
        if is_leap_greg(year):
            months[1] = 29
    elif year == 1918:
        target += 13
    
    sum_tmp = 0
    for ind, el in enumerate(months):
        if sum_tmp + el > target:
            month = '0' + str(ind + 1)
            day = target - sum_tmp
            break
        else:
            sum_tmp += el
            
    return ".".join([str(day), str(month), str(year)])

year = int(input().strip())
result = solve(year)
print(result)
