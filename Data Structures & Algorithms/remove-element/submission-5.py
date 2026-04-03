class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not len(nums):
            return 0
        
        L = 0
        R = len(nums) - 1

        while L < R:
            if nums[L] == val:
                while R >= L and nums[R] == val:
                    R -= 1
                
                nums[L], nums[R] = nums[R], nums[L]
                R -= 1
            
            L += 1
        
        return L + 1
        