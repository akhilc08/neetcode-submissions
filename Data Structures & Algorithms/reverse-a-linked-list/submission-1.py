# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        stack = []
        current = head
        stack.append(current)
        while current.next != None:
            current = current.next
            stack.append(current)
        head = stack.pop()
        current = head
        print(stack)
        while len(stack) != 0:
            current.next = stack.pop()
            current = current.next
        current.next = None
        return head
