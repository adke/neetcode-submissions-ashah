class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        visited = set()
        for index, nei in prerequisites:
            adj[index].append(nei)

        def dfs(courseIndex):
            # base cases
            if courseIndex in visited:
                return False
            if adj[courseIndex] == []:
                return True

            visited.add(courseIndex)

            for neighbor in adj[courseIndex]:
                if not dfs(neighbor):
                    return False

            adj[courseIndex] = []
            visited.remove(courseIndex)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True