import numpy
dims = [int(x) for x in input().strip().split()]

print(numpy.zeros(tuple(dims), dtype = numpy.int))
print(numpy.ones(tuple(dims), dtype = numpy.int))