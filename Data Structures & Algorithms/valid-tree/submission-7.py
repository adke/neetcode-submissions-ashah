class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        cycle = set()
        visit = set()

        adj = {i:[] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, prev):
            if node in cycle:
                return False

            if node in visit:
                return True

            cycle.add(node)

            for nei in adj[node]:
                if nei == prev:
                    continue
                elif not dfs(nei, node):
                    return False

            cycle.remove(node)
            visit.add(node)
            return True

        if not dfs(0, -1):
            return False
        elif len(visit) == n:
            return True
        else:
            return False
