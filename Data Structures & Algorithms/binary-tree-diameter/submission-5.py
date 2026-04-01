# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # POST-ORDER DFS QUESTION
        res = 0
        def dfs(node):
            nonlocal res
            # base case
            if not node:
                return -1 

            left = dfs(node.left)
            right = dfs(node.right)
            
            curr = left + right + 2
            res = max(res, curr)

            return 1 + max(left, right)

        dfs(root)

        return res
