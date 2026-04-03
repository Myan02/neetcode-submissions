class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # build string 1 key 
        string_key = [0] * 26
        for char in s1:
            idx = ord(char) - ord('a')
            string_key[idx] += 1
        
        # window contains key of size len(s1) 
        window = [0] * 26
        L = 0

        for R in range(len(s2)):

            # build s2 key until window size reaches size of s1 key
            if R < len(s1):
                window[ord(s2[R]) - ord('a')] += 1
                continue
            
            # check if keys are the same
            if window == string_key:
                return True
            
            # iterate window by one
            window[ord(s2[L]) - ord('a')] -= 1
            window[ord(s2[R]) - ord('a')] += 1
            L += 1

        
        return window == string_key

        