# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # pre-order traversal
        # left, right, node
        res = []
        def dfs(node):
            nonlocal res

            if not node:
                res.append("N")
                return

            res.append(str(node.val))

            left = dfs(node.left)
            right = dfs(node.right)

            return

        dfs(root)

        print(res)
        return ",".join(res)
     
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        res = data.split(",") # creates a list of elements seperator by ,
        # NEED TO USE PRE-ORDER TRAVERSAL HERE AS WELL
        i = 0
        def dfs():
            nonlocal i
            if res[i] == "N":
                i += 1
                return None

            node = TreeNode(int(res[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()

                

            
