class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        q = deque()
        q.append(["0000", 0])
        visit = set(deadends)
        visit.add("0000")

        def children(comb):
            res = []
            for i in range(4):
                digit = (int(comb[i]) + 1) % 10
                res.append(comb[:i] + str(digit) + comb[i+1:])
                digit = ((int(comb[i]) - 1) + 10) % 10
                res.append(comb[:i] + str(digit) + comb[i+1:])
            return res

        while q:
            for i in range(len(q)):
                combo, count = q.popleft()
                if combo == target:
                    return count

                for child in children(combo):
                    if child not in visit:
                        visit.add(child)
                        q.append([child, count + 1])
                    else:
                        continue

        return -1