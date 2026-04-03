class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        # if array is full
        if self.size == self.capacity:
            self.resize()
        
        # if array is not full
        self.array[self.size] = n
        self.size += 1


    def popback(self) -> int:
        last_value = self.array[self.size - 1]
        self.array[self.size - 1] = 0
        self.size -= 1
        
        return last_value

    def resize(self) -> None:
        self.capacity *= 2
        new_array = [0] * self.capacity

        for i in range(self.size):
            new_array[i] = self.array[i]
        
        self.array = new_array

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
