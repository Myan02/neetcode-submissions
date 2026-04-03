class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        shorter_word_length = min(len(word1), len(word2))

        i = 0
        while i < shorter_word_length:
            result = result + word1[i] + word2[i]
            i += 1
        
        if len(word1) == shorter_word_length:
            return result + word2[i:]
        else:
            return result + word1[i:]
           
            

