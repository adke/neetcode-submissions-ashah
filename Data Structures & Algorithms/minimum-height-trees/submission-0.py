class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        
        
        nodeCount = n
        adj = {i:[] for i in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        q = deque()
        edgeCount = {}
        for i in range(n):
            if len(adj[i]) == 1:
                q.append(i)
            edgeCount[i] = len(adj[i]) # proportional to the neighbor count

        while q:
            if nodeCount <= 2:
                return list(q)
            currLen = len(q)
            for i in range(currLen):
                curr = q.popleft()
                nodeCount -= 1
                for nei in adj[curr]:
                    edgeCount[nei] -= 1
                    if edgeCount[nei] == 1:
                        q.append(nei)

        
                
                

            