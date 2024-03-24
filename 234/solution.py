# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        count, curr = 0, head
        while curr:
            curr = curr.next
            count += 1
            
        prev, curr = None, head
        for _ in range(count // 2):
            curr.next, prev, curr = prev, curr, curr.next
            
        p1, p2 = prev, curr.next if count % 2 else curr
        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1, p2 = p1.next, p2.next
            
        return True