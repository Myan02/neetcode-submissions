# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        res = ListNode()     # this is the reference to return 
        dummy = res
        while list1 and list2:
            next_1 = list1.next
            next_2 = list2.next

            if list1.val <= list2.val:
                dummy.next = list1
                list1 = next_1
            else:
                dummy.next = list2
                list2 = next_2

            dummy = dummy.next
        
        if list1:
            dummy.next = list1

        if list2:
            dummy.next = list2

        return res.next
        
