class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        target = (ROWS - 1, COLS - 1)
        
        def dfs(r: int, c: int, visited: set()) -> int:
            # base case, bad choice
            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visited:
                return 0
            
            if (r, c) == target:
                return 1
            
            visited.add((r, c))

            count = 0
            count += dfs(r + 1, c, visited)
            count += dfs(r, c + 1, visited)

            visited.remove((r, c))
            return count
        
        return dfs(0, 0, set())
        