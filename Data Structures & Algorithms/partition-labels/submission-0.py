class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for i, c in enumerate(s):
            lastIndex[c] = i

        res = []
        count = 0
        end = 0
        for i, c in enumerate(s):
            end = max(end, lastIndex[c])
            count += 1

            if i == end:
                res.append(count)
                count = 0

        return res

        