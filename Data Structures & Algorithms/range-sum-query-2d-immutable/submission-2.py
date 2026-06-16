class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        ROWS = len(matrix)
        COLS = len(matrix[0])

        for r in range(ROWS):
            for c in range(COLS):
                cur = matrix[r][c]

                if c > 0:
                    cur += matrix[r][c - 1]
                if r > 0:
                    cur += matrix[r - 1][c]
                if r > 0 and c > 0:
                    cur -= matrix[r - 1][c - 1]
                
                self.matrix[r][c] = cur
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total_sum = self.matrix[row2][col2]
        difference_col = self.matrix[row2][col1 - 1] if col1 > 0 else 0
        difference_row = self.matrix[row1 - 1][col2] if row1 > 0 else 0
        padding = self.matrix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0

        return total_sum - difference_col - difference_row + padding
        
        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)