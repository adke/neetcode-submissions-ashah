class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # adjacency list problem
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)

        visit = set()
        
        def dfs(node):
            if adj[node] == []:
                return True
            if node in visit:
                return False

            visit.add(node)

            for nei in adj[node]:
                if not dfs(nei):
                    return False
            
            adj[node] = []
            visit.remove(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True