class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        while L < R:
            if not self.isValidChar(s[L]):
                L += 1
                continue
            
            if not self.isValidChar(s[R]):
                R -= 1
                continue
            
            if s[L].lower() != s[R].lower():
                return False
            
            L += 1
            R -= 1
        
        return True

    def isValidChar(self, c: str) -> bool:
        return (
            ord('a') <= ord(c) <= ord('z') or
            ord('A') <= ord(c) <= ord('Z') or
            ord('0') <= ord(c) <= ord('9')
        );
