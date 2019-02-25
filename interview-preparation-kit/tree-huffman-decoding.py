"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def is_leaf(root):
    if root.right == None and root.left == None:
        return True
    else:
        return False
    
def decodeHuff(root , s):
    node = root
    output = ''
    for dig in s:
        #print "dig = {} node.freq = {}".format(dig, node.freq)
        if dig == '0':
            if is_leaf(node.left):
                output += node.left.data
                node = root
            else:
                node = node.left
        else:
            if is_leaf(node.right):
                output += node.right.data
                node = root
            else:
                node = node.right
    
    print output
        
        
