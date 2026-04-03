class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in diffs:
                return [diffs[compliment], i]
            
            diffs[nums[i]] = i
        