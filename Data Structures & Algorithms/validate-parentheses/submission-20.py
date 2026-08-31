class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        brackets = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []

        # stack = 
        for c in s:
            if c in brackets and stack:
                if brackets[c] != stack[-1]:
                    return False
                
                stack.pop()
            
            else:
                stack.append(c)
        
        return False if stack else True


        