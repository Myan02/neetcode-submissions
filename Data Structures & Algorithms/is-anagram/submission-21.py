class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0] * 26    
        