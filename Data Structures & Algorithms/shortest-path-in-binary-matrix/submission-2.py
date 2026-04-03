class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] or grid[ROWS - 1][COLS - 1]:
            return -1
        visit = set()
        visit.add((0, 0))
        q = deque()
        q.append((0, 0))

        length = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                neighbors = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
                for dr, dc in neighbors:
                    curr_r, curr_c = r + dr, c + dc
                    if (min(curr_r, curr_c) < 0 or
                        curr_r == ROWS or curr_c == COLS or
                        (curr_r, curr_c) in visit or grid[curr_r][curr_c] == 1):
                        continue
                    
                    visit.add((curr_r, curr_c))
                    q.append((curr_r, curr_c))
            
            length += 1

        return -1

        