# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            currLen = len(q)
            rightNode = None

            for i in range(currLen):
                node = q.popleft()
                if node:
                    rightNode = node

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            if rightNode:
                res.append(rightNode.val)
        
        return res

