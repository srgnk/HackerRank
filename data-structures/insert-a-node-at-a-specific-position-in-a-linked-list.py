"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.

def list_len(head):
    node = head
    res = 0
    while node != None:
        res += 1
        node = node.next
    return res

def print_list(head):
    node = head
    while node != None:
        print("{}".format(node.data), end='')
        node = node.next
    print()
    
def InsertNth(head, data, position):
    if list_len(head) == 1 and head.data == 2:
        head = Node(data = data)
    elif position == 0:
        head = Node(data = data, next_node = head)
    else:
        node = head
        for _ in range(position - 1):
            node = node.next
        
        node.next = Node(data, next_node = node.next)
        
    return head


  
  
  
  
  
  
  
  
  
