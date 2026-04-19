class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = 0
        fresh = 0

        queue = deque()

        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                
                if grid[r][c] == 2:
                    rotten += 1
                    queue.append((r, c))
        
        if not fresh:
            return 0
        
        total = rotten + fresh
        minutes = 0
        while queue:
            num_cur_rotten = len(queue)

            for i in range(num_cur_rotten):
                r, c = queue.popleft()

                direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in direction:
                    if (r + dr < 0 or c + dc < 0 or
                        r + dr == ROWS or
                        c + dc == COLS or
                        grid[r + dr][c + dc] != 1):
                        continue
                    grid[r + dr][c + dc] = 2
                    fresh -= 1
                    queue.append((r + dr, c + dc))
            
            minutes += 1 if queue else 0
        
        return minutes if not fresh else -1






