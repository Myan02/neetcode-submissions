class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_map = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        for c in s:
            if stack and c in paren_map and stack[-1] == paren_map[c]:
                stack.pop()
                continue
            
            stack.append(c)
        
        return True if not stack else False
