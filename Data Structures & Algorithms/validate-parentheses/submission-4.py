class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) % 2) != 0:
            return False
        
        char_pairs = {']': '[', 
                      ')': '(', 
                      '}': '{' }
        
        stack = []

        for char in s:
            if char in char_pairs:
                if stack and stack[-1] == char_pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
                
            
        if stack:
            return False
        return True
        

                 


        