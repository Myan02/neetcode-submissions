# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        tail = ListNode()
        res = 0

        head_cur = head
        tail_cur = tail
        while head_cur:
            node = ListNode(head_cur.val)
            tail_cur.next = node

            head_cur = head_cur.next
            tail_cur = tail_cur.next
        
        tail = tail.next

        prev = None
        next_ptr = tail
        while next_ptr:
            next_ptr = tail.next
            tail.next = prev
            prev = tail
            tail = next_ptr
        
        tail = prev
        
        while head:
            res = max(res, head.val + tail.val)
            head = head.next
            tail = tail.next
        
        return res
