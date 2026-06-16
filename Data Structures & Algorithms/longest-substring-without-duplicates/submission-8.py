class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        window = {}
        longest_substr = 0
        L = 0

        for R in range(len(s)):
            if s[R] in window and L <= window[s[R]]:
                L = window[s[R]] + 1

            window[s[R]] = R
            longest_substr = max(longest_substr, R - L + 1)
        
        return longest_substr


        