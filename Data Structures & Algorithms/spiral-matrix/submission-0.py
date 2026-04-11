class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        used = set()
        ROWS, COLS = len(matrix), len(matrix[0])
        direction = "right"

        res = []

        r, c = 0, 0
        
        while len(used) != (ROWS * COLS):
            if direction == "right":
                if (r, c) in used or c >= COLS:
                    c -= 1
                    r += 1
                    direction = "down"
                else:
                    used.add((r, c))
                    res.append(matrix[r][c])
                    c += 1
                            
            elif direction == "down":
                if (r, c) in used or r >= ROWS:
                    r -= 1
                    c -= 1
                    direction = "left"
                else:
                    used.add((r, c))
                    res.append(matrix[r][c])
                    r += 1
            
            elif direction == "left":
                if (r, c) in used or c < 0:
                    c += 1
                    r -= 1
                    direction = "up"
                else:
                    used.add((r, c))
                    res.append(matrix[r][c])
                    c -= 1
            
            elif direction == "up":
                if (r, c) in used or r < 0:
                    r += 1
                    c += 1
                    direction = "right"
                else:
                    used.add((r, c))
                    res.append(matrix[r][c])
                    r -= 1
        
        return res




        
        