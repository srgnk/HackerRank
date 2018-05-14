#Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):
    node = head
    list_len = 0
    
    while node != None:
        node = node.next
        list_len += 1
        
    node = head
    for _ in range(list_len - position - 1):
        node = node.next
    
    return node.data
  
  
  
  
  
  
  
  
  
