#!/bin/python3

import sys

def libraryFine(d1, m1, y1, d2, m2, y2):
    fine = 0
    
    if y1 > y2:
        fine = 10000
    elif m1 > m2 and y1 == y2:
        fine = 500 * (m1 - m2)
    elif d1 > d2 and m1 == m2 and y1 == y2:
        fine = 15 * (d1 - d2)
        
    return fine

if __name__ == "__main__":
    d1, m1, y1 = input().strip().split(' ')
    d1, m1, y1 = [int(d1), int(m1), int(y1)]
    d2, m2, y2 = input().strip().split(' ')
    d2, m2, y2 = [int(d2), int(m2), int(y2)]
    result = libraryFine(d1, m1, y1, d2, m2, y2)
    print(result)
