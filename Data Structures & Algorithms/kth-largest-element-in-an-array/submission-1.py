class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [(-num, num) for num in nums]
        heapq.heapify(nums)

        res = tuple()
        while k:
            res = heapq.heappop(nums)
            k -= 1
        
        return res[1]
            
        