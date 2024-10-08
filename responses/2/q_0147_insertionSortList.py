class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        curr = head
        prev = dummy

        while curr:
            if curr.next and curr.next.val < curr.val:
                while prev.next and prev.next.val < curr.next.val:
                    prev = prev.next

                temp = prev.next
                prev.next = curr.next
                curr.next = curr.next.next
                prev.next.next = temp
                prev = dummy
            else:
                curr = curr.next

        return dummy.next
