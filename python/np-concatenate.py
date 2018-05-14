import numpy
n, m, p = [int(x) for x in input().strip().split()] 
arr1 = []
arr2 = []

for _ in range(n):
    arr1.append([int(x) for x in input().strip().split()] )
    
for _ in range(m):
    arr2.append([int(x) for x in input().strip().split()] )
    
arr1 = numpy.array(arr1)
arr2 = numpy.array(arr2)

print(numpy.concatenate((arr1, arr2)))