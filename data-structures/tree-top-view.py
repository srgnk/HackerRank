"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def _topLeft(root):
    if root is not None:
        _topLeft(root.left)
        print root.data,

def _topRight(root):
    if root is not None:
        print root.data,
        _topRight(root.right)

def topView(root):
    _topLeft(root.left)
    print root.data,
    _topRight(root.right)
        
