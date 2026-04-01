class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # create undirected adj list
        adj = {i:[] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def dfs(curr, prev):
            # base case
            if curr in visit:
                return False

            visit.add(curr)

            for nei in adj[curr]:
                if nei == prev:
                    continue
                if not dfs(nei, curr):
                    return False
            return True

        if dfs(0, -1) and len(visit) == n:
            return True
        else:
            return False