"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copy = {}

        def dfs(nodee):
            if nodee in copy:
                return copy[nodee]
            else:
                copyNode = Node(nodee.val)
                copy[nodee] = copyNode

                for nei in nodee.neighbors:
                    copyNode.neighbors.append(dfs(nei))

                return copyNode

        if node:
            return dfs(node)
        else:
            return None