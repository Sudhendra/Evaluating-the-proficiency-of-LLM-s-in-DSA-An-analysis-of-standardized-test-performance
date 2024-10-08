class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float('-inf'))  # Create a dummy node as the start of the sorted list
        curr = head
        
        while curr:
            prev = dummy
            next_node = curr.next
            
            # Find the correct position to insert the current node in the sorted list
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            # Insert the current node in the sorted list
            curr.next = prev.next
            prev.next = curr
            
            curr = next_node
        
        return dummy.next  # Return the sorted list without the dummy node
