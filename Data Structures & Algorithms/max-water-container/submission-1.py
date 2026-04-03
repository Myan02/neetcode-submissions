class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # var to keep track of our maximum area
        max_area = 0

        # two pointers 
        l, r = 0, len(heights) - 1

        while l < r:
            
            # the area is the l x w
            # we get w by finding the distance between the curr indices
            # we get l by finding the smaller of the two heights
            curr_area = (r - l) * min(heights[l], heights[r])

            # keep the larger value
            # either whatever our curr area is a new max or keep the high score
            max_area = max(max_area, curr_area)

            # increments the smaller pointer to have a larger change of finding a larger value
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area