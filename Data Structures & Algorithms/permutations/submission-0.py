class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        res = []
        subset = []
        combinations = [False] * len(nums)

        def dfs():
            if len(subset) == len(nums):
                res.append(subset[:])
                return 

            for i in range(len(nums)):
                if not combinations[i]:
                    subset.append(nums[i])
                    combinations[i] = True
                    dfs()
                    subset.pop()
                    combinations[i] = False
        
        dfs()
        return res

            

        