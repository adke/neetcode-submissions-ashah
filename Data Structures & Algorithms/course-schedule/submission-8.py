class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}

        for u, v in prerequisites:
            adj[u].append(v)
        
        visit = set()
        def dfs(node):
            if node in visit:
                return False
            elif adj[node] == []:
                return True

            visit.add(node)

            for nei in adj[node]:
                if not dfs(nei):
                    return False
            visit.remove(node)
            adj[node] == []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
