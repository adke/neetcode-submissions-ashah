"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # first -> create copies of each node
        # second -> add the links
        originalToCopy = {None:None}

        curr = head
        while curr:
            copy = Node(curr.val)
            originalToCopy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            originalToCopy[curr].next = originalToCopy[curr.next]
            originalToCopy[curr].random = originalToCopy[curr.random]
            curr = curr.next

        return originalToCopy[head]


