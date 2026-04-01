class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        q = deque(["0000"])
        visited = set()
        visited.add("0000")
        
        for deadend in deadends:
            visited.add(deadend)

        def findChildren(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res

        res = 0
        while q:
            for i in range(len(q)):
                lock = q.popleft()
                if lock == target:
                    return res
                for child in findChildren(lock):
                    if child not in visited:
                        q.append(child)
                        visited.add(child)
            res += 1
        return - 1

                

            

