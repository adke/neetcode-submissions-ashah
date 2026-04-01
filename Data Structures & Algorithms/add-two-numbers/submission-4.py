# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        r = 0

        while l1 or l2 or r:
            if not l1:
                val1 = 0
            else:
                val1 = l1.val
            if not l2:
                val2 = 0
            else:
                val2 = l2.val

            totalSum = val1 + val2 + r
            r = totalSum // 10
            totalSum = totalSum % 10

            curr.next = ListNode(totalSum)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next