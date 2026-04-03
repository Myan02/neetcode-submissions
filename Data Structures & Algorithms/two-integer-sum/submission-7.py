class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        res = []

        for i in range(len(nums)):
            val = target - nums[i]

            # answer exists, return indeces
            if val in compliments:
                res = [compliments[val], i]
                break
            
            # add current value in compliments
            compliments[nums[i]] = i
        
        return res
