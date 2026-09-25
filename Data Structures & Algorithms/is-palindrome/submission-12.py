class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        
        l, r = 0, len(s) - 1
        while l <= r:
            if not self.isAlphaNum(s[l]):
                l += 1
                continue
            
            if not self.isAlphaNum(s[r]):
                r -= 1
                continue
            
            if self.lower(s[l]) != self.lower(s[r]):
                return False
            
            l += 1
            r -= 1
        
        return True
    
    def isAlphaNum(self, s: str):
        return ((ord("0") <= ord(s) <= ord("9")) or
               (ord("a") <= ord(s) <= ord("z")) or
               (ord("A") <= ord(s) <= ord("Z")))
    
    def lower(self, s: str):
        if ord("A") <= ord(s) <= ord("Z"):
            return chr(ord(s) + (ord("a") - ord("Z") + (ord("z") - ord("a"))))
        
        return s
        