# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = l1
        b = l2
        # since we are creating a new linked list, create a dummy node
        dummy = ListNode(0)
        curr = dummy
        rem = 0

        while a or b or rem:
            if not a:
                val1 = 0
            else:
                val1 = a.val
            if not b:
                val2 = 0
            else:
                val2 = b.val

            total = val1 + val2 + rem
            rem = total // 10
            total = total % 10

            newNode = ListNode(total)
            curr.next = newNode
            curr = curr.next

            if a:
                a = a.next
            if b:
                b = b.next

        return dummy.next
