# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        aNode = root

        while True:

            if p.val < aNode.val and q.val < aNode.val:
                aNode = aNode.left
            elif p.val > aNode.val and q.val > aNode.val:
                aNode = aNode.right
            else:
                return aNode