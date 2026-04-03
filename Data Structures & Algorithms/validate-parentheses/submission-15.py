class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        paren = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        stack = []

        for c in s:
            if c not in paren:
                stack.append(c)
            else:
                if stack and stack[-1] != paren[c]:
                    return False
                stack.pop()
        return True


        