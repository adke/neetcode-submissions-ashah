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

       while (l1 or l2 or carry):
        if l1:
            value1 = l1.val
        else:
            value1 = 0
        if l2:
            value2 = l2.val
        else:
            value2 = 0
        
        value3 = value1 + value2 + carry
        carry = value3 // 10
        value3 = value3 % 10

        curr.next = ListNode(value3)

        if l1:
            l1 = l1.next
        else:
            l1 = l1
        if l2:
            l2 = l2.next
        else:
            l2 = l2
        
        curr = curr.next

       return dummy.next
        

            
            
            
