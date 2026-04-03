class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        L = -1

        for R in range(len(nums)):
            if nums[R] == 0:
                L = R

            res = max(res, R - L)
            
        return res
