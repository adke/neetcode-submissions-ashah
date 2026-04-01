class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # path compression
        # union by rank 
        num = len(edges) # since 1 cycle is guranteed
        rank = [1] * (num + 1)
        parent = [i for i in range(num + 1)]

        def findRootParent(n):
            if n == parent[n]:
                return parent[n]
            else:
                return findRootParent(parent[n])


        def unionRank(n1, n2):
            p1 = findRootParent(n1)
            p2 = findRootParent(n2)
            if p1 == p2:
                return False
            # use rank to update node's parent
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not unionRank(n1, n2):
                return [n1, n2]

        