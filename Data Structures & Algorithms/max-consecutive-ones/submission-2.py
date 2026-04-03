class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        L = -1
        res = 0

        for R in range(len(nums)):
            if nums[R] != 1:
                L = R
            
            res = max(res, R - L)
        
        return res
        