class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        if n == 0:
            return 0
        
        adj = {i:[] for i in range(n)}
        for index, nei in edges:
            adj[index].append(nei)
            adj[nei].append(index)

        visited = set()
        res = 0

        def dfs(node):
            # base case
            if node in visited:
                return

            visited.add(node)

            for nei in adj[node]:
                dfs(nei)

            return

        for i in range(n):
            if i in visited:
                continue
            else:
                dfs(i)
                res += 1

        return res
