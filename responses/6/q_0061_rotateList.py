class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Calculate the length of the linked list
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        
        # Connect the tail to the head to form a cycle
        current.next = head
        
        # Calculate the actual number of rotations needed
        k = k % length
        
        # Find the new tail position
        for _ in range(length - k):
            current = current.next
        
        # Disconnect at the new tail position
        new_head = current.next
        current.next = None
        
        return new_head
