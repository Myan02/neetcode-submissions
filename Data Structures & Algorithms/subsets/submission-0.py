class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(i, nums, subset, res):
            if i == len(nums):
                res.append(subset.copy())
                return res

            subset.append(nums[i])
            dfs(i + 1, nums, subset, res)
            subset.pop()
            dfs(i + 1, nums, subset, res)
            return res
        
        
        return dfs(0, nums, [], [])
        

        