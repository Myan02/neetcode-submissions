class TimeMap:

    def __init__(self):
        self.tmap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append((timestamp, value))
        

    """
    times: [(1, happy)]
    times: [(1, happy), (3, sad)], looking for 6

    """
    def get(self, key: str, timestamp: int) -> str:
        cur = self.tmap[key]
        res = ""

        if not cur:
            return ""

        L, R, mid = 0, len(cur) - 1, 0
        while L <= R:
            mid = (L + R) // 2

            if cur[mid][0] <= timestamp:
                res = cur[mid][1]
                L = mid + 1
            else:
                R = mid - 1

        return res

        
