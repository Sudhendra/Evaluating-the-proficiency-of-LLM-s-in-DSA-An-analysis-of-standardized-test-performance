class Solution:
    def reverseList_iteratively(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reverseList_recursively(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        p = self.reverseList_recursively(head.next)
        head.next.next = head
        head.next = None
        return p
