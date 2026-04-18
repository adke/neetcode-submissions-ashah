# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getK(groupPrev, k)
            if not kth:
                break
            curr = groupPrev.next
            groupNext = kth.next
            prev = None
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = groupPrev.next
            groupPrev.next.next = curr
            groupPrev.next = prev
            groupPrev = temp

        return dummy.next


        

    def getK(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1

        return curr