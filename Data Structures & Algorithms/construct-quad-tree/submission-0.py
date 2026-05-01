"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(n, r, c):
            # base case
            isSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r][c] != grid[r + i][c + j]:
                        isSame = False
                        break
            if isSame:
                return Node(grid[r][c], True, None, None, None, None)
            
            n = n // 2
            leftT = dfs(n, r, c)
            rightT = dfs(n, r, c + n)
            leftB = dfs(n, r + n, c)
            rightB = dfs(n, r + n, c + n)

            return Node(0, False, leftT, rightT, leftB, rightB)

        return dfs(len(grid), 0, 0)