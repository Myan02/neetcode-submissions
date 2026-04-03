class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        paren = {"}":"{",
                 "]":"[",
                 ")":"("}
        
        for c in s:
            if stack and c in paren and paren[c] == stack[-1]:
                stack.pop()
                continue
            
            stack.append(c)
        
        return True if not stack else False




        