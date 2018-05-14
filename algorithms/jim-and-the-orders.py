#!/bin/python3

import sys
from bisect import insort
from collections import defaultdict

def jimOrders(orders):
    sequence = []
    
    for ind, el in enumerate(orders, 1):
        time = sum(el)
        insort(sequence, (time, ind))
    
    #print("seq: {}".format(sequence))
    
    return list(map(lambda x: x[1], sequence))

if __name__ == "__main__":
    n = int(input().strip())
    orders = []
    for orders_i in range(n):
        orders_t = [int(orders_temp) for orders_temp in input().strip().split(' ')]
        orders.append(orders_t)
    result = jimOrders(orders)
    print (" ".join(map(str, result)))


