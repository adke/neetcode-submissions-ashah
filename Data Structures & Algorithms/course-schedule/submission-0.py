class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        visited = set()
        preMap = {i:[] for i in range(numCourses)}

        for crs, prereq in prerequisites:
            preMap[crs].append(prereq)

        def dfs(course):

            if course in visited:
                return False
            
            if preMap[course] == []:
                return True

            visited.add(course)

            for child in preMap[course]:
                if not dfs(child):
                    return False
            
            visited.remove(course)
            preMap[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True