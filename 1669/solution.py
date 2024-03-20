# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr = list1 
        prev = None 
        t = a
        while t > 0:
            prev = curr
            curr = curr.next 
            t -= 1
        
        curr = prev
        prev2 = None
        t = b - a + 2
        while t >= 0:
            prev2 = curr 
            curr = curr.next 
            t -= 1

        prev.next = list2

        head = list1 
        tail = None 
        while head:
            tail = head
            head = head.next 

        tail.next = prev2 

        return list1 
