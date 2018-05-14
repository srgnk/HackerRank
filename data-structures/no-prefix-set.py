#!/usr/bin/env python3

class Trie:
    def __init__(self):
        self.count = 1
        self.word = 0
        self.children = {}
        
    def add(self, name):
        if self.is_good(name):
            node = self
            for ind, let in enumerate(name):
                if let in node.children.keys():
                    node.children[let].count += 1
                    node = node.children[let]
                else:
                    node.children[let] = Trie()
                    node = node.children[let]
                    
                if ind == len(name)-1:
                    node.word = 1
        else:
            return False
        return True
                
    
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
        print("count = {} word = {} keys = {}".format(self.count, self.word, self.children.keys()))
        for key in self.children.keys():
            self.children[key].print()
            
    def is_good(self, word):
        node = self
        w_len = len(word)
        #if w_len == 1 and word in node.children.keys():
        #    return False
        
        for ind, let in enumerate(word):
            child = node.children.get(let)
            if not child:
                return True
            node = child
            
            #print("let = {} ind = {} w_len-1 = {} node.word = {} node.children = {}".format(let, ind, w_len-1, node.word, node.children))
            if ind == w_len-1 and len(node.children.keys()) > 0:
                #print("word is shorter")
                return False
            if ind <= w_len-1 and node.word == 1:
                #print("word is longer")
                return False
                
        return True
            
if __name__ == "__main__":
    t = int(input().strip())
    trie = Trie()
    passed = 1
    
    for _ in range(t):
        word = input().strip()
        retc = trie.add(word)
        if not retc:
            print("BAD SET")
            print(word)
            passed = 0
            break
        
    if passed:
        print("GOOD SET")