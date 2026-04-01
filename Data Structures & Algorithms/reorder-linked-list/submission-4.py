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
            slow = slow.next
            fast = fast.next.next

        secondHead = slow.next
        slow.next = None
        prev = None

        while secondHead:
            temp = secondHead.next
            secondHead.next = prev
            prev = secondHead
            secondHead = temp

        head2 = prev
        head1 = head

        while head2:
            temp1 = head1.next
            temp2 = head2.next
            head1.next = head2
            head2.next = temp1
            head1 = temp1
            head2 = temp2

