"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        Hashmap = { None : None }
        curr = head
        while curr:
            copy = Node(curr.val)
            Hashmap[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = Hashmap[curr]
            copy.next = Hashmap[curr.next]
            copy.random = Hashmap[curr.random]

            curr = curr.next



        return Hashmap[head]