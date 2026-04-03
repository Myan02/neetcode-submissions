class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in sums:
                return [sums[diff], i]
            
            sums[num] = i
        return []


        
            