# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # PRE-ORDER TRAVERSAL (DFS)
        def dfs(left, node, right):
            if not node:
                return True
            
            # process node first, then go to children
            if not (node.val >left and node.val < right):
                return False
            else:
                left = dfs(left, node.left, node.val)
                right = dfs(node.val, node.right, right)

                return left and right

        return dfs(float("-inf"), root, float("inf"))
