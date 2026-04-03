class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = 0
        total = 0
        L = 0

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                curr = R - L + 1
                res = curr if res == 0 else min(res, curr)
                total -= nums[L]
                L += 1
        
        return res
        