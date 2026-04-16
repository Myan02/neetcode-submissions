class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1:
            return -1

        N = len(grid)

        visit = set()
        queue = deque()
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1)
        ]

        queue.append((0, 0))
        visit.add((0, 0))

        length = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if r == N - 1 and c == N - 1:
                    return length
                
                for dr, dc in directions:

                    if min(r + dr, c + dc ) < 0 or r + dr == N or c + dc == N or (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1:
                        continue
                    
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            
            length += 1
        
        return -1






                

        
        