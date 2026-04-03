class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()   # sort to make it possible to skip same values

        def dfs(i, sum):
            # soln found
            if sum == target:
                res.append(subset.copy())
                return

            # either false soln or end of array
            if i == len(candidates) or sum > target:
                return
            
            # run dfs with nums[i]
            subset.append(candidates[i])
            dfs(i + 1, sum + candidates[i])

            # next iteration, skip values that are the same to remove non unique values
            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, sum)
        
        dfs(0, 0)
        return res
        