class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        visit = set()
        cycle = set()
        res = []

        for u, v in prerequisites:
            adj[u].append(v)

        def dfs(node):
            # BASE CASES FIRST
            if node in cycle:
                return False
            elif node in visit:
                return True
            else:
                cycle.add(node)
                for nei in adj[node]:
                    if not dfs(nei):
                        return False
                cycle.remove(node)
                visit.add(node)
                res.append(node)
                return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res
