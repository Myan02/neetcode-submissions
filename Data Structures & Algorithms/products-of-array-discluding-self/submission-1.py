class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1]
        total = 1
        res = []

        for i in range(len(nums) - 1):
            total *= nums[i]
            prefix.append(total)
        
        total = 1
        for i in range(len(nums) - 1, 0, -1):
            total *= nums[i]
            postfix.append(total)
        
        print(prefix)
        print(postfix)

        left, right = 0, len(nums) - 1
        while left < len(nums):
            res.append(prefix[left] * postfix[right])
            left += 1
            right -= 1
        
        return res

        

        