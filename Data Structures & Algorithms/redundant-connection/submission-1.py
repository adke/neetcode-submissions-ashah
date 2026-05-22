class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1 for i in range(n + 1)]

        def rootParent(node):
            currParent = parent[node]
            if currParent == node:
                return currParent
            return rootParent(currParent)

        def union(n1, n2):
            p1 = rootParent(n1)
            p2 = rootParent(n2)
            if p1 == p2:
                return False
            else:
                if rank[p1] >= rank[p2]:
                    rank[p1] += rank[p2]
                    parent[p2] = p1
                else:
                    rank[p2] += rank[p1]
                    parent[p1] = p2
            return True

        for x, y in edges:
            if not union(x, y):
                return [x, y]

            
                    
