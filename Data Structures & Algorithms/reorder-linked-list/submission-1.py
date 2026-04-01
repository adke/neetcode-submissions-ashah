# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        prev, slow.next = None, None

        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        second = prev # head of second LL which is reversed
        first = head
        
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        

            


