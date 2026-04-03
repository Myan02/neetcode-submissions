class MinHeap:
    
    def __init__(self):
        self.heap = [-1]
        

    def push(self, val: int) -> None:
        # If heap is empty, push value to the heap
        # if heap is not empty, push value to the heap and percolate that value up
        self.heap.append(val)

        curr = len(self.heap) - 1
        parent = curr // 2
        while parent:
            if self.heap[curr] < self.heap[parent]:
                # swap parent and child
                self.heap[curr], self.heap[parent] = self.heap[parent], self.heap[curr]
            
            curr = parent
            parent = curr // 2
    
    def percolateDown(self, curr: int) -> None:
        while curr * 2 < len(self.heap):
            # both children
            if (curr * 2 + 1 < len(self.heap) and
            self.heap[curr * 2 + 1] < self.heap[curr * 2] and
            self.heap[curr] > self.heap[curr * 2 + 1]):
                self.heap[curr], self.heap[curr * 2 + 1] = self.heap[curr * 2 + 1], self.heap[curr]
                curr = curr * 2 + 1

            # left child
            elif self.heap[curr] > self.heap[curr * 2]:
                self.heap[curr], self.heap[curr * 2] = self.heap[curr * 2], self.heap[curr]
                curr = curr * 2

            # no child
            else:
                break
            

    def pop(self) -> int:
        # empty heap
        if len(self.heap) <= 1:
            return -1
        
        # heap with 1 element
        if len(self.heap) <= 2:
            return self.heap.pop()
        
        # set min value to return and set last value as root
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        
        curr = 1
        self.percolateDown(curr)

        return res
        

    def top(self) -> int:
        if len(self.heap) == 1:
            return -1
        return self.heap[1]
        

    def heapify(self, nums: List[int]) -> None:
        # initialize heap by appending first value to the end
        if not nums:
            return
        nums.append(nums[0])
        self.heap = nums
        curr = (len(self.heap) - 1) // 2     # first node with a child

        # traverse each value from the end and percolate up 
        while curr:
            self.percolateDown(curr)
            curr -= 1
        






        
        