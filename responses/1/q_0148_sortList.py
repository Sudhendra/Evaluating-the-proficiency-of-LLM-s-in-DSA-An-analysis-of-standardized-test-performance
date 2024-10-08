class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        mid = self.find_middle(head)
        left = head
        right = mid.next
        mid.next = None
        
        left_sorted = self.sortList(left)
        right_sorted = self.sortList(right)
        
        return self.merge(left_sorted, right_sorted)
    
    def find_middle(self, head):
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def merge(self, left, right):
        dummy = ListNode()
        curr = dummy
        
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        
        if left:
            curr.next = left
        if right:
            curr.next = right
        
        return dummy.next
