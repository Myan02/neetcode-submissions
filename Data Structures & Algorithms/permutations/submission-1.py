class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def permDFS(res, subset):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in subset:
                    continue
                
                subset.append(nums[i])
                permDFS(res, subset)
                subset.pop()

            return res
        
        return permDFS([], [])
        


        