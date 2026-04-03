class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            M = (R + L) // 2

            if target < nums[M]:
                R = M - 1
            elif target > nums[M]:
                L = M + 1
            else:
                return M
                
        return L