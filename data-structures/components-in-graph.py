#!/usr/bin/env python3

import sys

class disjoint_set:
    class Node:
        def __init__(self, data = 0):
            self.data = data
            self.parent = self
            self.rank = 0

    def __init__(self):
        self.items = dict()

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
                node2.parent = node1
            else:
                node1.parent = node2

        return True

if __name__ == "__main__":
    n = int(input().strip())
    output = [0] * (n+1)
    
    dset = disjoint_set()
    
    for _ in range(n):
        rep1, rep2 = [int(x) for x in input().strip().split()]
        
        dset.make_set(rep1)
        dset.make_set(rep2)
        
        dset.union(rep1, rep2)
        
    for el in dset.items.keys():
        output[dset.find_set(el).data] += 1
        
    dset_max = max(output)
    dset_min = min(filter(lambda x: x > 0, output))
    
    print("{} {}".format(dset_min, dset_max))
        