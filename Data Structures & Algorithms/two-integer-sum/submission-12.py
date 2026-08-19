class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment_dict = {}

        for i in range(len(nums)):
            cur_dif = target - nums[i]

            if cur_dif in compliment_dict:
                return [compliment_dict[cur_dif], i]

            compliment_dict[nums[i]] = i
        
        return []
        