class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseLinkedList(head, k):
            prev = None
            curr = head
            while k > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev
        
        def getLength(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length
        
        length = getLength(head)
        if length < k:
            return head
        
        new_head = None
        prev_tail = None
        curr_head = head
        while length >= k:
            count = 0
            prev_group_tail = prev_tail
            group_head = curr_head
            while count < k:
                prev_tail = curr_head
                curr_head = curr_head.next
                count += 1
            group_tail = prev_tail
            if new_head is None:
                new_head = reverseLinkedList(group_head, k)
            if prev_group_tail:
                prev_group_tail.next = group_tail
            length -= k
        
        if group_tail:
            group_tail.next = curr_head
        
        return new_head