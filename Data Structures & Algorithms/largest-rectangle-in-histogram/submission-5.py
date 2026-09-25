class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
            go through each index and expand left and right
                - stop at out of bounds
                - stop if height is < cur value
                - store that value somewhere
            if we see a 1, automatically set it to the len of the array


        """

        stack = []
        res = 0

        for i, height in enumerate(heights):
            if not stack:
                stack.append([i, height])
                continue
            
            if stack[-1][1] == height:
                continue
            
            if stack[-1][1] < height:
                stack.append([i, height])
                continue

            while stack and stack[-1][1] > height:
                prev_idx, prev_height = stack.pop()

                res = max(res, (i - prev_idx) * prev_height)

            stack.append([prev_idx, height])

        while stack:
            cur_idx, cur_height = stack.pop()
            res = max(res, (len(heights) - cur_idx) * cur_height)            


        return res

                


                
