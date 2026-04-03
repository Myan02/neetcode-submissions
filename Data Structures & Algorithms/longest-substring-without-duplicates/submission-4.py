class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep two pts
        # increment the right ptr as long as the next char hasn't been seen yet
        # increment the left ptr when you find a value in your window
        # use a var to keep track of the max length 
        
        l, r = 0, 0
        res = 0
        window = set()

        while r < len(s):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])    
            r += 1
            res = max(res, r - l)
            
        return res

        