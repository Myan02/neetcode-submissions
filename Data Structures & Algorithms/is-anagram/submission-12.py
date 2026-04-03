class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        for char1, char2 in zip(s, t):
            freq1[char1] += 1
            freq2[char2] += 1
        
        return freq1 == freq2