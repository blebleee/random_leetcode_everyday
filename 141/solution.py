# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = {}
        curr = head 

        while curr is not None:
            if curr in d:
                return True
            d[curr] = 1
            curr = curr.next 
        
        return False