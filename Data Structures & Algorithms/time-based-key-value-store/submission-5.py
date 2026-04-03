class TimeMap:

    def __init__(self):
        # init hashmap
        self.map = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        # set hashmap keys to also be hashmaps
        self.map[key].append([value, timestamp])
        print(self.map)

    def get(self, key: str, timestamp: int) -> str:
        """
        we need to find the value BEFORE the timestamp if
        the timestamp doesn't exist. We use binary search for it
        """
        res, values = "", self.map.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res