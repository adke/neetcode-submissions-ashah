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

        newHead = slow.next
        slow.next = None
        prev = None

        # reverse second-half of the linked list

        curr = newHead
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        newHead = prev
        oldCurr = head

        while newHead:
            temp1 = oldCurr.next
            temp2 = newHead.next
            oldCurr.next = newHead
            newHead.next = temp1
            oldCurr = temp1
            newHead = temp2




