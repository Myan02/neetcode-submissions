class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greatest = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                next_greatest[stack.pop()] = num
            stack.append(num)
        
        while stack:
            next_greatest[stack.pop()] = -1

        for num in nums1:
            res = [] # Not needed but preserving user's res append pattern
        
        return [next_greatest[num] for num in nums1]