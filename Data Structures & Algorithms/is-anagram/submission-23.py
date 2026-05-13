class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s = [0] * 26
        count_t = [0] * 26

        for i in range(len(s)):
            s_idx = ord(s[i]) - ord("a")
            t_idx = ord(t[i]) - ord("a")

            count_s[s_idx] += 1
            count_t[t_idx] += 1


        
        for s_num, t_num in zip(count_s, count_t):
            if s_num != t_num:
                return False
        
        return True



        