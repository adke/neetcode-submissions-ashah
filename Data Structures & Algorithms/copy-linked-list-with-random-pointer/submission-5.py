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
        # use a hashmap to store the copy nodes under the original nodes
        copy = {None:None}
        curr = head

        while curr:
            copyNode = Node(curr.val)
            copy[curr] = copyNode
            curr = curr.next

        curr = head

        while curr:
            copy[curr].next = copy[curr.next]
            copy[curr].random = copy[curr.random]
            curr = curr.next

        return copy[head]
        

        