class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        # Count the length of the linked list
        length = 1
        curr = head
        while curr.next:
            length += 1
            curr = curr.next
        
        # Adjust `k` to avoid unnecessary rotations
        k = k % length
        if k == 0:
            return head
        
        # Find the new tail and break the cycle
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        
        # Connect the original tail to the original head
        curr.next = head
        
        return new_head
