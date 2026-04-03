class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        res = 0     # use res to keep track of max consecutive 1s in whole array
        curr = 0    # use curr to keep track of current subsequence of 1s
        
        for num in nums:
            if num:
                curr += 1
                res = max(res, curr)
            else:
                curr = 0
        
        return res

