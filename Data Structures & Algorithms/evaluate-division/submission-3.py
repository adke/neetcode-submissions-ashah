class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i in range(len(equations)):
            u, v = equations[i]
            adj[u].append([v, values[i]])
            adj[v].append([u, 1 / values[i]])

        
        def bfs(start, target):
            if start not in adj or target not in adj:
                return -1.0

            visit = set()
            q = deque()
            q.append([start, 1])

            while q:
                currLen = len(q)
                curr = q.popleft()
                currTarget, currRes = curr[0], curr[1]
                visit.add(currTarget)
                if currTarget == target:
                    return currRes
                for nei in adj[currTarget]:
                    if nei[0] not in visit:
                        q.append([nei[0], nei[1] * currRes])
                    else:
                        continue

            return -1.0
        res = []
        for x, y in queries:
            res.append(bfs(x, y))

        return res

            

                
                    