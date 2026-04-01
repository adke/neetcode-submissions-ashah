class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        visit = set()

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            # base case
            if node in visit:
                return

            visit.add(node)

            for nei in adj[node]:
                dfs(nei)
            return

        count = 0
        for i in range(n):
            if i in visit:
                continue
            else:
                dfs(i)
                count += 1

        return count

        


