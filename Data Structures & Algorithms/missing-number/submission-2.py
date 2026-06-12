class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cur = sum(nums)

        max = 0
        for num in range(len(nums) + 1):
            max += num
        
        return max - cur
        