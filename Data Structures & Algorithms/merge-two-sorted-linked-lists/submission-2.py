# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: return None
        if not list1: return list2
        if not list2: return list1
        
        c1 = list1
        c2 = list2
        res = None
        
        if c1.val < c2.val: 
            res = c1
            c1 = c1.next
        else: 
            res = c2
            c2 = c2.next

        curr = res

        while c1 or c2: 
            v1 = c1.val if c1 else math.inf
            v2 = c2.val if c2 else math.inf

            if v1<v2:
                curr.next = ListNode(v1)
                c1 = c1.next
            else: 
                curr.next = ListNode(v2)
                c2 = c2.next
            curr = curr.next
        return res


