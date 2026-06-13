# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper:
    def __init__(self, node) -> None:
        self.node = node
    
    def __lt__(self, other) -> bool:
        return self.node.val < other.node.val
    
    def __str__(self) -> str:
        return f"{self.node.val}"

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        res = ListNode()
        cur = res
        minHeap = []

        for l in lists:
            if l:
                heapq.heappush(minHeap, NodeWrapper(l))
                
        while minHeap:
            lst = heapq.heappop(minHeap)
            cur.next = lst.node
            cur = cur.next

            if lst.node.next:
                heapq.heappush(minHeap, NodeWrapper(lst.node.next))
        
        return res.next
        
        

        