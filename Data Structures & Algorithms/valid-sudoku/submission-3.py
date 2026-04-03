class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        n = len(board)

        for row in range(n):
            for col in range(n):

                if board[row][col] == ".":
                    continue
                
                val = board[row][col]
                square = (row // 3) * 3 + (col // 3)
                
                if val in rows[row]:
                    return False
                
                if val in cols[col]:
                    return False
                
                if val in squares[square]:
                    return False
                
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[square].add(board[row][col])
        
        return True






