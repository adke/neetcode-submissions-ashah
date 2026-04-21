# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(n1, n2):
            if not n1 and n2:
                return False
            elif not n2 and n1:
                return False
            elif not n2 and not n1:
                return True
            elif n1.val != n2.val:
                return False
            else:
                left = dfs(n1.left, n2.left)
                right = dfs(n1.right, n2.right)

                return left and right

        return dfs(p, q)
