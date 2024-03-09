# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = 0 
        curr = head 
        while curr:
            c += 1 
            curr = curr.next 
        
        n = c // 2

        while n > 0:
            head = head.next 
            n -= 1
        
        return head