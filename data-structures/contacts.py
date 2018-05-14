#!/usr/bin/env python3

class Trie:
    def __init__(self):
        self.count = 1
        self.children = {}
        
    def add(self, name):
        node = self
        for let in name:
            if let in node.children.keys():
                node.children[let].count += 1
                node = node.children[let]
            else:
                node.children[let] = Trie()
                node = node.children[let]
    
    def find(self, name):
        node = self
        for let in name:
            if let in node.children.keys():
                res = node.children[let].count
                node = node.children[let]
            else:
                res = 0
                break
                
        return res
    
    def print(self):
        print("count = {} keys = {}".format(self.count, self.children.keys()))
        for key in self.children.keys():
            self.children[key].print()
            
if __name__ == "__main__":
    t = int(input().strip())
    trie = Trie()
    
    for _ in range(t):
        args = input().strip().split()
        
        if args[0] == 'add':
            trie.add(args[1])
        elif args[0] == 'find':
            print(trie.find(args[1]))
            