class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # loop through every char 
        # at every char, if the char is equal to the first char of "word", run DFS

        def word_dfs(r: int, c: int, visit: set, word: str) -> bool:
            if not word:
                return True
            
            if (min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or board[r][c] != word[0]):
                return False
            
            visit.add((r, c))

            if word_dfs(r + 1, c, visit, word[1:]):
                return True
            if word_dfs(r - 1, c, visit, word[1:]):
                return True
            if word_dfs(r, c + 1, visit, word[1:]):
                return True
            if word_dfs(r, c - 1, visit, word[1:]):
                return True
            visit.remove((r, c))
            return False

        
        ROWS, COLS = len(board), len(board[0])
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    word_exists = True if word_dfs(r, c, set(), word) else False
                    if word_exists:
                        return True
        
        return False


        