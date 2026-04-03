class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        paren = {'}': '{',
                 ')': '(',
                 ']': '['}

        for char in s:
            if char in paren.keys() and stack:
                open_char = paren[char]
                if open_char == stack[-1]:
                    stack.pop()
                    continue
            
            stack.append(char)
            print("stack is:", stack)
        
        return False if stack else True
            




        