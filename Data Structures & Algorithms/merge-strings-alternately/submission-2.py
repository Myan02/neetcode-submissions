class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len = len(word1)
        word2_len = len(word2)
        res = ""

        for i in range(max(word1_len, word2_len)):
            if i < word1_len:
                res += word1[i]
            
            if i < word2_len:
                res += word2[i]
        
        return res
            
