class MyStack:

    def __init__(self):
        self.q = deque()
        self.size = 0

        
    def push(self, x: int) -> None:
        new_q = deque()
        new_q.append(x)
        new_q.append(self.q)

        self.q = new_q
        self.size += 1


    def pop(self) -> int:
        if not self.size:
            return 0

        res = self.q.popleft()
        self.q = self.q.popleft()
        self.size -= 1
        
        return res

        

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return self.size == 0
        