class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        paren = {
            "]": "[",
            ")": "(",
            "}": "{"
        }

        # 1. if open paren, push to stack
        # 2. if close paren, check to make sure the stack isn't empty + that 
        #    it matches the top of stack
        # 3. if it is the same as top of stack, remove from stack. 
        # 4. check if stack is empty or not

        stack = []

        for c in s:
            if c in paren:
                if stack and paren[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
                
                continue
                
            stack.append(c)
        
        return False if stack else True


        