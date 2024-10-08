from heapq import merge

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Find the middle of the linked list
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # Split the linked list into two halves
        mid = slow.next
        slow.next = None

        # Recursively sort the two halves
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(mid)

        # Merge the sorted halves
        return self.merge(left_sorted, right_sorted)

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 or l2

        return dummy.next
