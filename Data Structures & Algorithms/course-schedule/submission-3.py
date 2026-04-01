class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # courses are represented by indices not actual numbers
        hashMap = {i:[] for i in range(numCourses)}
        # filling in hashMap value 
        for courseIndex, preq in prerequisites:
            hashMap[courseIndex].append(preq)
        visited = set()

        def dfs(course):
            # check base cases
            if course in visited:
                return False
            if hashMap[course] == []:
                return True

            visited.add(course)

            for preq in hashMap[course]:
                if not dfs(preq):
                    return False

            visited.remove(course)
            hashMap[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
