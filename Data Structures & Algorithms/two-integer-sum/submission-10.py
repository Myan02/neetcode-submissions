class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in compliment:
                return [compliment[diff], i]
            
            compliment[num] = i

        return []
        