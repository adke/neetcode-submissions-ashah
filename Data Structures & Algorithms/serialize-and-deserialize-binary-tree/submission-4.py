# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serial = []
        def dfs(node):
            nonlocal serial
            if not node:
                serial.append("N")
                return
            
            serial.append(str(node.val))

            left = dfs(node.left)
            right = dfs(node.right)
            return
        
        dfs(root)
        print(serial)
        return ",".join(serial)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tree = data.split(",")
        i = 0
        def dfs():
            nonlocal i
            if tree[i] == "N":
                i += 1
                return None

            node = TreeNode(int(tree[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
        