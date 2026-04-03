class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowCount = defaultdict(set)
        colCount = defaultdict(set)
        squareCount = defaultdict(set)

        ROWS, COLS = len(board), len(board[0])
        for row in range(ROWS):
            for col in range(COLS):
                val = board[row][col]
                square = (row // 3) * 3 + (col // 3)


                if val == ".":
                    continue
                

                if val in rowCount[row]:
                    return False
                
                if val in colCount[col]:
                    return False
                
                if val in squareCount[square]:
                    return False
                
                rowCount[row].add(val)
                colCount[col].add(val)
                squareCount[square].add(val)
        
        return True

        