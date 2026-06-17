class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        [1, 1, 2, 8]
        [1, 6, 24, 48]
        [48, 24, 12, 8]
        """

        res = []
        left = [1]
        right = [1]

        total = 1
        for i in range(len(nums) - 1):
            total *= nums[i]
            left.append(total)

        total = 1
        for i in range(len(nums) - 1, 0, -1):
            total *= nums[i]
            right.append(total)

        for i in range(len(nums)):
            cur = left[i] * right[len(nums) - i - 1]
            res.append(cur)
        
        return res





