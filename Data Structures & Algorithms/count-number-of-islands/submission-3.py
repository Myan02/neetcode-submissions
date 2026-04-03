class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])    # row and col length
        seen = set()    # keep track of used island spaces
        res = 0         # total number of islands

        def dfs(row, col):
            # check bounds
            if min(row, col) < 0 or row >= ROWS or col >= COLS:
                return 
            # check if valid cell value and space
            if (row, col) in seen or grid[row][col] == "0":
                return
            
            seen.add((row, col))    # add island space to seen

            # look through the rest of the island and add it to seen
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # iterate through each grid cell oncec
        for row in range(ROWS):
            for col in range(COLS):

                # if cell is a 1: island found
                # if cell is not in seen: new island found
                if grid[row][col] == "1" and (row, col) not in seen:
                    res += 1
                    dfs(row, col)
        
        return res
                    
    
