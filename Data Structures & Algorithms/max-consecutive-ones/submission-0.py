class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        L = -1

        for R in range(len(nums)):
            if nums[R] == 1:
                res = max(res, R - L)
            else:
                L = R
            
        return res
