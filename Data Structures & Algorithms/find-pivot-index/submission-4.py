class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        [1, 7, 3, 6, 5, 6]
        left = [1, 8, 11, 17, 22, 28]
        """

        total = sum(nums)
        left = 0
        n = len(nums)

        for i in range(n):
            right = total - nums[i] - left

            if left == right:
                return i
            
            left += nums[i]
        
        return -1

        
        