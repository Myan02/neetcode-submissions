class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for L in range(len(nums)):
            for R in range(L + 1, len(nums)):
                if nums[L] == nums[R]:
                    return nums[L]
        
    