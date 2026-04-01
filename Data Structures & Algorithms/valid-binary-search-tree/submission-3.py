# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(left, node, right):
            # base cases
            if not node:
                return True
            elif not (left < node.val < right):
                return False

            l = dfs(left, node.left, node.val)
            r = dfs(node.val, node.right, right)

            return l and r

        return dfs(float("-inf"), root, float("inf"))