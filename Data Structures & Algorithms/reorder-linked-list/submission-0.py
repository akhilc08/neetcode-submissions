# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next 
        
        second = slow.next 
        prev = None
        while second:
            temp = second.next 
            second.next = prev
            prev = second
            second = temp

        first = head

        while prev != None: 
            temp1 = first.next 
            temp2 = prev.next
            first.next = prev
            prev.next = temp1
            first = temp1
            prev = temp2
        first.next = None

