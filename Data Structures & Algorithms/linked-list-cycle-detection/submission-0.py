# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return False

        left = head

        right = head.next

        while left != right:
            if not right or not right.next:
                return False

            left = left.next
            right = right.next.next

        return True
        
        