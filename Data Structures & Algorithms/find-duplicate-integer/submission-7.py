class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            index = abs(nums[i]) # check if nums[i] has been seen yet

            if nums[index] < 0:
                return abs(nums[i])
            
            nums[index] *= -1
            print(nums)
    