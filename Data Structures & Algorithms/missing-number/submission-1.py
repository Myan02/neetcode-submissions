class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        pocket = set(nums)

        for i in range(len(nums)):
            if i not in pocket:
                return i
        
        return len(nums)