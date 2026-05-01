# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, currMax):
            if not node:
                return 0
            
            isGood = False
            if node.val >= currMax:
                isGood = True
                currMax = node.val
            left = dfs(node.left, currMax)
            right = dfs(node.right, currMax)

            if isGood:
                return left + right + 1
            else:
                return left + right
        
        return dfs(root, root.val)
            