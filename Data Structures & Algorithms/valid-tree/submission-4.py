class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        visit = set()
        count = 0

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, nei):
            nonlocal count
            # edge case
            if node in visit:
                return False
            
            visit.add(node)

            for n in adj[node]:
                if n == nei:
                    continue
                else:
                    if not dfs(n, node):
                        return False
            visit.remove(node)
            count += 1
            return True
        
        if not dfs(0, -1) or count != n:
            return False
        else:
            return True


    
