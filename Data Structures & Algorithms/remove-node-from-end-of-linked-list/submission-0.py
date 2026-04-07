# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        first = head
        second = head
        count = 0
        while count < n and second:
            second = second.next 
            count += 1
        prev = None
        while second: 
            second = second.next
            prev = first
            first = first.next 
        
        if prev == None: 
            return first.next
        prev.next = first.next 
        return head
        
