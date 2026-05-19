class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # DIRECTED GRAPH
        adj = {i:[] for i in range(numCourses)}

        for u, v in prerequisites:
            adj[u].append(v)

        visit = set()
        cycle = set()
        res = []

        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True

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

        if len(res) == numCourses:
            return res
        else:
            return []
