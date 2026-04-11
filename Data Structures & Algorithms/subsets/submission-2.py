class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def findSubsets(res, subset, i):
            if i == len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            findSubsets(res, subset, i + 1)
            subset.pop()
            findSubsets(res, subset, i + 1)
            return res
        
        return findSubsets([], [], 0)
        