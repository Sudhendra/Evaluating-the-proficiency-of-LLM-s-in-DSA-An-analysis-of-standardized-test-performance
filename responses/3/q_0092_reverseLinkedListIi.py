class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
    
        for _ in range(left - 1):
            pre = pre.next
        
        current = pre.next
        for _ in range(right - left):
            temp = pre.next
            pre.next = current.next
            current.next = current.next.next
            pre.next.next = temp
    
        return dummy.next