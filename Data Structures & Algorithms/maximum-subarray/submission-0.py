class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_count = nums[0]
        curr_count = 0

        for num in nums:
            curr_count = max(curr_count, 0) + num
            max_count = max(curr_count, max_count)
        
        return max_count