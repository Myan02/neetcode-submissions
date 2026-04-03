class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = []
        suffix = []

        curr = 1
        # set prefix amounts
        for i in range(len(nums)):
            prefix.append(curr)
            curr *= nums[i]
        
        curr = 1
        # set suffix amounts
        for i in range(len(nums) - 1, -1, -1):
            suffix.append(curr)
            curr *= nums[i]
        
        l, r = 0, len(nums) - 1
        while l < len(nums):
            res.append(prefix[l] * suffix[r])
            l += 1
            r -= 1
        
        return res



