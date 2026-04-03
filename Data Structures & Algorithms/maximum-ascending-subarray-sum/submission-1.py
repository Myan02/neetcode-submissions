class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # base case, only 1 element
        if len(nums) == 1:
            return nums[0]
        
        res = nums[0]       # keep track of max sum 
        curr_sum = nums[0]  # keep track of max sum per sequence

        for R in range(1, len(nums)):

            # start new sequence
            if nums[R] <= nums[R - 1]:
                curr_sum = 0
            
            curr_sum += nums[R]
            res = max(res, curr_sum)    # update result if larger sequence is found
        
        return res


        