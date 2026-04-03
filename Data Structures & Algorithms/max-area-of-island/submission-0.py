class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:        
        max_area = 0
        ROWS, COLS = len(grid), len(grid[0])

        def matrixDFS(r: int, c: int) -> None:
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return

            nonlocal curr_area
            curr_area += 1
            grid[r][c] = 0

            matrixDFS(r + 1, c)
            matrixDFS(r - 1, c)
            matrixDFS(r, c + 1)
            matrixDFS(r, c - 1)
            
                
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    curr_area = 0
                    matrixDFS(r, c)
                    max_area = max(max_area, curr_area)
        
        return max_area

        