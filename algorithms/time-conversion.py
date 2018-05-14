#!/bin/python3

import sys

def timeConversion(s):
    if 'AM' in s:
        s_split = s.replace('AM', '').split(':')
        if s_split[0] == '12':
            s_split[0] = '00'
        res = s_split[0] + ':' + s_split[1] + ':' + s_split[2]
        return res
    else:
        s_split = s.replace('PM', '').split(':')
        
        if s_split[0] != '12':
            s_split[0] = str(int(s_split[0]) + 12)
        res = s_split[0] + ':' + s_split[1] + ':' + s_split[2]
        return res

s = input().strip()
result = timeConversion(s)
print(result)
