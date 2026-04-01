# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # pre-order traversal
        # still will use DFS - recursion
        # execute the logic first for the node, then move to children (node, left, right)

        def dfs(node1, node2):

            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            elif node1.val != node2.val:
                return False
            else:
                left = dfs(node1.left, node2.left)
                right = dfs(node1.right, node2.right)

                return left and right

        return dfs(p,q)

