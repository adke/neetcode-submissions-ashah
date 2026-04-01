class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])
        return
        
    def get(self, key: str, timestamp: int) -> str:
        arr = self.store[key]
        res = ""
        if arr == []:
            return res
        l = 0
        r = len(arr) - 1

        while l <= r:
            m = (l + r) // 2
            if arr[m][1] <= timestamp:
                res = arr[m][0]
                l = m + 1
            else:
                r = m - 1
        return res


