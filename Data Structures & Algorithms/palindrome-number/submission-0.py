class Solution:
    def isPalindrome(self, x: int) -> bool:
        # initial thoughts, convert x to a string and use l and r pointers to check for palindrome

        # can't be negative
        if x < 0:
            return False

        x = str(x)
        l, r = 0, len(x) - 1

        while l < r:
            if x[l] != x[r]:
                return False
            
            l += 1
            r -= 1
        
        return True

        