class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        L = 0   # start of window
        window = set()  # window contents

        for R in range(len(s)):
            while s[R] in window:
                window.remove(s[L])
                L += 1

            window.add(s[R])
            res = max(res, len(window))

        return res
                
        