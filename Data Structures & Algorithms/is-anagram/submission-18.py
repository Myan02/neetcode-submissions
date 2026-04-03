class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26

        for c in s:
            idx = ord(c) - ord("a")
            freq1[idx] += 1
        
        for c in t:
            idx = ord(c) - ord("a")
            freq2[idx] += 1
        
        return freq1 == freq2
        

        