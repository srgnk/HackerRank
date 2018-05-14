"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

def lca(root , v1 , v2):
    vals = sorted([v1, v2])
    v1, v2 = vals[0], vals[1]
    node = root
    while True:
        if v1 < v2 < node.data:
            node = node.left
        if v1 > v2 > node.data:
            node = node.right
        if v1 <= node.data <= v2:
            break
    return node
        
