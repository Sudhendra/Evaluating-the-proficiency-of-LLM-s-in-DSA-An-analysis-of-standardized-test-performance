class Solution:
    def insertionSortList(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head

        curr = head

        while curr.next:
            if curr.val > curr.next.val:
                prev = dummy
                while prev.next.val < curr.next.val:
                    prev = prev.next

                temp = curr.next
                curr.next = temp.next
                temp.next = prev.next
                prev.next = temp
            else:
                curr = curr.next

        return dummy.next
