class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        # Find the length of the linked list
        current = head
        length = 1
        while current.next:
            current = current.next
            length += 1
        
        # Connect the last node to the head to make it a circular linked list
        current.next = head
        
        # Calculate the actual rotation amount
        k = k % length
        
        # Find the new tail and new head after rotation
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        
        # Break the linked list at the new tail
        new_tail.next = None
        
        return new_head
