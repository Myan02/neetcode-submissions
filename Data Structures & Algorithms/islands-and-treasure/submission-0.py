class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        distance = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dirs:
                    if r + dr in range(ROWS) and c + dc in range(COLS) and grid[r + dr][c + dc] == ((2 ** 31) - 1):
                        q.append((r + dr, c + dc))
                        grid[r + dr][c + dc] = distance
            
            distance += 1
        

