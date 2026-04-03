class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # left and right window pointers
        L = 0
        window = set()  # keep track of current window
        for R in range(len(nums)):
            
            # check if there is a duplicate O(1) loopup
            if nums[R] in window:
                return True

            # always add newest value to window
            window.add(nums[R])

            # when out of window bounds, remove the oldest value and shift window 
            if (R - L) == k:
                window.remove(nums[L])
                L += 1
        
        return False