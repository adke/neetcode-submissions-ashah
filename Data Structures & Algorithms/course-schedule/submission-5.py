class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create adjacency list
        adj = {i:[] for i in range(numCourses)}
        visit = set()
        
        for course, nei in prerequisites:
            adj[course].append(nei)

        print(adj)
        
        def dfs(node):
            if node in visit:
                return False

            if adj[node] == []:
                return True

            visit.add(node)

            for nei in adj[node]:
                if not dfs(nei):
                    return False
            
            visit.remove(node)
            adj[node] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True