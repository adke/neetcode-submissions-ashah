class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if not n:
            return True

        childMap = {i:[] for i in range(n)}
        visited = set()

        for j,k in edges:
            childMap[j].append(k)
            childMap[k].append(j)

        def dfs(currNode, prevNode):
            if currNode in visited:
                return False

            visited.add(currNode)

            for child in childMap[currNode]:
                if child == prevNode:
                    continue
                if not dfs(child, currNode):
                    return False
            return True

        if dfs(0, -1) and n == len(visited):
            return True
        else:
            return False
            


        