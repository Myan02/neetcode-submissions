class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.findCombinations(candidates, [], [], 0, target)
    
    def findCombinations(self, nums: List[int], res: List[int], subset: List[int], i: int, target: int) -> List[List[int]]:
        if target == 0:
            res.append(subset[:])
            return
        
        if target < 0 or i == len(nums):
            return
        
        subset.append(nums[i])
        self.findCombinations(nums, res, subset, i + 1, target - nums[i])

        subset.pop()
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1

        self.findCombinations(nums, res, subset, i + 1, target)
        return res
        