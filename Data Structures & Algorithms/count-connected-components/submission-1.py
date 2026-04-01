class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def dfs(curr):
            # base case
            if curr in visit:
                return

            visit.add(curr)

            for nei in adj[curr]:
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