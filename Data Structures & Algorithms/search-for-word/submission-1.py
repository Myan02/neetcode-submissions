class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])

        def search(r, c, seen, word):
            if len(word) == 0:
                return True

            # out of bounds
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in seen or board[r][c] != word[0]:
                return False
            
            seen.add((r, c))

            if search(r + 1, c, seen, word[1:]):
                return True
            if search(r - 1, c, seen, word[1:]):
                return True
            if search(r, c + 1, seen, word[1:]):
                return True
            if search(r, c - 1, seen, word[1:]):
                return True

            seen.remove((r, c))
            return False


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    res = search(r, c, set(), word)
                    if res:
                        return True
        
        return False