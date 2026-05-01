class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_set = set()
        fresh = 0

        ROWS, COLS = len(grid), len(grid[0])

        q = deque()
        time = 0

        # calculate number of fresh fruit
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1

                elif grid[r][c] == 2:
                    q.append((r, c))
                    rotten_set.add((r, c))
        
        if not fresh:
            return 0
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in dirs:
                    if  (min(r + dr, c + dc) < 0 or r + dr == ROWS or c + dc == COLS or
                        (r + dr, c + dc) in rotten_set or grid[r + dr][c + dc] != 1):
                        continue        

                    rotten_set.add((r + dr, c + dc))
                    q.append((r + dr, c + dc))
                    fresh -= 1
            
            time += 1 if q else 0
            
        
        return time if not fresh else -1
                
