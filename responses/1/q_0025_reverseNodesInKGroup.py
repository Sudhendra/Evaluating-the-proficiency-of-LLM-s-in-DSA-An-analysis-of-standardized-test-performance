class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseLinkedList(head, k):
            prev = None
            curr = head
            while k > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev, curr
        
        def reverseKNodes(head, k):
            count = 0
            curr = head
            while count < k and curr:
                curr = curr.next
                count += 1
            if count < k:
                return head
            reversed_head, next_head = reverseLinkedList(head, k)
            head.next = reverseKNodes(next_head, k)
            return reversed_head
        
        return reverseKNodes(head, k)
