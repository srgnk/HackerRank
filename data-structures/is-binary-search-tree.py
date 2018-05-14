""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def inOrder(root):
    if root is not None:
        out = []
        out += inOrder(root.left)
        out.append(root.data)
        #print(root.data, end=' ')
        out += inOrder(root.right)
        return out
    else:
        return [] 
        
def check_binary_search_tree_(root):
    get_ordered = inOrder(root)
    return get_ordered == sorted(list(set(get_ordered)))

    