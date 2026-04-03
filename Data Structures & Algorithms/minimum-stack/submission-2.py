class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        # push to main stack
        self.main_stack.append(val)
    
        # if min stack is empty, push to min stack
        if not self.min_stack:
            self.min_stack.append(val)

        # if min stack is not empty, check if val is smaller than min_stack[-1]
        else:
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)

    def pop(self) -> None:
        # pop and store top of stack
        curr = self.main_stack.pop()
        
        # if value is a min value, we also want to get rid of it from the min stack
        if curr == self.min_stack[-1]:
            self.min_stack.pop()


    def top(self) -> int:
        return self.main_stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
