from collections import Counter

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        counter = Counter()
        
        # Count occurrences of each value
        while node:
            counter[node.val] += 1
            node = node.next
        
        dummy = ListNode(0)
        dummy.next = head
        prev, curr = dummy, head
        
        # Remove nodes with duplicate values
        while curr:
            if counter[curr.val] > 1:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return dummy.next
