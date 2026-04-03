class MyHashMap:

    def __init__(self):
        self.table = []

    def put(self, key: int, value: int) -> None:
        for i, pair in enumerate(self.table):
            if key == pair[0]:
                self.table[i][1] = value
                return
            
        self.table.append([key, value])
        

    def get(self, key: int) -> int:
        for pair in self.table:
            if pair[0] == key:
                return pair[1]
        
        return -1
        

    def remove(self, key: int) -> None:
        for i, pair in enumerate(self.table):
            if key == pair[0]:
                self.table.pop(i)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)