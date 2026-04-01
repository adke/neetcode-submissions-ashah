class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqMap = {i:[] for i in range(numCourses)}
        for course, preReq in prerequisites:
            preqMap[course].append(preReq)

        visited = set()
        cycle = set()
        res = []

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)

            for preq in preqMap[course]:
                if not dfs(preq):
                    return False

            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return res