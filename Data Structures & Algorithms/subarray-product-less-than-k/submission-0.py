class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0
        product = 1

        # start sliding window
        for r in range(len(nums)):
            product *= nums[r]
            
            # product exceeds k, reduce window
            while l <= r and product >= k:
                product //= nums[l]
                l += 1
            
            res += (r - l + 1)
        return res
        