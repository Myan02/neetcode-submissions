class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        string_key = [0] * 26

        for char in s1:
            idx = ord(char) - ord('a')
            string_key[idx] += 1
        
        print("string_key: ", string_key)
        print("")
        
        window = [0] * 26
        L = 0

        for R in range(len(s2)):
            if R < len(s1):
                window[ord(s2[R]) - ord('a')] += 1
                continue
            
            if window == string_key:
                return True
            
            window[ord(s2[L]) - ord('a')] -= 1
            window[ord(s2[R]) - ord('a')] += 1
            L += 1

        
        return window == string_key

        