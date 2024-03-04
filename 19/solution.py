class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None: 
            return 

        dummy_node = ListNode(0)    
        dummy_node.next = head 

        fast = dummy_node        
        for i in range(n): 
            fast = fast.next

        slow = dummy_node    
        while fast.next is not None: 
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next 
        return dummy_node.next    