# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # set two pointers, dummy points to head, right is at head
        dummy = ListNode(val=0, next=head)
        left, right = dummy, head

        # move right n steps
        for _ in range(n):
            right = right.next
        
        # move both pointers until right reaches end
        while right:
            right = right.next
            left = left.next

        # delete nth node
        left.next = left.next.next
        return dummy.next


        