class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        
        while cur and cur.next:
            if cur.val <= cur.next.val:
                cur = cur.next
            else:
                pre = dummy
                tmp = cur.next
                
                while pre.next.val <= tmp.val:
                    pre = pre.next
                
                cur.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
        
        return dummy.next
