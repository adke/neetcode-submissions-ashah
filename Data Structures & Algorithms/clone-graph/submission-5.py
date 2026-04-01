"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        copy = {}

        def dfs(node):
            # base case always
            if node in copy:
                return copy[node]
            else:
                copyN = Node(node.val)
                copy[node] = copyN

                for nei in node.neighbors:
                    copyN.neighbors.append(dfs(nei))

                return copyN
                
        return dfs(node)