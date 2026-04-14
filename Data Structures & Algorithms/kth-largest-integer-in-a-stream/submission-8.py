class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = []
        for i in range(len(nums)):
            heapq.heappush(self.stream, nums[i])

            if len(self.stream) > k:
                heapq.heappop(self.stream)

        self.k = k
        print(self.stream)


    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val)
        len(self.stream) > self.k and heapq.heappop(self.stream)
        
        return self.stream[0]

        






        

        
