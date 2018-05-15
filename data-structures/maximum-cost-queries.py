#!/bin/python3

import os
import sys
from bisect import bisect_right, bisect_left

class disjoint_set:
    class Node:
        def __init__(self, data = 0):
            self.data = data
            self.parent = self
            self.rank = 0
            self.size = 1

    def __init__(self):
        self.items = dict()
        self.ans = 0

    def make_set(self, data):
        if not data in self.items:
            self.items[data] = self.Node(data)
        return self.items

    def find_set(self, data):
        if data in self.items:
            node = self.items[data]
        else:
            return False

        if node.parent == node:
            return node
        node.parent = self.find_set(node.parent.data)

        return node.parent

    def union(self, rep1, rep2):
        node1 = self.find_set(rep1)
        node2 = self.find_set(rep2)

        #print("union: node1 = {} node2 = {}".format(node1.data, node2.data))

        if node1 and node2 and node1 != node2:
            if node1.rank >= node2.rank:
                if node1.rank == node2.rank:
                    node1.rank += 1

                self.ans -= (node1.size*(node1.size - 1))//2 + (node2.size*(node2.size - 1))//2
                node2.parent = node1
                node1.size += node2.size
                self.ans += (node1.size*(node1.size - 1))//2
            else:
                self.ans -= (node1.size*(node1.size - 1))//2 + (node2.size*(node2.size - 1))//2
                node1.parent = node2
                node2.size += node1.size
                self.ans += (node2.size*(node2.size - 1))//2

        return True

    def get_size(self, rep):
        return self.find_set(rep).size

    def get_ans(self):
        return self.ans

# Complete the solve function below.
def solve(tree, queries):
    dset = disjoint_set()
    tree = sorted(tree, key=lambda x: x[2])
    weights = list(map(lambda x: x[2], tree))
    anses = []

    for el in tree:
        dset.make_set(el[0])
        dset.make_set(el[1])
        dset.union(el[0], el[1])

        anses.append(dset.get_ans())
        print("adding {} ans = {}".format(el, dset.get_ans()))

    print("weights: {} anses: {}".format(weights, anses))
    # do queries
    output = []
    for q in queries:
        qleft, qright = q[0], q[1]

        if qright < weights[0]:
            output.append(0)
        else:
            right = bisect_right(weights, qright) - 1
            print("query: {} RIGHT weights[{}] = {}".format(q, right, weights[right]))

            if qleft <= weights[0]:
                output.append(anses[right])
            else:
                left = bisect_left(weights, qleft) - 1
                print("query: {} LEFT weights[{}] = {}".format(q, left, weights[left]))
                output.append(anses[right] - anses[left])


    return output

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()
    n = int(nq[0])
    q = int(nq[1])
    tree = []

    for _ in range(n-1):
        tree.append(list(map(int, input().rstrip().split())))

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = solve(tree, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

