# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        res_head = None
        if curr1 == None:
            return curr2
        elif curr2 == None:
            return curr1

        if curr1.val < curr2.val: 
            res_head = curr1
            curr1 = curr1.next
        else: 
            res_head = curr2
            curr2 = curr2.next
        
        res_curr = res_head
        while(curr1 != None and curr2 != None):
            if curr1.val < curr2.val:
                res_curr.next = curr1
                curr1 = curr1.next
            else: 
                res_curr.next = curr2
                curr2 = curr2.next
            res_curr = res_curr.next 

        print("check")

        while curr1 != None: 
            res_curr.next = curr1
            res_curr = res_curr.next
            curr1 = curr1.next

        while curr2 != None:
            res_curr.next = curr2
            res_curr = res_curr.next
            curr2 = curr2.next

        return res_head
