class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(head, tail):
            prev = tail
            current = head

            while current != tail:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            return prev

        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while True:
            count = 0
            group_start = prev_group_end.next
            group_end = group_start

            while count < k and group_end is not None:
                group_end = group_end.next
                count += 1

            if count < k:
                break

            next_group_start = group_end  # Save the next group starting node

            new_group_start = reverse(group_start, group_end)
            prev_group_end.next = new_group_start
            group_start.next = next_group_start

            prev_group_end = group_start

        return dummy.next
