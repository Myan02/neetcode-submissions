class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def findSum(cur_sum, res, subset, i):
            if cur_sum == target:
                res.append(subset.copy())
                return

            if i == len(nums) or cur_sum > target:
                return res
            
            cur_sum += nums[i]
            subset.append(nums[i])
            findSum(cur_sum, res, subset, i)

            cur_sum -= nums[i]
            subset.pop()
            findSum(cur_sum, res, subset, i + 1)
            return res


        return findSum(0, [], [], 0)
        