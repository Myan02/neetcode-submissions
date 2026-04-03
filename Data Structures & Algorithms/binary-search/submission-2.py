class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def _search(l: int, r: int):
            if l > r:
                return -1
            
            m = (l + r) // 2

            if nums[m] == target:
                return m
            if nums[m] < target:
                return _search(m + 1, r)
            return _search(l, m - 1)
        
        return _search(0, len(nums) - 1)