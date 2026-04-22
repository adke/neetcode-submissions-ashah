# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and not subRoot:
            return True
        elif not root and not subRoot:
            return True
        elif not root and subRoot:
            return False
        else:
            currRes = self.isSame(root, subRoot)
            if currRes:
                return True
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)

            return left or right

    def isSame(self, n1, n2):
        if not n1 and n2:
            return False
        elif not n2 and n1:
            return False
        elif not n1 and not n2:
            return True
        elif n1.val != n2.val:
            return False
        else:
            left = self.isSame(n1.left, n2.left)
            right = self.isSame(n1.right, n2.right)

            return left and right
