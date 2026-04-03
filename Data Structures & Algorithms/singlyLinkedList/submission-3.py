class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        # keep track of the current node and index
        curr = self.head.next
        i = 0

        # as long as curr node exists, keep iterating
        while curr:
            if index == i:
                return curr.value

            # if indeces do not match, iterate to the next node
            curr = curr.next
            i += 1
        
        # if we exit the loop, then we looked through the whole list and failed
        return -1

    def insertHead(self, val: int) -> None:
        # create new node
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node

        # if linked list was empty
        if self.tail == self.head:
            self.tail = new_node
        
    def insertTail(self, val: int) -> None:
        # create new node
        new_node = Node(val)

        # it doesn't matter if the new node points to a DIFFERENT null
        # new_node.next = self.tail.next

        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        # find the node at the index - 1
        curr = self.head
        i = 0

        while curr and i < index:
            curr = curr.next
            i += 1
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
    
        return False
        

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        
        while curr:
            res.append(curr.value)
            curr = curr.next
        
        return res
        
