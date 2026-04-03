class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # only need n since board is 9x9
        for r in range(n):
            for c in range(n):
                # get values
                val = board[r][c]   
                square = (r // 3) * 3 + (c // 3)

                # skip empty values
                if val == '.':
                    continue
                
                val = int(val)  # convert to integer

                # check if value exists in current row
                if val in rows[r]:
                    return False
                
                # check if value exists in current col
                if val in cols[c]:
                    return False
                
                # check if value exists in current square
                if val in squares[square]:
                    return False
                
                # add values to hashset to keep track of what we have
                rows[r].add(val)
                cols[c].add(val)
                squares[square].add(val)
        
        return True
        