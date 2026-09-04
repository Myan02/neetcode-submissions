class MinStack:

    def __init__(self):
        self.stack: list[tuple[int, int]] = []

        

    def push(self, val: int) -> None:
        stack = self.stack

        if not stack:
            stack.append((val, val))
            return
        
        cur_min = stack[-1][1]  # get min value

        if val < cur_min:
            next_val = (val, val)
        else:
            next_val = (val, cur_min)
        
        stack.append(next_val)
        

    def pop(self) -> None:
        stack = self.stack

        if stack:
            stack.pop()
        
        

    def top(self) -> int:
        stack = self.stack

        if stack:
            return stack[-1][0]
        

    def getMin(self) -> int:
        stack = self.stack

        if stack:
            return stack[-1][1]
        
