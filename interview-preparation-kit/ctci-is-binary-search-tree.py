""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkNode(node, min, max):
    if node == None:
        return True
    if node.data <= min or node.data >= max:
        return False
    return checkNode(node.left, min, node.data) and checkNode(node.right, node.data, max)

def checkBST(root):
    return checkNode(root, float('-inf'), float('inf'))
    