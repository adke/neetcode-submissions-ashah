# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # execute post-order traversal
        maxSum = root.val

        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            left = max(left, 0)
            right = max(right, 0)

            maxSum = max(maxSum, left + right + node.val)

            return node.val + max(left, right)

        dfs(root)

        return maxSum