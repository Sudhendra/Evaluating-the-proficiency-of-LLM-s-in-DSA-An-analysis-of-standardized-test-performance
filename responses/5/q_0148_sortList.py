class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Split the list into two halves
        middle = self.find_middle(head)
        second_half = middle.next
        middle.next = None
        
        # Recursively sort the two halves
        sorted_first_half = self.sortList(head)
        sorted_second_half = self.sortList(second_half)
        
        # Merge the sorted halves
        return self.merge(sorted_first_half, sorted_second_half)
    
    def find_middle(self, head):
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next
