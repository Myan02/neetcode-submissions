class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greatest = {}
        stack = []
        res = []

        for num in nums2:
            while stack and num > stack[-1]:
                next_greatest[stack.pop()] = num

            stack.append(num)
        
        while stack:
            next_greatest[stack.pop()] = -1

        for num in nums1:
            res.append(next_greatest[num])
        
        return res


        