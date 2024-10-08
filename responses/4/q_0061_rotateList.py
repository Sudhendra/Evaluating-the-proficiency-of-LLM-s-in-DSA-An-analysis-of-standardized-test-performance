class Solution:
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Find the length of the linked list and the last node
        length = 1
        last_node = head
        while last_node.next:
            last_node = last_node.next
            length += 1
        
        # Calculate the actual number of rotations needed
        k = k % length
        
        if k == 0:
            return head
        
        # Find the new tail node that will be rotated to the head
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next
        
        # Define the new head and break the link to form two separate linked lists
        new_head = new_tail.next
        new_tail.next = None
        
        # Connect the original tail to the original head to form a circular list
        last_node.next = head
        
        return new_head
