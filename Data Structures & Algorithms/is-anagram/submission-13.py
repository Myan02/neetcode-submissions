class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq1 = defaultdict(int)
        freq2 = defaultdict(int)

        for c1, c2 in zip(s, t):
            freq1[c1] += 1
            freq2[c2] += 1
        
        return freq1 == freq2

        
        