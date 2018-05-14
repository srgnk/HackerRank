import numpy

n, m = [int(x) for x in input().strip().split()]

print(numpy.eye(n, m))