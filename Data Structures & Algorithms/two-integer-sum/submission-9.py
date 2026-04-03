class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res: int = 0
        sums: dict = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in sums.keys():
                return [sums[complement], i]

            sums[num] = i
        
        return []

