class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseLinkedList(head: Optional[ListNode], k: int) -> Tuple[Optional[ListNode], Optional[ListNode]]:
            node = head
            count = 0
            while node and count < k:
                node = node.next
                count += 1
            if count == k:
                prev, curr = None, head
                for _ in range(k):
                    tmp = curr.next
                    curr.next = prev
                    prev, curr = curr, tmp
                head.next = reverseLinkedList(curr, k)[0] if curr else None
                return prev, head
            return head, node
        
        new_head, _ = reverseLinkedList(head, k)
        return new_head
