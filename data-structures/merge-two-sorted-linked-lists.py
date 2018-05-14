"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Insert(head, data):
    node = head
    if head is None:
        head = Node(data)
        return head
    
    while node.next is not None:
        node = node.next
    
    node.next = Node(data)
    
    return head

def MergeLists(headA, headB):
    list_out = Node()
    node_a = headA
    node_b = headB
    
    while node_a and node_b:
        if node_a.data < node_b.data:
            list_out = Insert(list_out, node_a.data)
            node_a = node_a.next
        else:
            list_out = Insert(list_out, node_b.data)
            node_b = node_b.next
    
    last_node = list_out
    while last_node.next is not None:
        last_node = last_node.next
    
    if node_a:
        last_node.next = node_a
    elif node_b:
        last_node.next = node_b
        
    return list_out.next
        
  
  
  
  
  
  
  
  
  
  
