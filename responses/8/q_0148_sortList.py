class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Divide the linked list into two halves
        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        # Recursively sort each half
        left = self.sortList(head)
        right = self.sortList(slow)

        # Merge the sorted halves
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode()
        curr = dummy

        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next

            curr = curr.next

        if left:
            curr.next = left
        else:
            curr.next = right

        return dummy.next
