# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for i, linked_list in enumerate(lists):
            head = linked_list

            while head:
                heapq.heappush(min_heap, [head.val, id(head), head])
                head = head.next
        
        dummy = ListNode(0)
        curr = dummy
        while min_heap:
            node = heapq.heappop(min_heap)[2]
            curr.next = node
            curr = curr.next
        
        curr.next = None
        return dummy.next