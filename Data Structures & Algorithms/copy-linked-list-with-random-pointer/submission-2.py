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
        if not head: return None
        current = head.next
        head2 = Node(head.val)
        nodes = {head : head2, None : None}
        
        while current:
            new = Node(current.val)
            head2.next = new
            nodes[current] = new
            current = current.next
            head2 = head2.next
       
        c2 = nodes[head]
        c1 = head
        while c2 and c1:
            c2.random = nodes[c1.random]
            c1 = c1.next
            c2 = c2.next

        return nodes[head]





        