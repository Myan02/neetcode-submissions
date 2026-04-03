class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        result = ""

        for i in range(max(n, m)):
            if i < n:
                result += word1[i]
            if i < m:
                result += word2[i]
            
        return result