#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    database = defaultdict(int)
    frequences = defaultdict(int)
    output = list()

    for q in queries:
        op, val = q

        if op == 1:
            frequences[database[val]] = max(0, frequences[database[val]]-1)
            database[val] += 1
            frequences[database[val]] += 1
        elif op == 2:
            frequences[database[val]] = max(0, frequences[database[val]]-1)
            database[val] = max(0, database[val] - 1)
            frequences[database[val]] += 1
        elif op == 3:
            if frequences[val] > 0:
                output.append(1)
            else:
                output.append(0)
                
        #print("q = {} db = {}".format(q, database))

    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
