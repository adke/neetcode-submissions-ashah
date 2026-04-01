class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visited = set()
        prereq = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        def dfs(course):
            if course in visited:
                return False
            if prereq[course] == []:
                return True

            visited.add(course)

            for neighbor in prereq[course]:
                if not dfs(neighbor):
                    return False

            visited.remove(course)
            prereq[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
