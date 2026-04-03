class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        largest_area = 0

        while l < r:
            curr_area = (r - l) * min(heights[l], heights[r])
            largest_area = max(largest_area, curr_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return largest_area


        