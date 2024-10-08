class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Get the length of the list and the last node
        length = 1
        last_node = head
        while last_node.next:
            last_node = last_node.next
            length += 1

        # Close the linked list to make it a circle
        last_node.next = head
        
        k = k % length  # Get the actual rotation amount

        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next

        new_tail.next = None

        return new_head
