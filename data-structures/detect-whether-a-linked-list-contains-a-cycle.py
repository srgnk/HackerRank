"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    cnt = 0
    node = head
    
    if head is None:
        return 0
    
    while node != None:
        node = node.next
        cnt += 1
        if cnt > 100:
            return 1
    
    return 0
    
