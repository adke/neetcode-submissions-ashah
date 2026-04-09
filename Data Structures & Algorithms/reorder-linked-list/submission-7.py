# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # the slow pointer will be the last node of list 1
        newHead = slow.next
        slow.next = None
        prev = None
        curr = newHead

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        curr2 = prev # prev will be the head of list 2 since we reversed it
        curr = head


        while curr2:
            temp1 = curr.next
            temp2 = curr2.next
            curr.next = curr2
            curr2.next = temp1
            curr = temp1
            curr2 = temp2

        
