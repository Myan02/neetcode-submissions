# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # reverse lists
        def reverseList(head):
            prev = None
            while head:
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp
            return prev
        
        l1 = reverseList(l1)
        l2 = reverseList(l2)

        # add values
        def getValue(head):
            value = ""
            while head:
                value += str(head.val)
                head = head.next
            return value
        
        l1 = int(getValue(l1))
        l2 = int(getValue(l2))

        res_str = str(l1 + l2)
        print(res_str)

        # add each digit to a new linked list
        res = ListNode()
        curr = res
        i = 0
        while i < len(res_str):
            curr.val = int(res_str[i])
            curr.next = None if i == len(res_str) - 1 else ListNode()
            curr = curr.next
            i += 1


        # reverse result
        return reverseList(res)




