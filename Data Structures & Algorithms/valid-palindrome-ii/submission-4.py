class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindromeHelper(l: int, r: int, savior: bool) -> bool:
            while l < r:
                if s[l] != s[r]:
                    if savior:
                        return palindromeHelper(l + 1, r, False) or palindromeHelper(l, r - 1, False)
                    return False
                
                l += 1
                r -= 1
            
            return True

        # initialize values for helper
        l, r = 0, len(s) - 1
        savior = True

        return palindromeHelper(l, r, savior)

        