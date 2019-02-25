"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
    values_a = []
    values_b = []
    
    node_a = headA
    node_b = headB
    
    while node_a != None:
        values_a.append(node_a.data)
        node_a = node_a.next
  
    while node_b != None:
        values_b.append(node_b.data)
        node_b = node_b.next
    
    res = values_a[-1]
    ind = 1
    while values_a[-ind] == values_b[-ind]:
        ind += 1
    
    res = values_a[-(ind-1)]
    
    return res
    
  
  
  
  
  
  
  
  
  
