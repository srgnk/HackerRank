"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""

def height(root):
    if root is not None:
        return max(1 + height(root.left), 1 + height(root.right))
    else:
        return -1

def _levelOrder(root, level):
    if root is not None:
        if level == 0:
            print root.data,
        else:
            _levelOrder(root.left, level - 1)
            _levelOrder(root.right, level - 1)
        

def levelOrder(root):
    for level in range(height(root)+1):
        _levelOrder(root, level)
        
