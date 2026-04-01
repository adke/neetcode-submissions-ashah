# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, left, right):
            if not node:
                return True
            
            if not (node.val > left and node.val < right):
                return False
            
            else:
                leftbool = dfs(node.left, left, node.val)
                rightbool = dfs(node.right, node.val, right)

            return leftbool and rightbool

        return dfs(root, float("-inf"), float("inf"))