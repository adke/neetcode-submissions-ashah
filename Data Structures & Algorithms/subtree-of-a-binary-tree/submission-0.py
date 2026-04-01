# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # pre-order traversal
        # add a function to represent sameTree
        if not root and subRoot:
            return False
        elif root and not subRoot:
            return True
        elif not root and not subRoot:
            return True
        else:

            if self.sameTree(root, subRoot):
                return True

            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)

            return left or right

    
    def sameTree(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:

            left = self.sameTree(p.left, q.left)
            right = self.sameTree(p.right, q.right)

            return left and right