class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i:[] for i in range(numCourses)}
        preMap = {} # goal is to fill this in for O(1) lookup when checking queries

        for u, v in prerequisites:
            adj[v].append(u)

        def dfs(node):
            # base case
            if node in preMap:
                return preMap[node]
            
            preMap[node] = set()
            for nei in adj[node]:
                preMap[node] |= dfs(nei)
            preMap[node].add(node)
            
            return preMap[node]
            

        for i in range(numCourses):
            dfs(i)

        res = []
        for x, y in queries:
            if x in preMap[y]:
                res.append(True)
            else:
                res.append(False)

        return res

        