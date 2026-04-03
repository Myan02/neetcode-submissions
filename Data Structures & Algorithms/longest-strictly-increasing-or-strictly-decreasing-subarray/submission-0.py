class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        L = 0

        for R in range(1, len(nums)):
            if nums[R] <= nums[R - 1]:
                L = R
            
            res = max(res, R - L + 1)
        
        L = 0
        for R in range(1, len(nums)):
            if nums[R] >= nums[R - 1]:
                L = R
            
            res = max(res, R - L + 1)
        
        return res
        

                
            
            

            
        