import numpy
n, m = [int(x) for x in input().strip().split()]
arr = []
for _ in range(n):
    arr.append([int(x) for x in input().strip().split()])
print(numpy.array(arr).transpose())
print(numpy.array(arr).flatten())