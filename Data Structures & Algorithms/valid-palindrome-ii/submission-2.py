class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return (self.palindrome(l + 1, r, s) or self.palindrome(l, r - 1, s))

            l += 1
            r -= 1

        return True
    
    def palindrome(self, l: int, r: int, s: str) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        return True
    