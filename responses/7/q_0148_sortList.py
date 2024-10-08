class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Split the linked list into two halves
        mid = self.find_middle(head)
        left = head
        right = mid.next
        mid.next = None
        
        # Recursively sort both halves
        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)
        
        # Merge the sorted halves
        return self.merge(left_sorted, right_sorted)
    
    def find_middle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head.next
        
        while fast and fast.next:
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
        
        current.next = left if left else right
        
        return dummy.next
