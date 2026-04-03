class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0

        for num in nums_set:
            
            if num - 1 not in nums_set:
                
                curr_total = 1
                while num + curr_total in nums_set:
                    curr_total += 1

                res = max(curr_total, res)    

        return res
                
            
