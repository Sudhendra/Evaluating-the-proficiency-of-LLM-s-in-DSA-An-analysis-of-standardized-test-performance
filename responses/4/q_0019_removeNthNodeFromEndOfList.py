class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        # Move the second pointer n nodes ahead
        for _ in range(n + 1):
            second = second.next

        # Move first and second pointers until the second pointer reaches the end
        while second is not None:
            first = first.next
            second = second.next

        # Remove the nth node from the end
        first.next = first.next.next

        return dummy.next
