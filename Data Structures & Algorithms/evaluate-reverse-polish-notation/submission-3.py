class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # return value if its the only one
        if len(tokens) < 2:
            return int(tokens[0])

        
        history_ = []       # history to keep track of what digits we have
        for char in tokens:
            match char:
                case '+':    
                    history_.append(history_.pop() + history_.pop())
                case '-':
                    a, b = history_.pop(), history_.pop()
                    history_.append(b - a)
                case '*':
                    history_.append(history_.pop() * history_.pop())
                case '/':
                    a, b = history_.pop(), history_.pop()
                    history_.append(int(float(b) / a))
                case _:
                    history_.append(int(char))
                
            
        return history_.pop()

            

            
                