class MinStack:

    def __init__(self):
        self.stack_ = []
        self.minVal_ = []

    def push(self, val: int) -> None:
        self.stack_.append(val)

        # initial append
        if not self.minVal_:
            self.minVal_.append(val)
        else:
            val = min(val, self.minVal_[-1])
            self.minVal_.append(val)


    def pop(self) -> None:
        self.stack_.pop()
        self.minVal_.pop()

    def top(self) -> int:
        return self.stack_[-1]

    def getMin(self) -> int:
        return self.minVal_[-1]
