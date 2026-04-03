class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        max_area = 0

        while l < r:
            # process left end as left pointer is the lower bound
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                max_area += max_l - height[l]
            
            # process right end as right pointer is the lower bound
            else:
                r -= 1
                max_r = max(max_r, height[r])
                max_area += max_r - height[r]
        
        return max_area

