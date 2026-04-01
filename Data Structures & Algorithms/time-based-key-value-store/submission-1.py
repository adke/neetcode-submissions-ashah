class TimeMap:

    def __init__(self):
        self.res = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.res:
            self.res[key] = []
        self.res[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        currList = self.res.get(key, [])

        if len(currList) == 0:
            return ""
        
        value = ""
        l = 0
        r = len(currList) - 1

        while l <= r:
            mid = (l + r) // 2
            currTime = currList[mid][1]

            if currTime <= timestamp:
                value = currList[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return value
