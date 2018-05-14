#!/usr/bin/env python3

import sys

class disjoint_set:
    class Node:
        def __init__(self, data = 0):
            self.data = data
            self.parent = self
            self.rank = 0
            self.size = 1

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
                node1.size += node2.size
            else:
                node1.parent = node2
                node2.size += node1.size

        return True
    
    def get_size(self, rep):
        return self.find_set(rep).size


if __name__ == "__main__":
    n, q = [int(x) for x in input().strip().split()]
    dset = disjoint_set()
    
    for ind in range(1, n+1):
        dset.make_set(ind)
    
    for _ in range(q):
        query = input().strip().split()
        
        if query[0] == 'M':
            rep1 = int(query[1])
            rep2 = int(query[2])
            dset.union(rep1, rep2)
        elif query[0] == 'Q':
            rep = int(query[1])
            print(dset.get_size(rep))
            