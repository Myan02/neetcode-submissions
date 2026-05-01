class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        # base case, start is not traversable
        if grid[0][0] == 1:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        min_length = 1
        visit = set()
        q = deque()
        q.append((0, 0))

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return min_length
                
                dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
                for dr, dc in dirs:
                    if  (min(r + dr, c + dc) < 0 or r + dr == ROWS or c + dc == COLS or
                        (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                        continue
                    
                    q.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
                
            min_length += 1
        
        return -1