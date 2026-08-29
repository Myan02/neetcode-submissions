class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, squares = {}, {}, {}

        ROWS = COLS = len(board)

        """
            (0, 0) (0, 1) (0, 2)   (0, 3) (0, 4) (0, 5)
            (1, 0) (1, 1) (1, 2)   (1, 3) (1, 4) (1, 5)
            (2, 0) (2, 1) (2, 2)   (2, 3) (2, 4) (2, 5)

            
        """

        for r in range(ROWS):
            for c in range(COLS):
                val = board[r][c]

                if val == ".":
                    continue
                
                cur_square = (r // 3 * 3) + c // 3

                if r not in rows:
                    rows[r] = set()
                if c not in cols:
                    cols[c] = set()
                if cur_square not in squares:
                    squares[cur_square] = set()
                
                if val in rows[r] or val in cols[c] or val in squares[cur_square]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                squares[cur_square].add(val)

                print(squares)
                print()

        
        return True

                

                

        