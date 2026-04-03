class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif stack:
                if char == ')' and stack.pop() == '(':
                    continue

                if char == ']' and stack.pop() == '[':
                    continue

                if char == '}' and stack.pop() == '{':
                    continue
                
                return False
            else:
                return False

        

        return False if stack else True
        