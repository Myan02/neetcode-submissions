class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n + 1)]
        res = []
        subset = []
        
        # run backtracking on nums
        # if size of subset < k, keep adding to subset
        # if size of subset >= k, append subset

        def dfs(i):
            if len(subset) == k:
                res.append(subset[:])
                return

            if i == len(nums):
                return
            
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
