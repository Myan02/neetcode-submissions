class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # base case, 1 token
        if len(tokens) <= 1:
            return int(tokens[0])
        
        operands = []

        for token in tokens:
            if token == "+":
                op1, op2 = operands.pop(), operands.pop()
                operands.append(op2 + op1)
                continue
            
            if token == "-":
                op1, op2 = operands.pop(), operands.pop()
                operands.append(op2 - op1)
                continue

            if token == "*":
                op1, op2 = operands.pop(), operands.pop()
                operands.append(op2 * op1)
                continue

            if token == "/":
                op1, op2 = operands.pop(), operands.pop()
                quotient = op2 / op1
                quotient = math.ceil(quotient) if quotient < 0 else math.floor(quotient)
                operands.append(quotient)
                continue
            
            operands.append(int(token))
        
        return operands[0]




