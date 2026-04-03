class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        try:
            for i in range(len(words)):
                word = words[i]

                for j in range(len(word)):
                    if word[j] != words[j][i]:
                        return False
        except Exception:
            return False
        
        return True
            
                
        