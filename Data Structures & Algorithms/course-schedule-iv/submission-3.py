class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i:[] for i in range(numCourses)}
        for u, v in prerequisites:
            adj[v].append(u)


        def dfs(target, node, cache):
            if node == target:
                return True
            if adj[node] == []:
                return False
            if node in cache:
                return cache[node]

            for nei in adj[node]:
                if dfs(target, nei, cache):
                    return True
                else:
                    continue
            cache[node] = False
            return False
        
        res = []
        for x, y in queries:
            res.append(dfs(x, y, {}))

        return res

              