# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
     if not root:
        return 0

     q = deque([root])
     level = 0
    
     while q:

        currlen = len(q)

        for i in range(currlen):
            currNode = q.popleft()

            if currNode.left:
                q.append(currNode.left)
            if currNode.right:
                q.append(currNode.right)
        
        level += 1
    
     return level
