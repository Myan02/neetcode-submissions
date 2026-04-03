class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        def isValidChar(char):
            return (ord('a') <= ord(char) <= ord('z') or 
                    ord('A') <= ord(char) <= ord('Z') or
                    ord('0') <= ord(char) <= ord('9'))

        while left < right:
            while not isValidChar(s[left]) and left < right:
                left += 1
            
            while not isValidChar(s[right]) and left < right:
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
        