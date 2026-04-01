"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        original_to_copy = {}

        def dfs(node):
            if node in original_to_copy:
                return original_to_copy[node]

            copy = Node(node.val)
            original_to_copy[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        if node:
            return dfs(node)
        else:
            return None