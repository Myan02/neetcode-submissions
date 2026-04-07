class MyStack:

    def __init__(self):
        self.q_1 = deque()
        self.q_2 = deque()

        self.active = None
        self.size = 0
        

    def push(self, x: int) -> None:
        if not self.q_1:
            self.q_1.append(x)
            self.active = self.q_1
        
        else:
            self.q_2.append(x)
            self.active = self.q_2

        for _ in range(self.size):
            if self.active is self.q_1:
                self.q_1.append(self.q_2.popleft())
            else:
                self.q_2.append(self.q_1.popleft())

        self.size += 1


    def pop(self) -> int:
        if not self.size:
            return 0

        self.size -= 1

        if self.active is self.q_1:
            return self.q_1.popleft()
        
        return self.q_2.popleft()
        

    def top(self) -> int:
        if self.active is self.q_1:
            return self.q_1[0]
        
        return self.q_2[0]
        

    def empty(self) -> bool:
        return self.size == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()