class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
    
        def matrixDFS(r: int, c: int, visit: Set[tuple]) -> int:
            ROWS, COLS = len(grid), len(grid[0])

            # base cases
            if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == 1:
                return 0
            if (r == ROWS - 1) and (c == COLS - 1):
                return 1
            
            # not a base case, continue
            visit.add((r, c))

            # traverse each direction
            count = 0
            count += matrixDFS(r + 1, c, visit)
            count += matrixDFS(r - 1, c, visit)
            count += matrixDFS(r, c + 1, visit)
            count += matrixDFS(r, c - 1, visit)

            # either dead end or backtracking
            visit.remove((r, c))
            return count
        
        visitSet = set()
        result = matrixDFS(0, 0, visitSet)
        return result


        