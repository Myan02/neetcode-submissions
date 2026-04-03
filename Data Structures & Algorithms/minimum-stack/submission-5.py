class MinStack:

    def __init__(self):
        self.main_s = []
        self.min_s = []
        

    def push(self, val: int) -> None:
        if not self.main_s:
            self.main_s.append(val)
            self.min_s.append(val)
            return
        
        if val > self.min_s[-1]:
            self.min_s.append(self.min_s[-1])
        else:
           self.min_s.append(val)
        
        self.main_s.append(val)
        

    def pop(self) -> None:
        self.main_s.pop()
        self.min_s.pop()
        

    def top(self) -> int:
        return self.main_s[-1]
        

    def getMin(self) -> int:
        return self.min_s[-1]
        
