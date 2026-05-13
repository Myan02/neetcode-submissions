class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}

        for i in range(len(nums)):
            curr_compliment = target - nums[i]

            if curr_compliment in compliments:
                return [compliments[curr_compliment], i]
            
            compliments[nums[i]] = i
        