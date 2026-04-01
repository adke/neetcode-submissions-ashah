class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        res = []
        preMap = {i:[] for i in range(numCourses)}

        for crse, prereq in prerequisites:
            preMap[crse].append(prereq)

        visited, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)

            for child in preMap[course]:
                if not dfs(child):
                    return False
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []

        return res



