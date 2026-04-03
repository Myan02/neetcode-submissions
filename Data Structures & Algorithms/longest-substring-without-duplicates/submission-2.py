class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = 0
        res = 0         # keep track of largest substring
        window = set()  # keep track of window 

        L = 0           # window left pointer
        R = 0
        while R < len(s):
            if s[R] not in window:
                window.add(s[R])
                curr += 1
                res = max(res, curr)
                R += 1
                continue
            
            window.remove(s[L])
            curr -= 1
            L += 1

        return res
        


        