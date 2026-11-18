class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        res = []

        for i, num in enumerate(nums):
            diff = target - num

            if diff in seen.keys():
                return [seen[diff], i]
            
            seen[num] = i
        
        


