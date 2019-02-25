"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""

def SortedInsert(head, data):
    if head == None:
        return Node(data=data, next_node=None, prev_node=None)
    
    node = head
    while node.next != None and node.next.data <= data:
        node = node.next
    
    node.next = Node(data=data, next_node=node.next, prev_node=node)
    
    return head
  
  
  
  
  
  
  
  
  
  
