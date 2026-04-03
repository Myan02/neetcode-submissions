import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = nums
        heapq.heapify(minHeap)
        res = 0
        for _ in range(len(nums) - k + 1):
            res = heapq.heappop(minHeap)
        
        return res

        