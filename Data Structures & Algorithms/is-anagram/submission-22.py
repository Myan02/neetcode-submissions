class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = [0] * 26    

        for i in range(len(s)):
            idx_s = ord(s[i]) - ord("a")
            idx_t = ord(t[i]) - ord("a")

            freq[idx_s] += 1
            freq[idx_t] -= 1
        
        for c in freq:
            if c:
                return False
        
        return True
            
        