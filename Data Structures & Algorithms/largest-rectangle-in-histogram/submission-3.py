class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_height = 0

        for index, height in enumerate(heights):
            if not stack:
                stack.append([index, height])
                continue
            
            # if height is same as prev
            if stack[-1][1] == height:
                continue
            
            # if height is taller than prev
            if stack[-1][1] < height:
                stack.append([index, height])
                continue
            
            # while height is shorter than prev
            while stack and stack[-1][1] > height:
                prev = stack.pop()
                max_height = max(max_height, (index - prev[0]) * prev[1])
            
            stack.append([prev[0], height])
            


        while stack:
            curr_bar = stack.pop()
            max_height = max(max_height, (len(heights) - curr_bar[0]) * curr_bar[1])
        
        return max_height