# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        i = 0
        res = 0 
        
        c1 = l1
        c2 = l2

        while  c2: 
            res += c2.val* 10**i
            i+=1
            c2 = c2.next
        
        i=0
        while c1: 
            res += c1.val * 10**i
            i+=1
            c1 = c1.next

        head = ListNode(int(res%10))
        res //= 10
        curr = head
        while res > 0: 
            curr.next = ListNode(int(res%10))
            curr = curr.next
            res //= 10
        
        return head



        