# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                value1 = l1.val
            else:
                value1 = 0

            if l2:
                value2 = l2.val
            else:
                value2 = 0

            valueSum = value1 + value2 + carry
            carry = valueSum // 10
            valueSum = valueSum % 10

            curr.next = ListNode(valueSum)
            curr = curr.next

            if l1:
                l1 = l1.next
            else:
                l1 = l1
            
            if l2:
                l2 = l2.next
            else:
                l2 = l2

        return dummy.next

            
            
            
