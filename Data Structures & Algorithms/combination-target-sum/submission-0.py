class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # keep track of a sum
        # if the sum is equal to target, append that subset to our result and return
        # we can keep dfs until the value to add is too big, then we return to the prev
        # if value is less than target, loop through and keep trying to add that value

        res = []
        subset = []

        def dfs(i: int, sum: int):
            if i >= len(nums) or sum > target:
                return 

            if sum == target:
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i, sum + nums[i])
            subset.pop()
            dfs(i + 1, sum)
        
        dfs(0, 0)
        return res

            


        