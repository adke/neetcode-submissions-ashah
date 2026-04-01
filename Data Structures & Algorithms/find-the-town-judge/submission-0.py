class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj = {i:[] for i in range(1, n + 1)}
        visit = set()

        for u, v in trust:
            adj[u].append(v)

        for i in range(1, n + 1):
            if adj[i] != []:
                visit.add(adj[i][0])
            else:
                continue

        if len(visit) == 1:
            myList = list(visit)
            return myList[0]
        else:
            return -1
