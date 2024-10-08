def reorderList(self, head: Optional[ListNode]) -> None:
    if not head or not head.next:
        return

    # Find the middle of the linked list using slow and fast pointers
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list
    prev, curr = None, slow.next
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    slow.next = None

    # Merge the first and reversed second half of the linked list
    first, second = head, prev
    while second:
        next_first, next_second = first.next, second.next
        first.next = second
        second.next = next_first
        first, second = next_first, next_second
