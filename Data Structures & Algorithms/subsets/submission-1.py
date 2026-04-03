class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        return self.find_subsets(nums, [], [], 0)

    
    
    def find_subsets(self, nums: List[int], res: List[List[int]], subset: List[int], i: int) -> List[List[int]]:
        # base case, if we are at the end of the list
        if i == len(nums):
            res.append(subset[:])
            return
        
        subset.append(nums[i])
        self.find_subsets(nums, res, subset, i + 1)
        subset.pop()
        self.find_subsets(nums, res, subset, i + 1)
        return res
        