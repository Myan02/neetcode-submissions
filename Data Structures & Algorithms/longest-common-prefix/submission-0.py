class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        result = ""
        strs.sort()

        for i in range(len(strs[0])):
            for word in strs[1:]:
                if strs[0][i] != word[i]:
                    return result
            
            result += strs[0][i]
        
        return result



            
        