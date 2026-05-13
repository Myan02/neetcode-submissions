class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        res = ""
        shortest_word = float("inf")

        for word in strs:
            shortest_word = min(shortest_word, len(word))
        
        for i in range(int(shortest_word)):
            curr_letter = strs[0][i]
            
            for word in strs[1:]:
                if word[i] != curr_letter:
                    return res
                
            res += curr_letter
        
        return res
                

        
        