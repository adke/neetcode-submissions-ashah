class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        hashMap = {i:[] for i in range(n)}
        visited = set()

        for i, j in edges:
            hashMap[i].append(j)
            hashMap[j].append(i)

        def dfs(currNode, prevNode):
            if currNode in visited:
                return False

            visited.add(currNode)

            for nei in hashMap[currNode]:
                if nei == prevNode:
                    continue
                if not dfs(nei, currNode):
                    return False
            return True

        if dfs(0, -1) and len(visited) == n:
            return True
        else:
            return False

        