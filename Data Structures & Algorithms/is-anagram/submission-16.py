class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        char_count_s = [0] * 26
        char_count_t = [0] * 26

        for c1, c2 in zip(s, t):
            char_count_s[ord(c1) - ord('a')] += 1
            char_count_t[ord(c2) - ord('a')] += 1

        return char_count_s == char_count_t

        
        