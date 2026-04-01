# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # POST-ORDER TRAVERSAL
        # NEED TO RETURN [BOOLEAN, HEIGHT]
        def dfs(node):
            if not node:
                return [True, 0]

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left[1] - right[1]) <= 1:
                res = True
            else:
                res = False

            return [left[0] and right[0] and res, max(left[1], right[1]) + 1]

        return dfs(root)[0]