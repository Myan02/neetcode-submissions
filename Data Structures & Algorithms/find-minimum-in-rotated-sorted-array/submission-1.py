class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        if nums[l] <= nums[r]:
            return nums[0]
        
        while l < r:
            m = (l + r) // 2

            if nums[l] < nums[m]:
                l = m
            elif nums[m] < nums[r]:
                r = m
            else:
                return nums[r]


            
        
        
        