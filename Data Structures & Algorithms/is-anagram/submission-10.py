class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_freq = defaultdict(int)
        t_freq = defaultdict(int)

        for s_char, t_char in zip(s, t):
            s_freq[s_char] += 1
            t_freq[t_char] += 1
        
        return s_freq == t_freq
            

