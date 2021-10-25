#!/bin/python3

import sys

def compare triplets(a,b):
    x=y= 0
    nas =[]
    for i in range(0,len(a)):
     if a[i]>b[i]:
            x=x+1
     elif b[i]>a[i]:
            y=y+1
     else:
          continue
    nas.append(x)
    nas.append(y)
    return nas

   



