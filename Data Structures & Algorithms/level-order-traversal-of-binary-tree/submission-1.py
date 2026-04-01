# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root])

        while q:
            currLen = len(q)
            sublist = []

            for i in range(currLen):
                node = q.popleft()
                
                if node:
                    sublist.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            
            if sublist:
                res.append(sublist)
            
        return res

