class Solution:
    def isValid(self, s: str) -> bool:
    
        capacity = len(s)

        if capacity < 2:
            return False

        stack = []
        pair = {
                ')' : '(', 
                '}' : '{',
                ']' : '[' 
        }

        for char in s:
            # check if closing
            if char in pair:
                if stack and stack[-1] == pair[char]:
                    stack.pop()
                else:
                    return False
            
            # opening char
            else:
                stack.append(char)
        
        return True if not stack else False            


        