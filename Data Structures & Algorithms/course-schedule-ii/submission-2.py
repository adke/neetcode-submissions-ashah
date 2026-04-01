class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # first create adjancency list
        adj = {i:[] for i in range(numCourses)}
        for index, preq in prerequisites:
            adj[index].append(preq)
        
        visited = set()
        cycle = set()
        res = []

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)

            for preq in adj[course]:
                if not dfs(preq):
                    return False

            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res