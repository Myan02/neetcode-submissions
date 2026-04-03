class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        next_greatest: dict = {}  # stores each values next greatest element in nums2
        stack: list = []          # holds elements that need a next greatest element
        res: list = []            # resulting array 

        for num in nums2:

            while stack and num > stack[-1]:
                next_greatest[stack.pop()] = num

            stack.append(num)
        
        # sets -1 to all values without a next gretest
        while stack:
            next_greatest[stack.pop()] = -1

        for num in nums1:
            res.append(next_greatest[num])
        
        return res


        