# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # pre-order traversal
        def dfs(left, node, right):
            if not node:
                return True
            elif not (node.val > left and node.val < right):
                return False
            else:

                leftChild = dfs(left, node.left, node.val)
                rightChild = dfs(node.val, node.right, right)

                return (leftChild and rightChild)

        return dfs(float("-inf"), root, float("inf"))

            
