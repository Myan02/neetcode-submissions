class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        # y = target - x
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in cache:
                return [cache[compliment], i]
            
            cache[num] = i
        
        return []

            

        