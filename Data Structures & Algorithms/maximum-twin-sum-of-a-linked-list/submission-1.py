# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = 0

        fast, slow, tmp = head, head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next

            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        List1 = prev
        List2 = slow

        while List1:
            res = max(res, List1.val + List2.val)
            List1 = List1.next
            List2 = List2.next
        
        return res

            
