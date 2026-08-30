class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        res = 0

        for num in nums:
            if num - 1 not in nums:
                cur = 1
                cur_num = num + 1

                while cur_num in nums:
                    cur_num += 1
                    cur += 1
                
                res = max(res, cur)
        
        return res
                    