class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseLinkedList(head: Optional[ListNode], k: int) -> Optional[ListNode]:
            count = 0
            current = head
            while current and count < k:
                current = current.next
                count += 1
            if count < k:
                return head
            new_head = None
            prev = None
            current = head
            count = 0
            while current and count < k:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
                count += 1
            if current:
                head.next = reverseLinkedList(current, k)
            return prev
        
        return reverseLinkedList(head, k)