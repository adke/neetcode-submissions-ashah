class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}

        for u, v in prerequisites:
            adj[u].append(v) # this is a directed graph

        visit = set()

        def dfs(node, visit):
            if node in visit:
                return False

            if adj[node] == []:
                return True

            visit.add(node)

            for nei in adj[node]:
                if not dfs(nei, visit):
                    return False
            adj[node] == []
            visit.remove(node)
            return True

        for i in range(numCourses):
            if not dfs(i, visit):
                return False
        
        return True
