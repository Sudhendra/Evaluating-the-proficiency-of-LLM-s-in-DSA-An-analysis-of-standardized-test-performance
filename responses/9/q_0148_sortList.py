class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        middle = self.find_middle(head)
        left, right = head, middle.next
        middle.next = None
        
        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)
        
        return self.merge(left_sorted, right_sorted)
    
    def find_middle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        
        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        
        if left:
            current.next = left
        if right:
            current.next = right
        
        return dummy.next
