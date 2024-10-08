class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current.next and current.next.next:
            if current.next.val == current.next.next.val:
                val = current.next.val
                while current.next and current.next.val == val:
                    current.next = current.next.next
            else:
                current = current.next
        
        return dummy.next
