class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        if obstacleGrid[ROWS - 1][COLS - 1] == 1:
            return 0

        prev = [0] * COLS
        prev[COLS - 1] = 1

        for r in range(ROWS - 1, -1, -1):
            cur = [0] * COLS
            cur[COLS - 1] = 0 if obstacleGrid[r][COLS - 1] == 1 else prev[COLS - 1] 

            for c in range(COLS - 2, -1, -1):
                if obstacleGrid[r][c] == 1:
                    continue
                
                cur[c] = cur[c + 1] + prev[c]
            prev = cur
        
        return prev[0]
        