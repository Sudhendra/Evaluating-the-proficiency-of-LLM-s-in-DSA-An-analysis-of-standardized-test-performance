class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Find the length of the linked list
        length = 1
        current = head
        while current.next:
            length += 1
            current = current.next
        
        # Adjust k to be less than the length of the linked list
        k = k % length
        
        if k == 0:
            return head
        
        # Find the new tail (kth node from the end) and the new head (node right before the new tail)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        
        # Rotate the list
        new_tail.next = None
        current = new_head
        while current.next:
            current = current.next
        current.next = head
        
        return new_head
