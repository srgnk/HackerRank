#!/usr/bin/env python3

import sys 

class Node():
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
        
def find_node_recursive(root, data):
    if root is not None:
        res = None
        if root.data == data:
            res = root
        if res == None:
            res = find_node(root.left, data)
        if res == None:
            res = find_node(root.right, data)
        return res

def find_node(root, data):
    current = root 
    s = []
    done = 0
     
    while(not done):
        if current is not None:
            s.append(current)
            current = current.left 
        else:
            if(len(s) > 0):
                current = s.pop()
                if current.data == data:
                    return current
         
                current = current.right 
            else:
                done = 1
    return None

def height(root):
    if root is not None:
        return max(1 + height(root.left), 1 + height(root.right))
    else:
        return 0
    
def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print("{} ".format(root.data), end='')
        inOrder(root.right)
        
def swap_level(root, level):
    if root is not None:
        if level == 1:
            root = swap_subtrees(root)
        else:
            swap_level(root.left, level - 1)
            swap_level(root.right, level - 1)
            
def swap_subtrees(node):
    node.left, node.right = node.right, node.left
    return node
            
if __name__ == "__main__":
    sys.setrecursionlimit(15000)
    root = Node(data = 1)
    node = root
    n = int(input().strip())

    for ind in range(1, n+1):
        a, b = map(int,input().split(' '))
        #inOrder(root)
        #print()
        #print("ind = {} a = {} b = {}".format(ind, a, b))
        
        node = find_node(root, ind)
        
        if a != -1:
            node.left = Node(data = a)
        if b != -1:
            node.right = Node(data = b)
            
    t = int(input().strip())
    for ind in range(t):
        k = int(input().strip())
        #print("k = {}".format(k))
        
        for level in range(k, height(root)+1, k):
            swap_level(root, level)
        inOrder(root)
        print()
            
