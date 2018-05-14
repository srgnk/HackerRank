import numpy

n, m = [int(x) for x in input().strip().split()]

a = numpy.array([[int(x) for x in input().strip().split()] for _ in range(n)])
b = numpy.array([[int(x) for x in input().strip().split()] for _ in range(n)])

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a**b)