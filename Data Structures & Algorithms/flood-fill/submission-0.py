class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        ROWS, COLS = len(image), len(image[0])

        def floorFillDfs(r, c, start_color):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or image[r][c] != start_color or image[r][c] == color:
                return
            
            image[r][c] = color

            floorFillDfs(r + 1, c, start_color)
            floorFillDfs(r - 1, c, start_color)
            floorFillDfs(r, c + 1, start_color)
            floorFillDfs(r, c - 1, start_color)

        
        floorFillDfs(sr, sc, image[sr][sc])
        return image

        