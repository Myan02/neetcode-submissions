class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for c in tokens:
            try:
                stack.append(int(c))

            except:
                a, b = stack.pop(), stack.pop()
                stack.append(int(eval(f"{b} {c} {a}")))

        return stack[-1]

            
        