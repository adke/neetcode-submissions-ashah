class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # need to create adj list first which we will use for DFS
        adj = defaultdict(list)
        for prereq in prerequisites:
            adj[prereq[0]].append(prereq[1])

        print(adj)

        # now DFS logic
        visit = set()
        def dfs(node):
            # base case always comes first
            if node in visit:
                return False
            if adj[node] == []:
                return True # return from here

            visit.add(node)

            # now check neighbour
            for nei in adj[node]:
                if not dfs(nei):
                    return False
            visit.remove(node)
            adj[node] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True