class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = 0     # keep track of min sub-arr size
        total = 0   # keep track of sum
        
        L = 0       # left window pointer
        for R in range(len(nums)):  # right window pointer
            total += nums[R]

            # keep checking if lower size arrays work
            while total >= target:
                curr = R - L + 1
                res = curr if res == 0 else min(res, curr)
                total -= nums[L]
                L += 1
        
        return res
        