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
            node = head
            while count < k and node:
                node = node.next
                count += 1
            return count == k

        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        while reverseKNodes(prev_group_end.next, k):
            group_start = prev_group_end.next
            group_end = group_start
            prev_group_end_next = group_start
            for _ in range(k-1):
                group_end = group_end.next
            group_end_next = group_end.next
            group_end.next = None
            prev_group_end.next, group_end = reverseLinkedList(group_start, k)
            group_end.next = group_end_next
            prev_group_end = group_end

        return dummy.next
