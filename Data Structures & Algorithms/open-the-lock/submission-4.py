class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if "0000" in deadends:
            return -1

        visit = set(deadends)
        q = deque(["0000"])
        res = 0

        def findChildren(combo):
            res = []
            for i in range(4):
                digit = combo[i]
                add = (int(digit) + 1) % 10
                res.append(combo[:i] + str(add) + combo[i + 1:])
                sub = (int(digit) - 1 + 10) % 10
                res.append(combo[:i] + str(sub) + combo[i + 1:])
            return res


        while q:
            currLen = len(q)
            for i in range(currLen):
                curr = q.popleft()
                if curr == target:
                    return res
                for child in findChildren(curr):
                    if child not in visit:
                        q.append(child)
                        visit.add(child)
                    else:
                        continue
            res += 1

        return -1

