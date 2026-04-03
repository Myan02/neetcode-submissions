class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        def dfs(i, curr_target, nums, subset, res):
            if i == len(nums) or curr_target < 0:
                return

            if curr_target == 0:
                res.append(subset.copy())
                return 
            
            
            subset.append(nums[i])
            dfs(i, curr_target - nums[i], nums, subset, res)
            subset.pop()
            dfs(i + 1, curr_target, nums, subset, res)
            return res
            
        
        return dfs(0, target, nums, [], [])
        

        