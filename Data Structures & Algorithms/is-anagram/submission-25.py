class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = [0] * 26

        for num_s, num_t in zip(s, t):
            counts[ord(num_s) - ord('a')] += 1
            counts[ord(num_t) - ord('a')] -= 1
        
        for num in counts:
            if num != 0:
                return False
        
        return True

        