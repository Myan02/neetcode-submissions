class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # base case if there is only one word in strs
        if len(strs) == 1:
            return strs[0]
        
        # sort the list to make the prefix's matchup
        result = ""
        strs.sort()

        # loop through the first words indeces
        for i in range(len(strs[0])):
            
            # loop through each other word
            for word in strs[1:]:

                # break if the prefix is not correct
                if strs[0][i] != word[i]:
                    return result
            
            result += strs[0][i]
        
        return result



            
        