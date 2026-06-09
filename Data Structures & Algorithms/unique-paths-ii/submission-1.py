class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        def dfs(r, c, cache):
            if r == rows or c == cols or obstacleGrid[r][c] == 1:
                return 0
            
            if cache[r][c]:
                return cache[r][c]
            
            if r == rows - 1 and c == cols - 1:
                return 1
            
            cache[r][c] = (dfs(r + 1, c, cache) + 
                    dfs(r, c + 1, cache))
            return cache[r][c]
        
        return dfs(0, 0, [[0] * cols for _ in range(rows)])
        