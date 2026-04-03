class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.sums = [[0] * len(row) for row in matrix]

        ROWS = len(matrix)
        COLS = len(matrix[0])
        for r in range(ROWS):
            for c in range(COLS):
                if r == 0:
                    self.sums[r][c] = matrix[r][c] + self.sums[r][c - 1] if c > 0 else matrix[r][c]

                elif c == 0:
                    self.sums[r][c] = matrix[r][c] + self.sums[r - 1][c]

                else:
                    self.sums[r][c] = matrix[r][c] + self.sums[r][c - 1] + self.sums[r - 1][c] - self.sums[r - 1][c - 1]             
        print(self.sums)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        main_sum = self.sums[row2][col2]
        preLeft = self.sums[row2][col1 - 1] if col1 > 0 else 0
        preTop = self.sums[row1 - 1][col2] if row1 > 0 else 0
        preDiag = self.sums[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return main_sum - preLeft - preTop + preDiag
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)