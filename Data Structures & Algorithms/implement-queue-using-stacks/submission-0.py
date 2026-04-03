class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.length = 0
        

    def push(self, x: int) -> None:
        if not self.s1:
            self.s1.append(x)
            self.length += 1
            return
        
        for i in range(self.length):
            self.s2.append(self.s1.pop())
        
        self.s1.append(x)

        for i in range(self.length):
            self.s1.append(self.s2.pop())
        
        self.length += 1
        
        
    def pop(self) -> int:
        self.length -= 1
        return self.s1.pop()
        
    def peek(self) -> int:
        return self.s1[-1]
        
    def empty(self) -> bool:
        return True if not self.s1 else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()