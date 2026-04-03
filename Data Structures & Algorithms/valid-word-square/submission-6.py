class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        
        for row_idx in range(len(words)):
            word = words[row_idx]

            tmp = ""
            col_idx = 0
            while col_idx < len(words) and row_idx < len(words[col_idx]):
                tmp += words[col_idx][row_idx]
                col_idx += 1

            if word != tmp:
                return False
        
        return True
