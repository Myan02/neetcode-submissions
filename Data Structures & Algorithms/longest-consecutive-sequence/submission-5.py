class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res = 0

        for num in nums_set:
            
            curr_total = 0
            if num - 1 not in nums_set:
                
               curr_total = 1
               res = max(res, curr_total)

               curr_val = num
               nums.remove(num)

               while curr_val + 1 in nums_set:
                    curr_total += 1
                    res = max(res, curr_total)

                    curr_val += 1
        
        return res
                
            
