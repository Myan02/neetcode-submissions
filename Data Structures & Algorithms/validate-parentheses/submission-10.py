class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis = {']': '[',
                       '}': '{', 
                       ')': '('}
        
        for char in s:
            # is a closing paren and matches the most recent open paren
            if stack and char in parenthesis.keys() and parenthesis[char] == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        
        return False if stack else True
        