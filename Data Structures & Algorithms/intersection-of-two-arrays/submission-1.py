class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums2)
        res = []

        for num in nums1:
            if num in seen:
                seen.remove(num)
                res.append(num)

        return res