# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next: return

        # Find the middle of the list
        slow, fast=head, head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next

        # Reverse the second half of the list
        prev=None
        cur=slow.next
        while cur:
            Next=cur.next
            cur.next=prev
            prev=cur
            cur=Next
        slow.next=None

        # Merge the 2 halves
        A, B=head, prev
        while A and B:
            A_next=A.next
            B_next=B.next  

            A.next=B
            B.next=A_next

            A=A_next
            B=B_next    