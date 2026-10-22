class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L < R:
            mid = (L + R) // 2

            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid
        
        L1, R1, L2, R2 = 0, L - 1, L, len(nums) - 1

        left_res = self.binarySearch(nums, L1, R1, target)
        right_res = self.binarySearch(nums, L2, R2, target)

        return left_res if right_res == -1 else right_res

    def binarySearch(self, nums, l, r, target):
        while l <= r:
            mid = (l + r) // 2

            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        
        return -1
