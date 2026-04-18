class Solution:
    def jump(self, nums: List[int]) -> int:
        L = R = 0
        res = 0

        while R < len(nums) - 1:

            max_val = nums[L]
            for i in range(L, R + 1):
                max_val = max(max_val, nums[i])
            
            L = R + 1
            R += max_val

            res += 1
        
        return res





        

        