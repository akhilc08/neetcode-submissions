# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        map = {}
        index = 0
        curr = head
        while curr != None: 
            if curr in map: 
                return True
            else: 
                map[curr] = index
                curr = curr.next 

        return False