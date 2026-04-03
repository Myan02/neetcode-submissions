# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def reverseList(head):
            prev = None
            while head:
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp
            return prev
        
        # reverse list
        head = reverseList(head)
        
        # remove nth node
        if n == 1:
            head = head.next
        else:
            curr = head
            while n > 2:
                curr = curr.next
                n -= 1
            curr.next = curr.next.next
        
        # reverse list again
        return reverseList(head)

        