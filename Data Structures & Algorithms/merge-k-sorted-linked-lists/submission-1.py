# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        res = ListNode()

        for l in lists:
            cur = l
            while cur:
                heapq.heappush(heap, cur.val)
                cur = cur.next

        cur = res
        while heap:
            cur.next = ListNode(heapq.heappop(heap))
            cur = cur.next
        
        return res.next
            
        
        