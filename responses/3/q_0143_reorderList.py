class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return

        # Find the middle of the linked list
        slow_ptr = fast_ptr = head
        while fast_ptr.next and fast_ptr.next.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        # Reverse the second half of the linked list
        prev_node, curr_node = None, slow_ptr.next
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        slow_ptr.next = None

        # Merge two halves of the linked list
        first_ptr, second_ptr = head, prev_node
        while second_ptr:
            next_first = first_ptr.next
            next_second = second_ptr.next
            first_ptr.next = second_ptr
            second_ptr.next = next_first
            first_ptr = next_first
            second_ptr = next_second
