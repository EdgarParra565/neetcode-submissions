# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        gPrev = dummy

        while True:
            kth = self.getK(gPrev, k)
            if not kth:
                break
            gNext = kth.next

            prev, curr = kth.next, gPrev.next
            while curr != gNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = gPrev.next
            gPrev.next = kth
            gPrev = temp
        return dummy.next

    def getK(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr