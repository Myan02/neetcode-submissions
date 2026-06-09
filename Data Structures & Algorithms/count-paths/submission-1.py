class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # syntactic sugar, easier to refer to these vars
        rows = m
        cols = n

        prev = [0] * cols   # create a temporary n + 1 row of 0s

        # we loop over every row and fill them up
        for i in range(rows - 1, -1, -1):
            cur = [0] * cols
            cur[cols - 1] = 1   

            for c in range(cols - 2, -1, -1):
                cur[c] = cur[c + 1] + prev[c]
            
            prev = cur
        
        return prev[0]
        