class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseLinkedList(head, k):
            prev, cur = None, head
            while k > 0:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                k -= 1
            return prev, cur

        def reverseKNodes(head, k):
            count = 0
            cur = head
            while cur and count < k:
                cur = cur.next
                count += 1
            if count == k:
                new_head, new_tail = reverseLinkedList(head, k)
                head.next = reverseKNodes(cur, k)
                return new_head
            else:
                return head

        return reverseKNodes(head, k)
