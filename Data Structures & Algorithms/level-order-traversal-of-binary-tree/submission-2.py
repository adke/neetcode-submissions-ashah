# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
            
        res = []

        q = deque([root])

        while q:
            currLen = len(q)
            levelList = []

            for i in range(currLen):
                currNode = q.popleft()
                levelList.append(currNode.val)

                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
            
            res.append(levelList)
        
        return res
