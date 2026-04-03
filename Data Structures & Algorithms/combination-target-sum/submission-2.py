class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.findCombinations(nums, [], [], 0, target)

    
    def findCombinations(self, nums: List[int], subset: List[int], res: List[List[int]], i: int, target: int) -> List[List[int]]:
        # base case, if total == 0, subset found
        if target == 0:
            res.append(subset[:])
            return
        
        # base case, if value goes over or end of the list, backtrack
        if target < 0 or i == len(nums):
            return
        
        subset.append(nums[i])
        self.findCombinations(nums, subset, res, i, target - nums[i])
        subset.pop()
        self.findCombinations(nums, subset, res, i + 1, target)
        return res
        