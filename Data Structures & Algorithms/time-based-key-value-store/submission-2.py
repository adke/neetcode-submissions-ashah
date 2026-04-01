class TimeMap:

    def __init__(self):
        self.mapp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapp[key].append([value, timestamp])


    def get(self, key: str, timestamp: int) -> str:
        currlist = self.mapp.get(key, [])
        if not currlist:
            return ""
        else:
            l = 0
            r = len(currlist) - 1
            res = ""

            while l <= r:
                mid = (l + r) // 2
                curr = currlist[mid]
                if curr[1] > timestamp:
                    r = mid - 1
                else:
                    res = curr[0]
                    l = mid + 1

            return res
