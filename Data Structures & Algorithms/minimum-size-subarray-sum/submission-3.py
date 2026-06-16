class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float("inf")
        cur_total = 0
        L = 0

        for R in range(len(nums)):
            cur_total += nums[R]

            while cur_total >= target:
                min_length = min(min_length, R - L + 1)
                cur_total -= nums[L]
                L += 1
        
        return 0 if min_length == float("inf") else int(min_length)
        