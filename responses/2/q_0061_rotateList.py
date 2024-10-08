class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        # Count the length of the linked list
        current = head
        list_length = 1
        while current.next:
            current = current.next
            list_length += 1
        
        # Connect the last node with the first node to form a circular linked list
        current.next = head
        
        # Find the new tail at position length - k % length
        new_tail_position = list_length - k % list_length
        new_tail = head
        for _ in range(new_tail_position - 1):
            new_tail = new_tail.next
        
        # Break the circular connection at the new tail and update the head
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head