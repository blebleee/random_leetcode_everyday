# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefixSum = 0
        mp = {}
        dummy = ListNode(0)
        dummy.next = head
        mp[0] = dummy
        while head:
            prefixSum += head.val
            if prefixSum in mp:
                start = mp[prefixSum]
                temp = start
                pSum = prefixSum
                while temp != head:
                    temp = temp.next
                    pSum += temp.val
                    if temp != head:
                        del mp[pSum]
                start.next = head.next
            else:
                mp[prefixSum] = head
            head = head.next
        return dummy.next