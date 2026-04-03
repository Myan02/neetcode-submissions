class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the threshold, L == M and nums[L] > nums[R]
        # run binary search on whichever side contains the target

        def binarySearch(l: int, r: int) -> int:
            while l <= r:
                m = (l + r) // 2

                if target > nums[m]:
                    l = m + 1
                elif target < nums[m]:
                    r = m - 1
                else:
                    return m
            
            return -1

        l, r = 0, len(nums) - 1
        
        # base case, nums hasn't been shifted
        if nums[l] < nums[r]:
            return binarySearch(l, r)
        
        pivot = 0

        # finding the threshold
        while l < r:
            m = (l + r) // 2

            # threshold is to the right of m
            if nums[m] > nums[l]:
                l = m
            
            # threshold is to the left of m
            elif nums[m] < nums[l]:
                r = m
            
            # threshold has been found
            else:
                pivot = m   # max value in nums
                break
        
        l, r = 0, len(nums) - 1
        if nums[l] <= target <= nums[pivot]:
            return binarySearch(l, pivot)
        return binarySearch(pivot + 1, r)
        

        