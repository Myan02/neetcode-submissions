"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # linked list is empty
        if not head:
            return None

        copy = {None: None}

        # set hash map with new nodes
        curr = head
        while curr:
            new = Node(curr.val)
            copy[curr] = new
            curr = curr.next
        
        # set new node pointers using old list
        curr = head
        while curr:
            copy_node = copy[curr]
            copy_node.next = copy[curr.next]
            copy_node.random = copy[curr.random]
            curr = curr.next

            
        return copy[head]
            
            