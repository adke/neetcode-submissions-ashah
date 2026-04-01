class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        res = []
        
        for i, eq in enumerate(equations):
            adj[eq[0]].append([eq[1], values[i]])
            adj[eq[1]].append([eq[0], 1 / values[i]])
        

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1               
            visit = set()
            q = deque()
            q.append([src, 1])
            visit.add((src))

            while q:
                for i in range(len(q)):
                    currN, currVal = q.popleft()
                    if currN == target:
                        return currVal

                    for nei in adj[currN]:
                        if nei[0] in visit:
                            continue
                        q.append([nei[0], currVal * nei[1]])
                        visit.add(nei[0])
            return -1

        for num, den in queries:
            res.append(bfs(num, den))

        return res
