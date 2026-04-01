# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # node, left, right

        def dfs(node, currMax):
            # process currNode
            if not node:
                return 0
            elif node.val >= currMax:
                res = 1
            else:
                res = 0
            
            currMax = max(node.val, currMax)
            res += dfs(node.left, currMax)
            res += dfs(node.right, currMax)

            return res

        return dfs(root, root.val)
