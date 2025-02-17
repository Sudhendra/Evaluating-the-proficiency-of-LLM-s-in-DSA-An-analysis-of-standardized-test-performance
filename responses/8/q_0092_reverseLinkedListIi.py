class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        
        for _ in range(left - 1):
            pre = pre.next
        
        curr = pre.next
        
        for _ in range(right - left):
            temp = pre.next
            pre.next = curr.next
            curr.next = curr.next.next
            pre.next.next = temp
        
        return dummy.next
