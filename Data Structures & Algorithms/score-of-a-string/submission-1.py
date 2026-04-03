class Solution:
    def scoreOfString(self, s: str) -> int:
        L = 0
        res = 0

        for R in range(1, len(s)):
            pair = abs(ord(s[R]) - ord(s[L]))
            res += pair
            L += 1
        
        
        return res
        