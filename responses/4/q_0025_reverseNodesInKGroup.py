class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse_sublist(start, end):
            prev, curr = None, start
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        def get_sublist_length(start):
            length = 0
            while start:
                length += 1
                start = start.next
            return length

        dummy = ListNode()
        dummy.next = head
        prev_group_end = dummy
        while True:
            sublist_length = get_sublist_length(prev_group_end.next)
            if sublist_length < k:
                break
            group_start = prev_group_end.next
            group_end = group_start
            for _ in range(k - 1):
                group_end = group_end.next

            next_group_start = group_end.next

            new_group_start = reverse_sublist(group_start, next_group_start)
    
            prev_group_end.next = group_end
            group_start.next = next_group_start

            prev_group_end = group_start

        return dummy.next
