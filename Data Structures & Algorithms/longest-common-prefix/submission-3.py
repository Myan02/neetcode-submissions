class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        res = ""
        min_length = len(strs[0])

        for s in strs:
            min_length = min(min_length, len(s))
        
        for i in range(min_length):
            letter = strs[0][i]
            for word in strs[1:]:
                if letter != word[i]:
                    return res
            
            res += letter

        return res


        

