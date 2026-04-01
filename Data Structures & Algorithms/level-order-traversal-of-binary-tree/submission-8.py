# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS PROBLEM
        # USE QUEUE TO SOLVE
        # ALGORITHM STOPS WHEN QUEUE IS EMPTY
        # IT IS GURANTEED TO GET EMPTY WHEN THERE IS NO CHILD NODE LEFT
        # TO ADD BACK TO THE QUEUE

        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            currlen = len(q)
            level = []
            for i in range(currlen):
                curr = q.popleft()
                level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(level)

        return res

        
