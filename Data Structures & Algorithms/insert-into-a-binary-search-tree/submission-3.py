class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        def dfs(node):
            if not node:
                return False

            if val > node.val:
                right = dfs(node.right)
                if not right:
                    node.right = TreeNode(val)
                    return True
            else:
                left = dfs(node.left)
                if not left:
                    node.left = TreeNode(val)
                    return True
        
            return True

        dfs(root)

        return root