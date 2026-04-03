class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = r = 1
        unique = 1

        while r < len(nums):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                unique += 1
                r += 1
                l += 1
            else:
                r += 1
        
        return unique
        
        