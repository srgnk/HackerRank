"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def insert(root, val):
    if root is None:
        root = Node(data=val)
        return root
    
    current = root
    while True:
        if current.data > val:
            if current.left is not None:
                current = current.left
            else:
                current.left = Node(data=val)
                break
        else:
            if current.right is not None:
                current = current.right
            else:
                current.right = Node(data=val)
                break
    
    return root
    
